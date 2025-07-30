Code Parser Service
This project provides a service to parse source code files and extract structured metadata such as classes and functions using Tree-sitter.

🚀 Features
Detects language of the code file

Extracts class and function definitions with line numbers

Supports Python (and can be extended to other languages)

Clean modular structure

Testable via pytest

📁 Folder Structure
<img width="575" height="292" alt="image" src="https://github.com/user-attachments/assets/cac6cf29-f0be-439a-9ec5-aa781f8bdb7f" />

🛠️ Setup Instructions
Follow these steps to run this project on your local machine for the first time.
1️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/Mrunal31-Stark/code-parser-lsp.git

2️⃣ Create and Activate Virtual Environment
Windows:
python -m venv venv
venv\Scripts\activate
Mac/Linux:
python3 -m venv venv
source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

🧪 Running the Parser
From the project root , run:
python tests/test_code_parser_service.py
If successful, it will output structured JSON data about the parsed code.

🧾 Example Output
For examples/sample.py:

<img width="763" height="588" alt="image" src="https://github.com/user-attachments/assets/953edd12-5c7f-4705-80b3-18310e329a72" />

🧰 Troubleshooting
ModuleNotFoundError: Ensure you are in the task/ folder when running tests.

ImportError for tree_sitter_languages:

Make sure all requirements are installed and no typo in import

AttributeError: 'str' object has no attribute 'suffix':

Ensure filePath is passed as pathlib.Path, not str.

📦 Requirements (requirements.txt)
tree_sitter_languages
tree_sitter
pytest
uuid
typing_extensions

🧠 Extendability
You can add new languages to support by updating:

src/interfaces.py (Language enum)

Language detection logic

Tree-sitter grammar loading in code_parser_service.py


👨‍💻 Author
Mrunal Kishor Yewatkar
mrunalyewatkar31@gmail.com

