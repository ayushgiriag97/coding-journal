# ⏰ Task Reminder

A simple and interactive **Python CLI tool** that helps you schedule reminders with **Windows notifications and Voice Alerts (SAPI)**.  
You can add, view, edit, and delete reminders, customize the voice, and get instant popup + spoken notifications.

---

## 🚀 Features
- ➕ Add reminders with title, time, and optional message.
- 👀 View and ✏️ edit existing reminders.
- ❌ Delete reminders easily by number.
- 🎤 Select from installed voices (male/female, accents).
- 🔔 Instant Windows notification popup + voice readout using Windows SAPI.
- ⚠️ Input validation and error handling for smooth experience.
- 🧹 Clean, user‑friendly CLI with emojis for better readability.

---

## Install dependency:

### Prerequisites
- Windows OS (uses **SAPI.SpVoice** and **Winotify**).
- Python 3.x installed.
- `pywin32` and `winotify` package installed:
  ```bash
  pip install pywin32 winotify
  python -m pip install pywin32 winotify
  ```

---

## 🖥️ Menu Options
When you run the program, you’ll see:
```bash
════════════════════════════════════════
           📌  Reminder Menu            
════════════════════════════════════════
1️⃣ ➕  Add reminder
2️⃣ 👀  View reminders
3️⃣ ❌  Delete reminder
4️⃣ 🎤  Change voice
5️⃣ 🚪  Exit
════════════════════════════════════════
👉 Choose an option: 
```

---

## 🎯 Example Usage
```bash
👉 Choose an option: 1
Enter your name: Ayush
Enter reminder title: Meeting
Enter reminder time (HH:MM, 24hr format, e.g. 14:30): 14:30
Enter reminder message (optional): Project discussion

✅ Reminder 'Meeting' set for 14:30
```
Then when you proceed:
```bash
Hello Ayush, it’s 14:30, your reminder is: Project discussion
```
