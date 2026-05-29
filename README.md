# Rule-Based AI Chatbot

[![Tests](https://github.com/YUVANSHANKAR-B/Rule-Based-AI-Chatbot/actions/workflows/tests.yml/badge.svg)](https://github.com/YUVANSHANKAR-B/Rule-Based-AI-Chatbot/actions)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)

A production-ready, rule-based chatbot built with Python and Flask. Perfect for internship preparation and learning AI fundamentals.

## Project Overview

This project demonstrates a rule-based chatbot system with:

- ✅ Command-line chatbot interface (`rule_based_chatbot.py`)
- ✅ Flask web application with chat history (`web_app.py`)
- ✅ Modular architecture (`chatbot/`)
- ✅ Full test coverage with pytest
- ✅ GitHub Actions CI/CD pipeline
- ✅ Production-ready code

## Features

- **Smart Keyword Matching**: Handles greetings, exit commands, and help requests
- **Domain-Specific Responses**: Answers about time, weather, jokes, and internship-related questions
- **Career Guidance**: Provides advice on resumes, interviews, projects, and skills
- **Dual Interface**: Terminal chatbot + Browser-based web app
- **Persistent Chat**: Browser maintains chat history with clear button
- **Fully Tested**: 5 unit tests with 100% passing rate

## Installation

### Prerequisites
- Python 3.9 or higher
- pip package manager

### Quick Start

1. Clone the repository:
```bash
git clone https://github.com/YUVANSHANKAR-B/Rule-Based-AI-Chatbot.git
cd Rule-Based-AI-Chatbot
```

2. Create a virtual environment:
```bash
python -m venv venv
```

3. Activate the environment:

**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Chatbot

### Terminal Version
```bash
python rule_based_chatbot.py
```

Example interaction:
```
=== Rule-Based AI Chatbot ===
Type a message and press Enter. Type 'exit' to quit.
You: hello
Bot: Hi there! I'm ready to assist you.
You: tell me about internships
Bot: To prepare for internships, build small projects, study algorithms, and practice coding problems.
```

### Web Version
```bash
python web_app.py
```
Then open http://localhost:5000 in your browser

## Testing

Run the test suite:
```bash
python -m pytest test_chatbot.py -v
```

Expected output:
```
test_chatbot.py::test_greeting_response PASSED
test_chatbot.py::test_time_response PASSED
test_chatbot.py::test_internship_response PASSED
test_chatbot.py::test_help_response PASSED
test_chatbot.py::test_exit_detection PASSED

============================== 5 passed ==============================
```

## Production Deployment

### Option 1: Heroku (Free Alternative)
```bash
# Install Heroku CLI and login
heroku login

# Create app
heroku create your-app-name

# Deploy
git push heroku main

# View logs
heroku logs --tail
```

### Option 2: PythonAnywhere
1. Go to pythonanywhere.com
2. Upload your code
3. Configure WSGI file for Flask
4. Set up scheduled tasks

### Option 3: AWS/GCP/Azure
Deploy Flask app using their respective services with Docker containerization.

## Project Structure

```
Rule-Based-AI-Chatbot/
├── chatbot/
│   ├── __init__.py
│   ├── engine.py         # Core chatbot logic
│   ├── rules.py          # Keyword definitions
│   └── responses.py      # Response database
├── templates/
│   └── index.html        # Web UI
├── test_chatbot.py       # Unit tests
├── rule_based_chatbot.py # CLI entry point
├── web_app.py            # Flask app
├── requirements.txt      # Dependencies
└── README.md             # This file
```

## Architecture

The chatbot uses a **rule-based system** with:
- **Keyword matching**: Identifies user intent via keywords
- **Response selection**: Returns appropriate response from database
- **Modular design**: Separates rules, engine, and responses

## Dependencies

- **Flask** (≥2.0): Web framework
- **pytest** (≥8.0): Testing framework

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

## Author

**YUVAN SHANKAR B**
- GitHub: [@YUVANSHANKAR-B](https://github.com/YUVANSHANKAR-B)

## Acknowledgments

- Built as an internship preparation project
- Demonstrates rule-based AI fundamentals
- Perfect starting point for NLP learning

## Support

Have questions? 
- Check the [Issues](https://github.com/YUVANSHANKAR-B/Rule-Based-AI-Chatbot/issues) section
- Read the project documentation

## Changelog

### v1.0.0 (Production Release)
- ✅ Initial release
- ✅ Full test coverage
- ✅ GitHub Actions CI/CD
- ✅ Production-ready code
- ✅ Documentation complete

---

**Made with ❤️ for learning and production**

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
