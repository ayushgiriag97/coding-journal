from winotify import Notification
import win32com.client
import time
from datetime import datetime, timedelta

reminders = []

def add_reminder():
    user_name = input("Enter your name: ").strip()
    if not user_name:
        print("❌ Name cannot be empty.")
        return

    title = input("Enter notification title: ").strip()
    if not title:
        print("❌ Title cannot be empty.")
        return

    message = input("Enter notification message (optional): ").strip()

    reminder_time = input("Enter reminder time (HH:MM, 24hr format). Example: 14:30 for 2:30 PM: ").strip()
    try:
        reminder_time_obj = datetime.strptime(reminder_time, "%H:%M").time()
    except ValueError:
        print("❌ Invalid time format. Please use HH:MM (24hr). Example: 14:30")
        return

    recurrence = input("Repeat? (none/daily/weekly): ").strip().lower()
    # Prevent duplicate reminders
    for r in reminders:
        if r[1] == title and r[3] == reminder_time_obj:
            print("⚠️ Duplicate reminder detected. Skipping.")
            return

    reminders.append((user_name, title, message, reminder_time_obj, recurrence))
    print(f"✅ Reminder '{title}' set for {reminder_time_obj.strftime('%H:%M')}")

def view_reminders():
    if not reminders:
        print("📭 No reminders scheduled.")
        return
    print("\n📋 Current Reminders:")
    for i, (user_name, title, message, reminder_time_obj, recurrence) in enumerate(reminders, 1):
        print(f"{i}) {title} at {reminder_time_obj.strftime('%H:%M')} ({recurrence})")

def cancel_reminder():
    view_reminders()
    if not reminders:
        return
    choice = input("Enter the number of the reminder to cancel: ").strip()
    if choice.isdigit():
        idx = int(choice) - 1
        if 0 <= idx < len(reminders):
            removed = reminders.pop(idx)
            print(f"❌ Reminder '{removed[1]}' cancelled.")
        else:
            print("❌ Invalid choice.")
    else:
        print("❌ Please enter a valid number.")

def show_reminder(user_name, title, message):
    toast = Notification(app_id="RemindMe Ayush", title=title, msg=message if message else title)
    toast.show()

    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    if message:
        speaker.Speak(f"Hello {user_name}, your reminder is: {message}")
    else:
        speaker.Speak(f"Hello {user_name}, your reminder is: {title}")

def run_scheduler():
    while reminders:
        now = datetime.now()
        for i, (user_name, title, message, reminder_time_obj, recurrence) in enumerate(reminders):
            if now.hour == reminder_time_obj.hour and now.minute == reminder_time_obj.minute:
                show_reminder(user_name, title, message)

                snooze = input("Snooze? Enter minutes or press Enter to skip: ").strip()
                if snooze.isdigit():
                    snooze_time = now + timedelta(minutes=int(snooze))
                    reminders[i] = (user_name, title, message, snooze_time.time(), recurrence)
                    print(f"🔔 Snoozed for {snooze} minutes.")
                    continue

                if recurrence == "daily":
                    next_time = (now + timedelta(days=1)).time()
                    reminders[i] = (user_name, title, message, next_time, recurrence)
                elif recurrence == "weekly":
                    next_time = (now + timedelta(weeks=1)).time()
                    reminders[i] = (user_name, title, message, next_time, recurrence)
                else:
                    reminders.pop(i)
                break
        time.sleep(30)

def main():
    while True:
        print("\n📌 Reminder Menu")
        print("1) Add reminder")
        print("2) View reminders")
        print("3) Cancel reminder")
        print("4) Start scheduler")
        print("5) Exit")

        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_reminder()
        elif choice == "2":
            view_reminders()
        elif choice == "3":
            cancel_reminder()
        elif choice == "4":
            run_scheduler()
        elif choice == "5":
            print("👋 Exiting Reminder App.")
            break
        else:
            print("❌ Invalid choice. Please select 1–5.")

if __name__ == "__main__":
    main()
