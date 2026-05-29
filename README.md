# Rule-Based AI Chatbot

A complete internship-ready chatbot project built with Python and Flask.

## Project Overview

This project demonstrates a rule-based chatbot that answers user questions using keyword matching. It includes:

- A command-line chatbot (`rule_based_chatbot.py`)
- A Flask web interface (`web_app.py`)
- Modular code under `chatbot/`
- Test coverage with `test_chatbot.py`
- Project documentation and a portfolio summary

## Features

- Handles greetings, exit commands, and help requests
- Recognizes time, weather, jokes, and internship-related questions
- Provides career and project advice for internship preparation
- Runs as a terminal chatbot or as a browser-based web app
- Supports browser chat history and a clear-chat button in the web UI

## Installation

1. Install Python 3.9+.
2. Open a terminal in this folder.
3. Create a virtual environment (recommended):

```bash
python -m venv venv
```

4. Activate the environment:

- Windows:
  ```bash
  venv\Scripts\activate
  ```

5. Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the CLI Chatbot

```bash
python rule_based_chatbot.py
```

## Running the Web App

```bash
python web_app.py
```

Or on Windows, run the launcher:

```powershell
run_web_app.bat
```

If the web app still cannot find Flask, run it from the virtual environment directly:

```powershell
.\.venv\Scripts\python.exe web_app.py
```

Then open `http://127.0.0.1:5000/` in your browser.

## Running the CLI Chatbot

```bash
python rule_based_chatbot.py
```

Or on Windows, use:

```powershell
run_chatbot.bat
```

## Testing

Run the tests using:

```bash
python -m pytest test_chatbot.py
```

## Example Commands

- `hello`
- `what time is it?`
- `tell me a joke`
- `give me internship advice`
- `what should I put on my resume?`
- `show me project ideas`
- `exit`

## Internship Presentation Tips

- Show how the bot uses keyword rules rather than machine learning.
- Explain the project structure and how you separated logic from presentation.
- Point out the CLI and Flask web interface to demonstrate both backend and frontend skills.
- Describe how you added rules for resume tips, interview advice, project portfolio guidance, and teamwork.
- Mention the test file and documentation as evidence of a professional development workflow.
- Use `portfolio_summary.md` to describe the project clearly in a resume or interview.
