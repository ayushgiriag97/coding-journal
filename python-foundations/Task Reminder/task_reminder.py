from winotify import Notification
import win32com.client
import time
from datetime import datetime, timedelta

def get_reminders():
    reminders = []
    while True:
        user_name = input("Enter your name: ").strip()
        title = input("Enter notification title: ").strip()
        message = input("Enter notification message (optional): ").strip()
        reminder_time = input("Enter reminder time (HH:MM, 24hr format): ").strip()

        try:
            reminder_time_obj = datetime.strptime(reminder_time, "%H:%M").time()
        except ValueError:
            print("❌ Invalid time format. Example: 14:30")
            continue

        recurrence = input("Repeat? (none/daily/weekly): ").strip().lower()
        reminders.append((user_name, title, message, reminder_time_obj, recurrence))

        more = input("Add another reminder? (y/n): ").strip().lower()
        if more != "y":
            break
    return reminders

def show_reminder(user_name, title, message):
    toast = Notification(app_id="RemindMe Ayush", title=title, msg=message if message else title)
    toast.show()

    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    if message:
        speaker.Speak(f"Hello {user_name}, your reminder is: {message}")
    else:
        speaker.Speak(f"Hello {user_name}, your reminder is: {title}")

def main():
    reminders = get_reminders()
    print("✅ Reminders scheduled.")

    while reminders:
        now = datetime.now()
        for i, (user_name, title, message, reminder_time_obj, recurrence) in enumerate(reminders):
            if now.hour == reminder_time_obj.hour and now.minute == reminder_time_obj.minute:
                show_reminder(user_name, title, message)

                # Snooze option
                snooze = input("Snooze? Enter minutes or press Enter to skip: ").strip()
                if snooze.isdigit():
                    snooze_time = now + timedelta(minutes=int(snooze))
                    reminders[i] = (user_name, title, message, snooze_time.time(), recurrence)
                    print(f"🔔 Snoozed for {snooze} minutes.")
                    continue

                # Handle recurrence
                if recurrence == "daily":
                    next_time = (now + timedelta(days=1)).time()
                    reminders[i] = (user_name, title, message, next_time, recurrence)
                elif recurrence == "weekly":
                    next_time = (now + timedelta(weeks=1)).time()
                    reminders[i] = (user_name, title, message, next_time, recurrence)
                else:
                    reminders.pop(i)  # remove one-time reminder
                break

        time.sleep(30)

if __name__ == "__main__":
    main()
