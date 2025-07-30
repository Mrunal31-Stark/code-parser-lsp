from pathlib import Path
from python_lsp_server import LanguageServer #type:ignore # Base class for Language Server Protocol support 
from src.services.code_parser_service import CodeParserService  # Custom code parser service

# LspServerManager inherits from the base LanguageServer class
class LspServerManager(LanguageServer):
    def __init__(self):
        super().__init__()  # Initialize the parent LanguageServer class
        self.codeParser = CodeParserService()  # Create an instance of the code parser service

    def initialize(self, params):
        """
        Handle the 'initialize' request from the client.

        This function returns the capabilities of the language server. You can extend this
        to declare specific capabilities (like code completion, hover, etc.).
        """
        return {"capabilities": {}}  # Currently, no capabilities are declared

    def initialized(self, params):
        """
        Called when the client has completed the initialization process.

        Used for logging or setting up additional services after initialization.
        """
        print("✅ LSP Initialized")

    def shutdown(self):
        """
        Gracefully shutdown the server when requested by the client.
        """
        print("🛑 Shutting down LSP...")

    def did_open(self, params):
        """
        Triggered when a text document is opened in the editor.

        This method:
        - Extracts the file path from the URI
        - Identifies the programming language of the file using CodeParserService
        - Logs the detected language
        """
        # Convert the URI to a file path by stripping the "file://" prefix
        file_path = Path(params['textDocument']['uri'].replace('file://', ''))

        # Use the code parser to determine the language of the file
        lang = self.codeParser.identifyLanguage(file_path)

        # Output the detected language
        print(f"📂 Opened file: {file_path}")
        print(f"🧠 Detected language: {lang}")
