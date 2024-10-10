import openai

# Set your OpenAI API key
openai.api_key = "YOUR_API_KEY"

def chat():
    """Main chat function."""

    print("Chatbot: Hello! How can I assist you today?")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break

        response = openai.Completion.create(
            engine="text-davinci-003",  
            prompt=user_input,
            max_tokens=150,
            temperature=0.7,
        )

        print("Chatbot:", response.choices[0].text.strip())

if __name__ == "__main__":
    chat()