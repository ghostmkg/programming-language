def cast_vote(votes, candidates):
    vote = input(f"Enter the name of your candidate {candidates}: ").capitalize()
    if vote in votes:
        votes[vote] += 1
    else:
        print("Invalid candidate. Try again.")

def display_results(votes):
    print("\nVoting Results:")
    for candidate, vote_count in votes.items():
        print(f"{candidate}: {vote_count} votes")

def main():
    votes = {"Alice": 0, "Bob": 0, "Charlie": 0}
    candidates = list(votes.keys())

    while True:
        print("\n1. Cast Vote\n2. Show Results\n3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            cast_vote(votes, candidates)
        elif choice == "2":
            display_results(votes)
        elif choice == "3":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
