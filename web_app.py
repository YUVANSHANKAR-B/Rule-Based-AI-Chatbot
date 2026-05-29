from flask import Flask, request, render_template
from chatbot import get_response, is_exit_command, get_help_text

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    user_text = ""
    bot_reply = "Hello! Ask me about internships, projects, time, weather, or say help."

    if request.method == "POST":
        user_text = request.form.get("user_input", "").strip()
        if user_text:
            bot_reply = get_response(user_text)

    return render_template("index.html", user_text=user_text, bot_reply=bot_reply)


@app.route("/help")
def help_page():
    return get_help_text()


if __name__ == "__main__":
    app.run(debug=True)
