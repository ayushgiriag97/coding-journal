import win32com.client

# Initialize the speech engine
speaker = win32com.client.Dispatch("SAPI.SpVoice")

def print_names(names):
    """Display the current list of names."""
    print("\nList of names for shoutout:\n")
    if not names:
        print("No names in the list.")
    else:
        for i, name in enumerate(names, start=1):
            print(f"{i}. {name}")

def add_names(names):
    """Add one or more names to the list."""
    new_names = input("Enter names to add (separate with commas): ")
    for n in new_names.split(","):
        n = n.strip()
        if n:  # validation: ignore empty entries
            names.append(n)
            print(f"{n} added to the list.")
    return names

def remove_names(names):
    """Remove one or more names from the list."""
    if not names:
        print("List is empty. Nothing to remove.")
        return names
    remove_names = input("Enter names to remove (separate with commas): ")
    for n in remove_names.split(","):
        n = n.strip()
        if n in names:
            names.remove(n)
            print(f"{n} removed from the list.")
        else:
            print(f"{n} not found in the list.")
    return names

def clear_names():
    """Clear the entire list."""
    print("All names cleared from the list.")
    return []

def shoutout(names):
    """Speak out the shoutouts."""
    if not names:
        print("No names in the list. Nothing to shoutout.")
        return
    for i, name in enumerate(names, start=1):
        message = f"Shoutout to {name}!"
        print(message)
        try:
            speaker.Speak(message)
        except Exception as e:
            print(f"Error speaking message: {e}")

def menu():
    """Main menu loop."""
    names = ["Ayush", "Ronaldo", "Messi"]
    while True:
        print_names(names)
        print("\nWhat would you like to do?\n")
        print("1) Add names")
        print("2) Remove names")
        print("3) Clear all names")
        print("4) Proceed to give shoutout")

        choice = input("Enter your choice (1/2/3/4): ").strip()

        if choice == "1":
            names = add_names(names)
        elif choice == "2":
            names = remove_names(names)
        elif choice == "3":
            names = clear_names()
        elif choice == "4":
            print("Proceeding with shoutouts...")
            shoutout(names)
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
