from chatbot import get_response, is_exit_command, get_help_text


def main() -> None:
    print("=== Rule-Based AI Chatbot ===")
    print("Type a message and press Enter. Type 'exit' to quit.")
    print("Need help? Type 'help'.")

    while True:
        user_input = input("You: ").strip()

        if not user_input:
            print("Please type something so I can respond.")
            continue

        if is_exit_command(user_input):
            print(f"Bot: {get_response(user_input)}")
            break

        if user_input.lower() == "help":
            print(f"Bot: {get_help_text()}")
            continue

        response = get_response(user_input)
        print(f"Bot: {response}")


if __name__ == "__main__":
    main()
