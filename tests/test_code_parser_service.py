# tests/test_code_parser_service.py
import sys
import os
from src.services.code_parser_service import CodeParserService
from pathlib import Path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_python_parsing_function_and_class():
    service = CodeParserService()
    mock_code = """
class MyClass:
    def method_one(self):
        pass

def standalone_function():
    pass
"""
    file_path = Path("sample.py")
    result = service.parseCode(file_path, mock_code)

    assert result.language == "python"
    assert len(result.classes) == 1
    assert result.classes[0].name == "MyClass"
    assert len(result.functions) == 2  # method_one + standalone_function
