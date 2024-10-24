import requests

def get_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)
    data = response.json()
    return f"{data['setup']} - {data['punchline']}"

def main():
    while True:
        choice = input("Do you want to hear a joke? (yes/no): ").lower()
        if choice == "yes":
            print(get_joke())
        elif choice == "no":
            print("Goodbye!")
            break
        else:
            print("Please enter yes or no.")

if __name__ == "__main__":
    main()
