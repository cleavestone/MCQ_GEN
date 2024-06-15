🌟 Introduction
This application allows users to generate MCQs from PDF or text files and displays the correct answers in a user-friendly format. It's built using Streamlit for the front end and LangChain for generating the MCQs.

✨ Features
Upload PDF or text files to generate MCQs.
Enumerated choices for easy selection.
Highlight correct answers distinctly.
Smooth and intuitive user interface.

🧠 Technologies and Concepts Learned
Streamlit: Creating interactive web applications.
LangChain: Integrating with LangChain API for generating MCQs.
Python Development Best Practices:
Virtual environments for dependency management.
Project structure and organization.
Exception handling and logging.
Version Control with Git:
Cloning, committing, and pushing changes.
Collaborating using version control.
Documentation:
Writing comprehensive README files.
Commenting code for better understanding and maintenance.
Generative AI: Leveraging AI to create dynamic content and applications.
🗂 Project Structure
plaintext

MCQ_GEN/
├── env/                    # Virtual environment for managing dependencies
├── src/                    # Source code of the project
│   ├── __init__.py         # Makes src a package
│   ├── app.py              # Main application script
│   ├── openai_utils.py     # Utility functions for interacting with OpenAI API
│   ├── text_utils.py       # Utility functions for reading and processing text files
│   └── logger.py           # Logger configuration and setup
├── Response.json           # Sample response JSON file
├── .gitignore              # Specifies files and directories to be ignored by Git
├── requirements.txt        # Lists project dependencies
├── README.md               # Project documentation

🛠️ Setup and Installation
Clone the repository:


git clone https://github.com/yourusername/MCQ_GEN.git
cd MCQ_GEN
Set up a virtual environment:



python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
Install the dependencies:


pip install -r requirements.txt

🚀 Usage
Run the application:


streamlit run src/app.py
Upload a file: Use the file uploader to upload a PDF or text file.

Generate questions: Specify the number of MCQs to generate and click the "Generate Questions" button.

View answers: Questions and their respective correct answers will be displayed in a user-friendly format.