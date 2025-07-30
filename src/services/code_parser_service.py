import uuid
import os
from pathlib import Path
from tree_sitter_languages import get_language
from tree_sitter import Parser

# Importing custom interfaces and models
from src.interfaces import ICodeParserService, ParsedCodeModel, FunctionNode, ClassNode

# Define path to the compiled tree-sitter language shared library (.dll/.so/.dylib)
DLL_PATH = os.path.join(os.path.dirname(__file__), '..', '..', 'build', 'my-languages.dll')

# Load Python language for tree-sitter
PY_LANGUAGE = get_language('python')

# Initialize a parser instance
parser = Parser()
parser.set_language(PY_LANGUAGE)


class CodeParserService(ICodeParserService):
    """
    Service class to parse source code and extract structure like functions and classes.
    Inherits from ICodeParserService interface.
    """

    def __init__(self):
        """
        Initializes a new parser specifically for Python source code.
        """
        self.pythonParser = Parser()
        self.pythonParser.set_language(PY_LANGUAGE)

    def identifyLanguage(self, filePath: Path) -> str:
        """
        Identify programming language based on file extension.

        Args:
            filePath (Path): The file path of the source code file.

        Returns:
            str: Name of the detected language ('python', 'javascript', or 'unknown').
        """
        suffix = Path(filePath).suffix
        if suffix == '.py':
            return "python"
        elif suffix == '.js':
            return "javascript"
        else:
            return "unknown"

    def parseCode(self, filePath: Path, codeContent: str) -> ParsedCodeModel:
        """
        Parses the given code content and extracts function and class definitions.

        Args:
            filePath (Path): The path of the source code file.
            codeContent (str): The content of the source code file.

        Returns:
            ParsedCodeModel: Structured representation of the parsed code.
        """
        # Parse the code to generate the syntax tree
        tree = self.pythonParser.parse(bytes(codeContent, "utf8"))
        root_node = tree.root_node

        fileId = uuid.uuid4().hex  # Unique ID for this file
        functions = []  # List to store function nodes
        classes = []    # List to store class nodes

        def traverse(node):
            """
            Recursive function to traverse the AST and extract class/function definitions.

            Args:
                node: Current AST node being visited.
            """
            if node.type == 'function_definition':
                name_node = node.child_by_field_name('name')
                if name_node is not None:
                    name = name_node.text.decode('utf-8')
                    start_line = node.start_point[0] + 1
                    end_line = node.end_point[0] + 1
                    functions.append(FunctionNode(
                        id=f'func_uuid_{name}',
                        name=name,
                        fileId=fileId,
                        startLine=start_line,
                        endLine=end_line
                    ))

            elif node.type == 'class_definition':
                name_node = node.child_by_field_name('name')
                if name_node is not None:
                    name = name_node.text.decode('utf-8')
                    start_line = node.start_point[0] + 1
                    end_line = node.end_point[0] + 1
                    classes.append(ClassNode(
                        id=f'class_uuid_{name.lower()}',
                        name=name,
                        fileId=fileId,
                        startLine=start_line,
                        endLine=end_line
                    ))

            # Recursively visit all children
            for child in node.children:
                traverse(child)

        # Start traversing from the root node
        traverse(root_node)

        # Return a structured representation of the parsed data
        return ParsedCodeModel(
            id=fileId,
            filePath=str(filePath),
            language=self.identifyLanguage(filePath),
            functions=functions,
            classes=classes
        )
