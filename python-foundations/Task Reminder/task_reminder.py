from winotify import Notification
import win32com.client
import pythoncom   
from datetime import datetime
import time
import threading

reminders = []
voice_index = 0  # default voice

def add_reminder():
    user_name = input("Enter your name: ").strip()
    if not user_name:
        print("❌ Name cannot be empty.")
        return

    title = input("Enter reminder title: ").strip()
    if not title:
        print("❌ Title cannot be empty.")
        return

    time_str = input("Enter reminder time (HH:MM, 24hr format, e.g. 14:30): ").strip()
    try:
        reminder_time = datetime.strptime(time_str, "%H:%M").time()
    except ValueError:
        print("❌ Invalid time format. Use HH:MM (24hr).")
        return

    message = input("Enter reminder message (optional): ").strip()
    reminders.append({
        "user": user_name,
        "title": title,
        "time": reminder_time,
        "message": message,
        "voice": voice_index
    })
    print(f"✅ Reminder '{title}' set for {time_str}")

def view_reminders():
    if not reminders:
        print("📭 No reminders scheduled.")
        return
    print("\n📋 Current Reminders:")
    for i, r in enumerate(reminders, 1):
        print(f"{i}) {r['title']} at {r['time'].strftime('%H:%M')} "
              f"(Voice {r['voice']}) - {r['message'] if r['message'] else 'No message'}")

    choice = input("\nDo you want to edit a reminder?\nEnter number or press Enter to skip: ").strip()
    if choice.isdigit():
        idx = int(choice) - 1
        if 0 <= idx < len(reminders):
            edit_reminder(idx)
        else:
            print("❌ Invalid choice.")

def edit_reminder(idx):
    r = reminders[idx]
    print(f"\n✏️ Editing reminder '{r['title']}'")
    new_title = input(f"Enter new title (or press Enter to keep '{r['title']}'): ").strip()
    if new_title:
        r['title'] = new_title

    new_message = input(f"Enter new message (or press Enter to keep current): ").strip()
    if new_message:
        r['message'] = new_message

    new_time = input(f"Enter new time (HH:MM) or press Enter to keep {r['time'].strftime('%H:%M')}: ").strip()
    if new_time:
        try:
            r['time'] = datetime.strptime(new_time, "%H:%M").time()
        except ValueError:
            print("❌ Invalid time format. Keeping old time.")

    print(f"✅ Reminder updated: {r['title']} at {r['time'].strftime('%H:%M')}")

def delete_reminder():
    if not reminders:
        print("📭 No reminders to delete.")
        return
    print("\n🗑️ Reminders:")
    for i, r in enumerate(reminders, 1):
        print(f"{i}) {r['title']} at {r['time'].strftime('%H:%M')}")
    choice = input("Enter the number of the reminder to delete: ").strip()
    if choice.isdigit():
        idx = int(choice) - 1
        if 0 <= idx < len(reminders):
            removed = reminders.pop(idx)
            print(f"❌ Reminder '{removed['title']}' deleted.")
        else:
            print("❌ Invalid choice.")
    else:
        print("❌ Please enter a valid number.")

def change_voice():
    global voice_index
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    voices = speaker.GetVoices()
    print("\n🎤 Available voices:")
    for i in range(voices.Count):
        print(f"{i}) {voices.Item(i).GetDescription()}")
    choice = input("Choose voice number (default 0): ").strip()
    try:
        choice = int(choice)
    except ValueError:
        choice = 0
    if 0 <= choice < voices.Count:
        voice_index = choice
        print(f"✅ Voice changed to {voices.Item(choice).GetDescription()}")
    else:
        print("❌ Invalid choice, using default voice.")

def show_reminder(r):
    # Popup notification
    toast = Notification(
        app_id="RemindMe Ayush",
        title=r['title'],
        msg=r['message'] if r['message'] else r['title']
    )
    toast.show()

    # Voice reads popup content (COM init required in thread)
    pythoncom.CoInitialize()
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    voices = speaker.GetVoices()
    if 0 <= r['voice'] < voices.Count:
        speaker.Voice = voices.Item(r['voice'])

    msg = r['message'] if r['message'] else r['title']
    speaker.Speak(f"Hello {r['user']}, it’s {r['time'].strftime('%H:%M')}, your reminder is: {msg}")
    pythoncom.CoUninitialize()

def run_scheduler():
    while True:
        if reminders:
            now = datetime.now()
            due = [r for r in reminders if now.hour == r['time'].hour and now.minute == r['time'].minute]
            for r in due:
                show_reminder(r)
                reminders.remove(r)
        time.sleep(1)

def show_menu():
    print("\n" + "═" * 40)
    print("📌  Reminder Menu".center(40))
    print("═" * 40)
    print("1)  Add reminder ➕")
    print("2)  View reminders 👀")
    print("3)  Delete reminder ❌")
    print("4)  Change voice 🎤")
    print("5)  Exit 🚪")
    print("═" * 40)
    choice = input("👉 Choose an option: ").strip()
    return choice

def main():
    # Start scheduler in background thread
    threading.Thread(target=run_scheduler, daemon=True).start()

    while True:
        choice = show_menu()
        if choice == "1":
            add_reminder()
        elif choice == "2":
            view_reminders()
        elif choice == "3":
            delete_reminder()
        elif choice == "4":
            change_voice()
        elif choice == "5":
            print("👋 Exiting Reminder App.")
            break
        else:
            print("❌ Invalid choice. Please select 1–5.")

if __name__ == "__main__":
    main()
