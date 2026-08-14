#imports
import win32com.client
import os

# Initialize the speech engine
speaker = win32com.client.Dispatch("SAPI.SpVoice")

# Get the folder path where this script is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LIST_FILE = os.path.join(BASE_DIR, "shoutout_list.txt")

# Utility functions
def print_names(names):
    """Display the current list of names."""
    print("\n Current Shoutout List \n")
    if not names:
        print("⚠️  The list is empty.")
    else:
        for i, name in enumerate(names, start=1):
            print(f" {i}. {name}")
    print("-" * 30)

def add_names(names):
    """Add one or more names to the list."""
    new_names = input("\n➕ Enter names to add (separate with commas):\n")
    for n in new_names.split(","):
        n = n.strip()
        if n:
            names.append(n)
            print(f"✅ {n} added to the list.")
    return names

def remove_names(names):
    """Remove one or more names from the list."""
    if not names:
        print("⚠️  The list is empty. Nothing to remove.")
        return names
    remove_names = input("\n➖ Enter names to remove (separate with commas):\n")
    for n in remove_names.split(","):
        n = n.strip()
        if n in names:
            names.remove(n)
            print(f"🗑️ {n} removed from the list.")
        else:
            print(f"❌ {n} not found in the list.")
    return names

def clear_names():
    """Clear the entire list."""
    print("🧹 All names cleared from the list.")
    return []

def set_voice_settings():
    """Allow user to set voice speed and volume."""
    try:
        rate = int(input("\n🎚️ Enter speech rate (-10 to +10, default 0): ").strip() or 0)
        volume = int(input("🔊 Enter volume (0 to 100, default 100): ").strip() or 100)
        speaker.Rate = max(-10, min(10, rate))
        speaker.Volume = max(0, min(100, volume))
        print(f"✅ Voice settings updated → Rate={speaker.Rate}, Volume={speaker.Volume}")
    except ValueError:
        print("⚠️ Invalid input. Keeping current voice settings.")

def select_voice():
    """Let user choose from installed voices."""
    voices = speaker.GetVoices()
    print("\n🎤 Available Voices:")
    for i in range(voices.Count):
        print(f" {i}) {voices.Item(i).GetDescription()}")
    try:
        choice = int(input("\nEnter the number of the voice you want: ").strip())
        if 0 <= choice < voices.Count:
            speaker.Voice = voices.Item(choice)
            print(f"✅ Voice changed to: {voices.Item(choice).GetDescription()}")
        else:
            print("⚠️ Invalid choice. Keeping current voice.")
    except ValueError:
        print("⚠️ Invalid input. Keeping current voice.")

def save_list(names):
    """Save names to a file inside the script folder."""
    with open(LIST_FILE, "w", encoding="utf-8") as f:
        for name in names:
            f.write(name + "\n")
    print(f"💾 List saved to {LIST_FILE}")

def load_list():
    """Load names from a file inside the script folder."""
    if os.path.exists(LIST_FILE):
        with open(LIST_FILE, "r", encoding="utf-8") as f:
            names = [line.strip() for line in f if line.strip()]
        print(f"📂 List loaded from {LIST_FILE}")
        return names
    else:
        print("⚠️ No saved list found.")
        return []

def shoutout(names):
    """Speak out the shoutouts."""
    if not names:
        print("⚠️ No names in the list. Nothing to shoutout.")
        return
    print("\n📣 Starting shoutouts...\n")
    for i, name in enumerate(names, start=1):
        message = f"Shoutout to {name}!"
        print(f"👉 {message}")
        try:
            speaker.Speak(message)
        except Exception as e:
            print(f"❌ Error speaking message: {e}")
    print("\n✅ All shoutouts completed!\n")

# Entry point
def menu():
    """Main menu loop."""
    names = load_list() or ["Ayush", "Ronaldo", "Messi"]
    while True:
        print_names(names)
        print("\n📋 Menu Options:\n")
        print(" 1) ➕ Add names")
        print(" 2) ➖ Remove names")
        print(" 3) 🧹 Clear all names")
        print(" 4) 🎚️ Change voice settings")
        print(" 5) 🎤 Select voice")
        print(" 6) 💾 Save list")
        print(" 7) 📂 Load list")
        print(" 8) 📣 Proceed to give shoutout\n")

        choice = input("👉 Enter your choice (1-8): ").strip()

        if choice == "1":
            names = add_names(names)
        elif choice == "2":
            names = remove_names(names)
        elif choice == "3":
            names = clear_names()
        elif choice == "4":
            set_voice_settings()
        elif choice == "5":
            select_voice()
        elif choice == "6":
            save_list(names)
        elif choice == "7":
            names = load_list()
        elif choice == "8":
            shoutout(names)
            break
        else:
            print("⚠️ Invalid choice. Please try again.")

# Main guard
if __name__ == "__main__":
    menu()
