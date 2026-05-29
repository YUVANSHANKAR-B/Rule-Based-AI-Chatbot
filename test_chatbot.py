from chatbot import get_response, is_exit_command


def test_greeting_response():
    assert "hello" in get_response("hello").lower() or "hi" in get_response("hello").lower()


def test_time_response():
    response = get_response("what is the time")
    assert "current time" in response.lower()


def test_internship_response():
    response = get_response("tell me about internships")
    assert "internship" in response.lower() or "resume" in response.lower() or "project" in response.lower()


def test_exit_detection():
    assert is_exit_command("bye") is True
    assert is_exit_command("quit") is True
