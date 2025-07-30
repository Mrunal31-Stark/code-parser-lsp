from typing import List
from pathlib import Path
from pydantic import BaseModel
from abc import ABC, abstractmethod

class FunctionNode(BaseModel):
    """Represents a function's metadata in the parsed code."""
    id: str
    name: str
    fileId: str
    startLine: int
    endLine: int

class ClassNode(BaseModel):
    """Represents a class's metadata in the parsed code."""
    id: str
    name: str
    fileId: str
    startLine: int
    endLine: int

class ParsedCodeModel(BaseModel):
    """Represents the full parsed result of a source code file."""
    id: str
    filePath: str
    language: str
    functions: List[FunctionNode]
    classes: List[ClassNode]

class ICodeParserService(ABC):
    """Abstract interface for code parsing operations using Tree-sitter."""
    
    @abstractmethod
    def identifyLanguage(self, filePath: Path) -> str:
        """Identify the programming language based on file extension or content."""
        pass

    @abstractmethod
    def parseCode(self, filePath: Path, codeContent: str) -> ParsedCodeModel:
        """Parse code and return its structure as functions and classes."""
        pass
