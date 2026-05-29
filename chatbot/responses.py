import random

RESPONSES = {
    "greetings": [
        "Hello! How can I help you today?",
        "Hi there! I’m ready to assist you.",
        "Hey! What would you like to discuss?"
    ],
    "farewell": [
        "Goodbye! Best of luck with your internship journey.",
        "See you later! Keep practicing your skills.",
        "Bye! Keep building projects and learning."
    ],
    "weather": [
        "I don’t have live weather data, but you can check your local forecast app.",
        "I can’t fetch weather updates right now, but I recommend checking a weather website.",
        "Weather is always changing—your local weather service will have the latest."
    ],
    "time": [
        "It’s always a good time to learn something new!",
        "Let me check the clock for you."
    ],
    "name": [
        "I’m a rule-based chatbot made to help with simple questions and internship guidance.",
        "I’m a chatbot prototype designed for a beginner AI project."
    ],
    "internship": [
        "To prepare for internships, build small projects, study algorithms, and practice coding problems.",
        "Keep your resume clear, include project links, and practice explaining your work.",
        "Internship success comes from hands-on practice, good communication, and persistence."
    ],
    "resume": [
        "A strong resume is clean, specific, and shows your best projects and skills.",
        "List technical tools, project results, and links to your code or portfolio."
    ],
    "interview": [
        "Practice common technical interview questions and explain your solutions clearly.",
        "Do mock interviews, review algorithms, and ask questions during the interview."
    ],
    "learning": [
        "Build a learning plan with short goals and practice coding every day.",
        "Use online tutorials, projects, and coding challenges to improve quickly."
    ],
    "teamwork": [
        "Good teamwork means communicating clearly and helping your teammates succeed.",
        "Show that you can collaborate well and contribute ideas in group projects."
    ],
    "motivation": [
        "Keep going! Learning takes time, and every small project helps you improve.",
        "Stay patient and focus on growth, not perfection. You are on the right path."
    ],
    "jokes": [
        "Why did the developer go broke? Because he used up all his cache!",
        "Why do programmers hate nature? Too many bugs.",
        "Why did the computer show up at work late? It had a hard drive!"
    ],
    "thanks": [
        "You’re welcome! I’m happy to help.",
        "Anytime! Keep asking questions.",
        "Glad I could help."
    ],
    "skills": [
        "Good internship skills include problem solving, working in teams, and communicating your ideas clearly.",
        "Practice Python, build projects, and learn how to explain your code."
    ],
    "project": [
        "A strong project shows what you built, the technology you used, and what you learned.",
        "Include a few small projects on GitHub and describe them clearly in your resume."
    ],
    "default": [
        "I’m not sure I understand. Can you ask in a different way?",
        "Sorry, I don’t know that yet. Try another question.",
        "Try asking about internships, time, weather, or project advice."
    ]
}

def random_response(category: str) -> str:
    return random.choice(RESPONSES.get(category, RESPONSES["default"]))
