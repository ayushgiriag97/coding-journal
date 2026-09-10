import os
import json
import requests
import win32com.client

# ==========================================
# CONFIGURATION & GLOBAL CONSTANTS
# ==========================================
API_KEY = "2f5293092b0e4e888edf2b9a84049950"
BASE_URL = "https://newsapi.org/v2"

# Dynamic File Paths
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SAVED_ARTICLES_FILE = os.path.join(SCRIPT_DIR, "saved_news.json")

# Allowed NewsAPI Top-Headline Categories
VALID_CATEGORIES = ("business", "entertainment", "general", "health", "science", "sports", "technology")

# Global Text-to-Speech Queue
speech_queue = []


# ==========================================
# REUSABLE INPUT VALIDATION HELPERS 
# ==========================================
def get_user_choice_in_range(prompt, min_val, max_val):
    """Safely prompts user for an integer within [min_val, max_val]. Returns None if invalid."""
    try:
        choice = int(input(prompt).strip())
        if min_val <= choice <= max_val:
            return choice
        print(f"❌ Selection out of range. Choose between {min_val} and {max_val}.")
    except ValueError:
        print("❌ Invalid input. Please enter a valid number.")
    return None


def fetch_news_from_api(endpoint, params):
    """Centralized API fetch helper handling status checks and exceptions safely."""
    url = f"{BASE_URL}/{endpoint}"
    params["apiKey"] = API_KEY
    
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        if data.get("status") == "error":
            print(f"❌ API Error: {data.get('message', 'Unknown error occurred.')}")
            return []
            
        return data.get("articles", [])
    except requests.exceptions.RequestException as e:
        print(f"❌ Network or Connection Error: {e}")
        return []


def print_article_list(articles):
    """Prints a formatted numbered list of articles."""
    for idx, article in enumerate(articles, start=1):
        title = article.get('title', 'No Title')
        source = article.get('source', {}).get('name', 'Unknown Source')
        print(f"[{idx}] {title}\n    Source: {source}\n")


# ==========================================
# NEWS FETCHING FUNCTIONS
# ==========================================
def today_top_headlines():
    """Fetches and displays top 3 breaking news headlines."""
    print("\n" + "=" * 50)
    print("           TODAY'S TOP HEADLINES 🌐")
    print("=" * 50)
    
    articles = fetch_news_from_api("top-headlines", {"country": "us", "pageSize": 3})
    
    if not articles:
        print("No headlines retrieved.")
        return []

    print_article_list(articles)
    return articles


def browse_by_category():
    """Prompts for category, normalizes case, validates, and fetches articles."""
    print("\n" + "=" * 50)
    print("             BROWSE BY CATEGORY 🏷️")
    print("=" * 50)
    print(f"Available Categories: {', '.join(VALID_CATEGORIES)}")
    
    user_input = input("\nEnter category: ").strip().lower()
    
    if user_input not in VALID_CATEGORIES:
        print(f"❌ '{user_input}' is not a valid category. Choose from the list above.")
        return []

    articles = fetch_news_from_api("top-headlines", {"category": user_input, "country": "us", "pageSize": 5})
    
    if not articles:
        print(f"No articles found for category '{user_input}'.")
        return []

    print(f"\nFound {len(articles)} articles under '{user_input}':\n")
    print_article_list(articles)
    return articles


def search_by_date_time():
    """Queries everything endpoint filtered by a query keyword and YYYY-MM-DD dates."""
    print("\n" + "=" * 50)
    print("         SEARCH BY DATE / TIMEFRAME 📅")
    print("=" * 50)
    query = input("Enter search keyword (e.g., AI, Crypto, Election): ").strip()
    from_date = input("Enter start date (YYYY-MM-DD): ").strip()
    to_date = input("Enter end date (YYYY-MM-DD): ").strip()

    if not query or not from_date or not to_date:
        print("❌ Keyword, start date, and end date are all required.")
        return []

    params = {
        "q": query,
        "from": from_date,
        "to": to_date,
        "sortBy": "publishedAt",
        "pageSize": 5
    }
    
    articles = fetch_news_from_api("everything", params)
    
    if not articles:
        print("No articles found matching criteria.")
        return []

    print(f"\nFound {len(articles)} articles from {from_date} to {to_date}:\n")
    print_article_list(articles)
    return articles


# ==========================================
# LOCAL STORAGE (JSON) FUNCTIONS
# ==========================================
def load_saved_articles_from_file():
    """Reads articles from local JSON storage safely."""
    if not os.path.exists(SAVED_ARTICLES_FILE):
        return []
    try:
        with open(SAVED_ARTICLES_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError) as e:
        print(f"⚠️ Error reading saved file: {e}")
        return []


