# Open Source LLM ChatBot 🩺🤖

## Introduction
Welcome to the LLM using LLA-Ma 2 ChatBot repository! This sophisticated tool is engineered to provide prompt Chat information in response to user queries. Leveraging cutting-edge language models and vector stores, Llama2 Chat Bot stands as a beacon in digital healthcare assistance.

## Table of Contents
- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites
Before diving into the Llama2 Chat Bot, ensure your system is equipped with:
- Python 3.6 or higher
- Necessary Python packages (installable via pip):
  - `langchain`
  - `chainlit`
  - `sentence-transformers`
  - `faiss`
  - `PyPDF2` (for PDF document loading)
  - `huggingface_hub`
  - `ctransformers`
  - `chainlit`

## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/atulX7/ChatBot.git
   cd Chatbot
   ```


2. **Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. **Download Language Models and Data**:
- Refer to the Langchain documentation for instructions on downloading and setting up the language model and vector store from the code file.

5. **Configure Paths and Settings**:
- Set `DB_FAISS_PATH` and other configurations as required for your project.

## Getting Started
To kickstart your journey with the Llama2 Chat Bot:
1. Set up your environment and install packages as outlined in [Installation](#installation).
2. Configure the project (DB_FAISS_PATH and other custom configurations).
3. Prepare the language model and data following the Langchain documentation.

## Usage
Use the Chat Bot to get answers to Chat queries:
1. Train the Chatbot using your custom data:
   a. Place your PDF files in DATA_PATH path.
   b. Run:
   ```bash
   python ingest.py
   ```  
2. To Query the Chatbot, run
   ```bash
   python Chatbot.py -q <query>
   ```
3. To run locally (ChatBot using Chainlit)
   ```bash
   chainlit run chainlit.py -w
   ```  
4. Customize the bot's responses based on specific queries and contexts.

## Contributing
We welcome contributions to the Chat ChatBot! 🌟 Here's how you can contribute:
1. Fork the repository to your account.
2. Create a new branch for your feature or bug fix.
3. Implement your changes and ensure all tests pass.
4. Submit a pull request detailing your changes.
5. After review, your contributions may be merged into the main codebase.

## License
This project is licensed under the [MIT License](License).

For detailed guidance on usage, configuration, and extension, please refer to the Langchain documentation or contact the project maintainers.

🚀 **Happy coding!** 🚀
