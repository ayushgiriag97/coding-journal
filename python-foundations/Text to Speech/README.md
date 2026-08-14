# 🎤 Shoutouts to Everyone

A fun and interactive **Python CLI tool** that lets you manage a list of names and give them shoutouts using the **Windows Speech API (SAPI)**.  
You can add/remove names, clear the list, save/load names from a file, and even customize the voice, speed, and volume.

---

## 🚀 Features
- 📋 Manage a shoutout list (add, remove, clear).
- 💾 Save and 📂 load names from a text file (`shoutout_list.txt`).
- 🎚️ Adjust speech rate and 🔊 volume interactively.
- 🎤 Select from installed voices (male/female, accents).
- 📣 Speak out loud each shoutout using Windows SAPI.
- ⚠️ Input validation and error handling for smooth experience.
- 🧹 Clean, user‑friendly CLI with emojis for better readability.

---

## Install dependency:

### Prerequisites
- Windows OS (uses **SAPI.SpVoice**).
- Python 3.x installed.
- `pywin32` package installed:
  ```bash
  pip install pywin32
  python -m pip install pywin32
  ```

---

## 📂 File Persistence
The program automatically creates and uses a file named:
```bash
shoutout_list.txt
```
This file is stored in the same folder as the script.
Use the menu options to save or load your shoutout list.

---

## 🖥️ Menu Options
When you run the program, you’ll see:
```bash
📋 Menu Options:

 1) ➕ Add names
 2) ➖ Remove names
 3) 🧹 Clear all names
 4) 🎚️ Change voice settings
 5) 🎤 Select voice
 6) 💾 Save list
 7) 📂 Load list
 8) 📣 Proceed to give shoutout
```

---

## 🎯 Example Usage
```bash
 Current Shoutout List

 1. Ayush
 2. Ronaldo
 3. Messi
------------------------------

👉 Enter your choice (1-8): 1
➕ Enter names to add (separate with commas):
Harvey, Jon Snow

✅ Harvey added to the list.
✅ Jon Snow added to the list.
```
Then when you proceed:
```bash
📣 Starting shoutouts...

👉 Shoutout to Ayush!
👉 Shoutout to Ronaldo!
👉 Shoutout to Messi!
👉 Shoutout to Harvey!
👉 Shoutout to Jon Snow!

✅ All shoutouts completed!
```
