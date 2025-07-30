# modules.py

from src.services.code_parser_service import CodeParserService

# Registry for supported languages
PARSER_SERVICES = {
    "python": CodeParserService()
}

def get_parser_for(language: str):
    return PARSER_SERVICES.get(language)
