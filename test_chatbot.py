from chatbot import get_response, is_exit_command


def test_greeting_response():
    response = get_response("hello").lower()
    assert "hello" in response or "hi" in response


def test_time_response():
    response = get_response("what is the time")
    assert "current time" in response.lower()


def test_internship_response():
    response = get_response("tell me about internships")
    normalized = response.lower()
    assert (
        "internship" in normalized
        or "resume" in normalized
        or "project" in normalized
        or "career" in normalized
    )
    assert "what would you like" not in normalized


def test_help_response():
    response = get_response("help")
    assert "type a question" in response.lower()


def test_exit_detection():
    assert is_exit_command("bye") is True
    assert is_exit_command("quit") is True
