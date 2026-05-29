from flask import Flask, request, render_template, session, redirect, url_for
from chatbot import get_response, is_exit_command, get_help_text

app = Flask(__name__)
import os

app.secret_key = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')

# Production configuration
if os.environ.get('FLASK_ENV') == 'production':
    app.config['SESSION_COOKIE_SECURE'] = True
    app.config['SESSION_COOKIE_HTTPONLY'] = True
    app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'


def add_message(role: str, text: str) -> None:
    conversation = session.get("conversation", [])
    conversation.append({"role": role, "text": text})
    session["conversation"] = conversation


@app.route("/", methods=["GET", "POST"])
def home():
    if "conversation" not in session:
        session["conversation"] = [
            {
                "role": "bot",
                "text": "Hello! Ask me about internships, projects, time, weather, or say help."
            }
        ]

    user_text = ""

    if request.method == "POST":
        user_text = request.form.get("user_input", "").strip()
        if user_text:
            add_message("user", user_text)
            bot_reply = get_response(user_text)
            add_message("bot", bot_reply)

    return render_template(
        "index.html",
        user_text=user_text,
        conversation=session["conversation"],
    )


@app.route("/clear", methods=["POST"])
def clear_chat():
    session.pop("conversation", None)
    return redirect(url_for("home"))


@app.route("/help")
def help_page():
    return get_help_text()


if __name__ == "__main__":
    app.run(debug=True)
