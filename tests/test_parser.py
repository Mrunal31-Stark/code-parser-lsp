import os
import sys
import json

# Add project root to the Python path for module resolution
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import the CodeParserService and model for parsing code
from src.services.code_parser_service import CodeParserService, ParsedCodeModel

class CodeDirectoryParser:
    """
    Class to handle parsing of all Python files within a directory using CodeParserService.
    """

    def __init__(self, folder_path: str):
        """
        Initialize the parser with the directory to scan.
        :param folder_path: Path to the directory containing Python files
        """
        self.folder_path = folder_path
        self.parser = CodeParserService()

    def get_all_python_files(self) -> list:
        """
        Recursively collects all .py files from the folder path.
        :return: List of absolute file paths
        """
        python_files = []
        for root, _, files in os.walk(self.folder_path):
            for file in files:
                if file.endswith(".py"):
                    python_files.append(os.path.join(root, file))
        return python_files

    def parse_files(self) -> list:
        """
        Parses all Python files found in the directory.
        :return: List of parsed results as dictionaries
        """
        if not os.path.exists(self.folder_path):
            print(f"❌ Folder not found: {self.folder_path}")
            return []

        all_files = self.get_all_python_files()
        if not all_files:
            print("⚠️ No Python files found.")
            return []

        results = []

        for file_path in all_files:
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()

            print(f"🔍 Parsing: {file_path}")
            result: ParsedCodeModel = self.parser.parseCode(file_path, content)
            results.append(result.model_dump())

        return results

    def export_results_as_json(self, output_path: str = None):
        """
        Parses files and prints or saves results as JSON.
        :param output_path: Optional file path to save the JSON output
        """
        results = self.parse_files()

        if output_path:
            with open(output_path, "w", encoding="utf-8") as out_file:
                json.dump(results, out_file, indent=2)
            print(f"✅ Output saved to: {output_path}")
        else:
            print(json.dumps(results, indent=2))


def main():
    # Directory to scan (change if needed)
    folder_path = "examples"
    
    # Output file (optional): change to None if not saving to file
    output_json_path = None

    # Create parser object and run parsing
    parser = CodeDirectoryParser(folder_path)
    parser.export_results_as_json(output_path=output_json_path)

if __name__ == "__main__":
    main()