def save_article(article):
    """Appends an article to JSON storage avoiding duplicates."""
    saved = load_saved_articles_from_file()
    
    if any(item.get("url") == article.get("url") for item in saved):
        print("ℹ️ Article is already saved.")
        return

    saved.append(article)
    try:
        with open(SAVED_ARTICLES_FILE, "w", encoding="utf-8") as f:
            json.dump(saved, f, indent=4)
        print("✓ Article saved successfully!")
    except OSError as e:
        print(f"❌ Failed to save article to file: {e}")


def delete_article(article_index):
    """Deletes an article from storage by index."""
    saved = load_saved_articles_from_file()
    if 0 <= article_index < len(saved):
        removed = saved.pop(article_index)
        try:
            with open(SAVED_ARTICLES_FILE, "w", encoding="utf-8") as f:
                json.dump(saved, f, indent=4)
            print(f"✓ Removed article: '{removed.get('title')}'")
        except OSError as e:
            print(f"❌ Failed to update storage: {e}")
    else:
        print("❌ Invalid article selection.")


def saved_articles():
    """Saved articles menu interface."""
    while True:
        saved = load_saved_articles_from_file()
        print("\n" + "=" * 50)
        print("              SAVED ARTICLES 🔖")
        print("=" * 50)
        
        if not saved:
            print("No articles currently saved.")
            input("\nPress Enter to return to Main Menu...")
            break

        print_article_list(saved)

        print("-" * 50)
        print("[ SAVED ARTICLES ACTIONS ]")
        print("1. 🗑️ Delete a Saved Article")
        print("2. 🔊 Read a Saved Article Aloud")
        print("3. 🔙 Back to Main Menu")
        print("-" * 50)
        
        choice = input("Enter choice (1-3): ").strip()
        
        if choice in ("1", "2"):
            selected_num = get_user_choice_in_range("Enter article number: ", 1, len(saved))
            if selected_num is not None:
                if choice == "1":
                    delete_article(selected_num - 1)
                else:
                    add_to_speech_queue(saved[selected_num - 1])
                    play_speech_queue()
        elif choice == "3":
            break
        else:
            print("❌ Invalid choice. Try again.")


# ==========================================
# TEXT-TO-SPEECH QUEUE ENGINE
# ==========================================
def add_to_speech_queue(article):
    """Appends an article to speech queue."""
    speech_queue.append(article)
    print(f"✓ Queued for reading: '{article.get('title')}'")


def play_speech_queue():
    """Processes queued articles sequentially via Windows SpVoice."""
    if not speech_queue:
        print("The speech queue is empty!")
        return

    try:
        speaker = win32com.client.Dispatch("SAPI.SpVoice")
        print(f"\nPlaying {len(speech_queue)} article(s)...")
        
        while speech_queue:
            article = speech_queue.pop(0)
            title = article.get('title', 'No Title')
            desc = article.get('description', 'No description available.')
            
            print(f"\n🔊 NOW READING: {title}\n{desc}\n")
            speaker.Speak(f"{title}. {desc}")
            
        print("✓ Playback complete!")
    except Exception as e:
        print(f"❌ Text-to-speech error: {e}")


# ==========================================
# INTERACTIVE ACTION SUB-MENU
# ==========================================
def handle_article_actions(articles):
    """Sub-menu allowing users to perform actions on currently listed articles."""
    if not articles:
        return

    while True:
        print("\n" + "-" * 50)
        print("[ ACTIONS ]")
        print("1. 🔊 Queue Article to Read Aloud & Play")
        print("2. 💾 Save an Article")
        print("3. 🔙 Back to Main Menu")
        print("-" * 50)
        
        choice = input("Enter choice (1-3): ").strip()
        
        if choice in ("1", "2"):
            selected_num = get_user_choice_in_range("Which article number? ", 1, len(articles))
            if selected_num is not None:
                if choice == "1":
                    add_to_speech_queue(articles[selected_num - 1])
                    play_speech_queue()
                else:
                    save_article(articles[selected_num - 1])
        elif choice == "3":
            break
        else:
            print("❌ Invalid option. Enter 1-3.")


# ==========================================
# MAIN APPLICATION LOOP
# ==========================================
def main():
    while True:
        print("\n" + "=" * 50)
        print("           Welcome to Ayush News House 📰")
        print("=" * 50)
        print("[ MAIN MENU ]")
        print("1. 🌐 Today's Top Headlines")
        print("2. 🏷️  Browse by Category")
        print("3. 📅  Search by Date / Timeframe")
        print("4. 🔖 View Saved Articles")
        print("5. ❌ Exit")
        print("-" * 50)

        choice = input("Enter choice (1-5): ").strip()

        if choice == "1":
            handle_article_actions(today_top_headlines())
        elif choice == "2":
            handle_article_actions(browse_by_category())
        elif choice == "3":
            handle_article_actions(search_by_date_time())
        elif choice == "4":
            saved_articles()
        elif choice == "5":
            print("\nThank you for using Ayush News House! Goodbye. 👋")
            break
        else:
            print("❌ Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
