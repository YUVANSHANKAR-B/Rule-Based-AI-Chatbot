import datetime
import re
from .responses import random_response
from .rules import (
    EXIT_KEYWORDS,
    GREETING_KEYWORDS,
    WEATHER_KEYWORDS,
    TIME_KEYWORDS,
    NAME_KEYWORDS,
    INTERNSHIP_KEYWORDS,
    RESUME_KEYWORDS,
    INTERVIEW_KEYWORDS,
    JOKE_KEYWORDS,
    THANKS_KEYWORDS,
    SKILL_KEYWORDS,
    LEARNING_KEYWORDS,
    TEAMWORK_KEYWORDS,
    MOTIVATION_KEYWORDS,
    PROJECT_KEYWORDS,
    HELP_KEYWORDS,
)


def _contains_keyword(user_input: str, keywords: list[str]) -> bool:
    tokens = re.findall(r"\b[\w']+\b", user_input)

    for keyword in keywords:
        if " " in keyword:
            if re.search(rf"\b{re.escape(keyword)}\b", user_input):
                return True
        else:
            if keyword in tokens:
                return True
            if keyword + "s" in tokens:
                return True
            if keyword.endswith("y") and keyword[:-1] + "ies" in tokens:
                return True

    return False


def get_help_text() -> str:
    return (
        "Type a question or command, such as: hello, time, weather, "
        "tell me a joke, internship advice, project tips, or exit."
    )


def is_exit_command(user_input: str) -> bool:
    return _contains_keyword(user_input, EXIT_KEYWORDS)


def _get_time_response() -> str:
    now = datetime.datetime.now()
    return f"The current time is {now.strftime('%I:%M %p on %A, %B %d, %Y')}"


def get_response(user_input: str) -> str:
    normalized = user_input.strip().lower()

    if not normalized:
        return "Please type a message so I can respond."

    if is_exit_command(normalized):
        return random_response("farewell")

    if _contains_keyword(normalized, GREETING_KEYWORDS):
        return random_response("greetings")

    if _contains_keyword(normalized, WEATHER_KEYWORDS):
        return random_response("weather")

    if _contains_keyword(normalized, TIME_KEYWORDS):
        return _get_time_response()

    if _contains_keyword(normalized, NAME_KEYWORDS):
        return random_response("name")

    if _contains_keyword(normalized, INTERNSHIP_KEYWORDS):
        return random_response("internship")

    if _contains_keyword(normalized, RESUME_KEYWORDS):
        return random_response("resume")

    if _contains_keyword(normalized, INTERVIEW_KEYWORDS):
        return random_response("interview")

    if _contains_keyword(normalized, JOKE_KEYWORDS):
        return random_response("jokes")

    if _contains_keyword(normalized, THANKS_KEYWORDS):
        return random_response("thanks")

    if _contains_keyword(normalized, SKILL_KEYWORDS):
        return random_response("skills")

    if _contains_keyword(normalized, LEARNING_KEYWORDS):
        return random_response("learning")

    if _contains_keyword(normalized, TEAMWORK_KEYWORDS):
        return random_response("teamwork")

    if _contains_keyword(normalized, MOTIVATION_KEYWORDS):
        return random_response("motivation")

    if _contains_keyword(normalized, PROJECT_KEYWORDS):
        return random_response("project")

    if _contains_keyword(normalized, HELP_KEYWORDS):
        return get_help_text()

    return random_response("default")
