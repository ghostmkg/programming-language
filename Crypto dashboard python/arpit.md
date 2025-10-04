def traffic_light():
    print("Traffic Light System")
    print("Enter 'red', 'yellow', or 'green' to simulate the light.")
    print("Type 'exit' to stop.\n")

    while True:
        color = input("Enter light color: ").strip().lower()

        if color == "red":
            print("🟥 RED - Stop!\n")
        elif color == "yellow":
            print("🟨 YELLOW - Get Ready!\n")
        elif color == "green":
            print("🟩 GREEN - Go!\n")
        elif color == "exit":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("❌ Invalid input. Try again.\n")


