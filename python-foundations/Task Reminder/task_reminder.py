#imports
from winotify import Notification
import win32com.client
import time
from datetime import datetime

#helper function
def get_user_input():
    try:
        user_name = input("Enter your name: ").strip()
        if not user_name:
            raise ValueError("Name cannot be empty.")

        title = input("Enter notification title: ").strip()
        if not title:
            raise ValueError("Title cannot be empty.")

        message = input("Enter notification message (optional): ").strip()
        # message can be empty, so no error here

        reminder_time = input("Enter reminder time (HH:MM, 24hr format): ").strip()
        reminder_time_obj = datetime.strptime(reminder_time, "%H:%M").time()

        return user_name, title, message, reminder_time_obj
    except ValueError as e:
        print(f"❌ Error: {e}")
        exit()

#main execution block
def main():
    user_name, title, message, reminder_time_obj = get_user_input()
    print(f"✅ Reminder set for {reminder_time_obj.strftime('%H:%M')}")

    try:
        while True:
            now = datetime.now().time()

            # Allow user to cancel
            cancel = input("Type 'cancel' to stop reminder or press Enter to continue: ").strip().lower()
            if cancel == "cancel":
                print("❌ Reminder cancelled by user.")
                break

            if now.hour == reminder_time_obj.hour and now.minute == reminder_time_obj.minute:
                # Show notification
                toast = Notification(
                    app_id="RemindMe Ayush",
                    title=title,
                    msg=message if message else "No message provided"
                )
                toast.show()

                # Speak reminder
                speaker = win32com.client.Dispatch("SAPI.SpVoice")
                if message:
                    speaker.Speak(f"Hello {user_name}, your reminder is: {message}")
                else:
                    speaker.Speak(f"Hello {user_name}, your reminder is: {title}")
                break

            time.sleep(30)  # check every 30 seconds
    except KeyboardInterrupt:
        print("\n❌ Reminder cancelled (Ctrl+C).")

if __name__ == "__main__":
    main()
