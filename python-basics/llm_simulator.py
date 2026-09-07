responses = {
    "hello": "How i can help you?",
    "python": "Python is a programming language",
    "ai": "AI stands for Artificial Intelligence"
}

user_input = input("You: ").lower()

print(
    responses.get(
        user_input,
        "I don't know that yet"
    )
)