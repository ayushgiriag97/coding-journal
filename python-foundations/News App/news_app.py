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

# Global Text-to-Speech Queue
speech_queue = []


# ==========================================
# NEWS FETCHING FUNCTIONS
# ==========================================
def today_top_headlines():
    """Fetches and displays the top 3 headlines from NewsAPI."""
    url = f"{BASE_URL}/top-headlines"
    params = {
        "country": "us",
        "pageSize": 3,
        "apiKey": API_KEY
    }
    try:
        response = requests.get(url, params=params)
        data = response.json()
        articles = data.get("articles", [])
        
        print("\n" + "=" * 50)
        print("           TODAY'S TOP HEADLINES 🌐")
        print("=" * 50)
        
        if not articles:
            print("No top headlines found.")
            return []

        for idx, article in enumerate(articles, start=1):
            print(f"[{idx}] {article.get('title', 'No Title')}")
            print(f"    Source: {article.get('source', {}).get('name', 'Unknown')}\n")
            
        return articles
    except Exception as e:
        print(f"❌ Error fetching top headlines: {e}")
        return []


def browse_by_category():
    """Prompts the user for a category search term (q) and fetches news."""
    print("\n" + "=" * 50)
    print("             BROWSE BY CATEGORY 🏷️")
    print("=" * 50)
    category = input("Enter a topic or category (e.g., technology, sports, business): ").strip()
    
    if not category:
        print("❌ Category cannot be empty.")
        return []

    url = f"{BASE_URL}/top-headlines"
    params = {
        "q": category,
        "pageSize": 5,
        "apiKey": API_KEY
    }
    
    try:
        response = requests.get(url, params=params)
        data = response.json()
        articles = data.get("articles", [])
        
        if not articles:
            print(f"No articles found for category '{category}'.")
            return []

        print(f"\nFound {len(articles)} articles for '{category}':\n")
        for idx, article in enumerate(articles, start=1):
            print(f"[{idx}] {article.get('title', 'No Title')}")
            print(f"    Source: {article.get('source', {}).get('name', 'Unknown')}\n")
            
        return articles
    except Exception as e:
        print(f"❌ Error fetching category news: {e}")
        return []


def search_by_date_time():
    """Queries everything endpoint filtered by a query and YYYY-MM-DD dates."""
    print("\n" + "=" * 50)
    print("         SEARCH BY DATE / TIMEFRAME 📅")
    print("=" * 50)
    query = input("Enter search keyword (e.g., AI, Crypto, Election): ").strip()
    from_date = input("Enter start date (YYYY-MM-DD): ").strip()
    to_date = input("Enter end date (YYYY-MM-DD): ").strip()

    url = f"{BASE_URL}/everything"
    params = {
        "q": query,
        "from": from_date,
        "to": to_date,
        "sortBy": "publishedAt",
        "pageSize": 5,
        "apiKey": API_KEY
    }
    
    try:
        response = requests.get(url, params=params)
        data = response.json()
        
        if data.get("status") == "error":
            print(f"❌ API Error: {data.get('message')}")
            return []
            
        articles = data.get("articles", [])
        
        if not articles:
            print("No articles found matching that date range.")
            return []

        print(f"\nFound {len(articles)} articles from {from_date} to {to_date}:\n")
        for idx, article in enumerate(articles, start=1):
            print(f"[{idx}] {article.get('title', 'No Title')}")
            print(f"    Published At: {article.get('publishedAt', 'N/A')}\n")
            
        return articles
    except Exception as e:
        print(f"❌ Error searching by date: {e}")
        return []


