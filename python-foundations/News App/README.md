# 📰 Ayush News House 

A fun and interactive **Python CLI tool** that fetches the latest news using the **NewsAPI**.
You can browse headlines by country or category, search by date range or publisher, save and export articles, and even listen to them aloud with **Windows Speech API (SAPI)**.
---

## 🚀 Features
- 🌐 View today’s top headlines by country.
- 🏷️ Browse news by category (business, sports, tech, etc.).
- 📅 Search articles by keyword and date range.
- 📰 Search by publisher/source (e.g., BBC, CNN).
- 🔖 Save articles locally in JSON storage.
- 📄 Export saved articles to a text file..
- 🔊 Read articles aloud using Windows SAPI (with OS check).

---

## Install dependency:

### Prerequisites
- Windows OS (uses **SAPI.SpVoice**).
- Python 3.x installed.
- A valid NewsAPI key (replace the placeholder in API_KEY)
- `pywin32` package installed:
  ```bash
  pip install pywin32
  python -m pip install pywin32
  ```
- `request` package installed:
  ```bash
  pip install requests
  python -m pip install requests
  ```

---

## 📂 File Persistence
The program automatically creates and uses a file named:
```bash
saved_news.json
exported_news.txt
```
This file is stored in the same folder as the script.
Use the menu options to save or load your shoutout list.

---

## 🖥️ Menu Options
When you run the program, you’ll see:
```bash
📋 Menu Menu:

 1) 🌐 Today's Top Headlines
 2) 🏷️ Browse by Category
 3) 📅 Search by Date / Timeframe
 4) 📰 Search by Publisher / Source
 5) 🔖 View Saved Articles
 6) ❌ Exit
```

---

## 🎯 Example Usage
```bash
 Current Headlines

 1. AI Revolution in Healthcare
    Source: TechCrunch | Published: 2026-09-10 14:30 UTC
 2. Global Markets Rally
    Source: Bloomberg | Published: 2026-09-10 13:15 UTC
------------------------------

👉 Enter your choice (1-6): 5
```

Then when you view saved articles:

```bash
🔖 Saved Articles

 1. AI Revolution in Healthcare
 2. Global Markets Rally

📋 Actions:
 1) 🗑️ Delete a Saved Article
 2) 🔊 Read a Saved Article Aloud
 3) 📄 Export a Saved Article to Text File
 4) 🔙 Back to Main Menu
```