# ==========================================
# LOCAL STORAGE (JSON) FUNCTIONS
# ==========================================
def load_saved_articles_from_file():
    """Helper function to load articles list from JSON file safely."""
    if not os.path.exists(SAVED_ARTICLES_FILE):
        return []
    try:
        with open(SAVED_ARTICLES_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []


def save_article(article):
    """Saves an article dictionary into saved_news.json."""
    saved = load_saved_articles_from_file()
    
    # Avoid duplicate saves
    for item in saved:
        if item.get("url") == article.get("url"):
            print("ℹ️ Article is already saved.")
            return

    saved.append(article)
    with open(SAVED_ARTICLES_FILE, "w", encoding="utf-8") as f:
        json.dump(saved, f, indent=4)
    print("✓ Article saved successfully!")


def delete_article(article_index):
    """Deletes an article from saved_news.json by 0-based index."""
    saved = load_saved_articles_from_file()
    if 0 <= article_index < len(saved):
        removed = saved.pop(article_index)
        with open(SAVED_ARTICLES_FILE, "w", encoding="utf-8") as f:
            json.dump(saved, f, indent=4)
        print(f"✓ Removed article: '{removed.get('title')}'")
    else:
        print("❌ Invalid article index.")


def saved_articles():
    """Views saved articles and handles article deletion operations."""
    while True:
        saved = load_saved_articles_from_file()
        print("\n" + "=" * 50)
        print("              SAVED ARTICLES 🔖")
        print("=" * 50)
        
        if not saved:
            print("No articles currently saved.")
            input("\nPress Enter to return to Main Menu...")
            break

        for idx, article in enumerate(saved, start=1):
            print(f"[{idx}] {article.get('title')}")

        print("\n" + "-" * 50)
        print("[ SAVED ARTICLES ACTIONS ]")
        print("1. 🗑️ Delete a Saved Article")
        print("2. 🔊 Read a Saved Article Aloud")
        print("3. 🔙 Back to Main Menu")
        print("-" * 50)
        
        choice = input("Enter choice (1-3): ").strip()
        
        if choice == "1":
            try:
                item_num = int(input(f"Enter article number to delete (1-{len(saved)}): "))
                delete_article(item_num - 1)
            except ValueError:
                print("❌ Invalid number input.")
        elif choice == "2":
            try:
                item_num = int(input(f"Enter article number to queue for reading (1-{len(saved)}): "))
                if 1 <= item_num <= len(saved):
                    add_to_speech_queue(saved[item_num - 1])
                    play_speech_queue()
                else:
                    print("❌ Invalid article choice.")
            except ValueError:
                print("❌ Invalid number input.")
        elif choice == "3":
            break
        else:
            print("❌ Invalid choice. Try again.")


# ==========================================
# TEXT-TO-SPEECH QUEUE ENGINE
# ==========================================
def add_to_speech_queue(article):
    """Appends an article to the speech lineup."""
    speech_queue.append(article)
    print(f"✓ Queued for reading: '{article.get('title')}'")


def print_current_article(article):
    """Displays the current article details being spoken."""
    print("\n" + "-" * 50)
    print(f"🔊 NOW READING: {article.get('title')}")
    print(f"Source: {article.get('source', {}).get('name', 'Unknown')}")
    print("-" * 50)
    print(f"{article.get('description', 'No description available.')}\n")


def play_speech_queue():
    """Processes all queued articles sequentially via Windows SpVoice."""
    if not speech_queue:
        print("The speech queue is currently empty!")
        return

    try:
        speaker = win32com.client.Dispatch("SAPI.SpVoice")
        print(f"\nStarting playback for {len(speech_queue)} queued article(s)...")
        
        while speech_queue:
            # First-In, First-Out (FIFO) queue processing
            current_article = speech_queue.pop(0)
            print_current_article(current_article)
            
            title = current_article.get('title', '')
            description = current_article.get('description', '')
            text_to_speak = f"{title}. {description}"
            
            speaker.Speak(text_to_speak)
            
        print("✓ Speech queue playback complete!")
    except Exception as e:
        print(f"❌ Text-to-speech error: {e}")


# ==========================================
# INTERACTIVE ACTION SUB-MENU
# ==========================================
def handle_article_actions(articles):
    """Sub-menu allowing users to save or read from current active list."""
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
        
        if choice == "1":
            try:
                num = int(input(f"Which article number to read? (1-{len(articles)}): "))
                if 1 <= num <= len(articles):
                    add_to_speech_queue(articles[num - 1])
                    play_speech_queue()
                else:
                    print("❌ Choice out of range.")
            except ValueError:
                print("❌ Enter a valid integer.")
                
        elif choice == "2":
            try:
                num = int(input(f"Which article number to save? (1-{len(articles)}): "))
                if 1 <= num <= len(articles):
                    save_article(articles[num - 1])
                else:
                    print("❌ Choice out of range.")
            except ValueError:
                print("❌ Enter a valid integer.")
                
        elif choice == "3":
            break
        else:
            print("❌ Invalid option. Enter 1-3.")


# ==========================================
# MAIN ROUTINE & APPLICATION LOOP
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

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            current_articles = today_top_headlines()
            handle_article_actions(current_articles)

        elif choice == "2":
            current_articles = browse_by_category()
            handle_article_actions(current_articles)

        elif choice == "3":
            current_articles = search_by_date_time()
            handle_article_actions(current_articles)

        elif choice == "4":
            saved_articles()

        elif choice == "5":
            print("\nThank you for using Ayush News House! Goodbye. 👋")
            break

        else:
            print("❌ Invalid input. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()