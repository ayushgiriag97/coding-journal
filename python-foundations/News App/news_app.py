import os
import sys
import json
import requests
from datetime import datetime

# ==========================================
# CONFIGURATION & GLOBAL CONSTANTS
# ==========================================
API_KEY = "2f5293092b0e4e888edf2b9a84049950"
BASE_URL = "https://newsapi.org/v2"

# Dynamic File Paths
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SAVED_ARTICLES_FILE = os.path.join(SCRIPT_DIR, "saved_news.json")
EXPORT_TXT_FILE = os.path.join(SCRIPT_DIR, "exported_news.txt")

# Allowed NewsAPI Top-Headline Categories and Valid Countries
VALID_CATEGORIES = ("business", "entertainment", "general", "health", "science", "sports", "technology")
VALID_COUNTRIES = ("us", "gb", "in", "ca", "au", "de", "fr")

# Global Text-to-Speech Queue
speech_queue = []


# ==========================================
# REUSABLE HELPERS & INPUT VALIDATION
# ==========================================
def get_user_choice_in_range(prompt, min_val, max_val):
    """Safely prompts the user for an integer within [min_val, max_val].

    Args:
        prompt (str): Text prompt displayed to the user.
        min_val (int): Minimum acceptable integer value.
        max_val (int): Maximum acceptable integer value.

    Returns:
        int | None: Validated choice integer, or None if validation fails.
    """
    user_input = input(prompt).strip()
    if not user_input:
        print("❌ Input cannot be empty.")
        return None

    try:
        choice = int(user_input)
        if min_val <= choice <= max_val:
            return choice
        print(f"❌ Selection out of range. Choose between {min_val} and {max_val}.")
    except ValueError:
        print("❌ Invalid input. Please enter a valid number.")
    return None


def get_valid_date_obj(prompt):
    """Prompts the user for a date string and validates format against YYYY-MM-DD.

    Args:
        prompt (str): Text prompt displayed to the user.

    Returns:
        datetime | None: Validated datetime object, or None if invalid.
    """
    user_input = input(prompt).strip()
    if not user_input:
        print("❌ Date cannot be empty.")
        return None
    try:
        return datetime.strptime(user_input, "%Y-%m-%d")
    except ValueError:
        print("❌ Invalid date format. Please strictly use YYYY-MM-DD (e.g., 2026-09-10).")
        return None


def format_published_date(raw_date_str):
    """Parses ISO-formatted date string into human-readable string.

    Args:
        raw_date_str (str): Raw timestamp from NewsAPI (e.g., '2026-09-10T14:30:00Z').

    Returns:
        str: Formatted timestamp 'YYYY-MM-DD HH:MM UTC', or raw string if parsing fails.
    """
    if not raw_date_str or raw_date_str == "N/A":
        return "N/A"
    try:
        cleaned_str = raw_date_str.replace("Z", "")
        dt = datetime.fromisoformat(cleaned_str)
        return dt.strftime("%Y-%m-%d %H:%M UTC")
    except (ValueError, TypeError):
        return raw_date_str


def get_country_code():
    """Prompts user to select a country code or default to US.

    Returns:
        str: Validated 2-letter country code string.
    """
    print(f"Available Countries: {', '.join(VALID_COUNTRIES)}")
    user_input = input("Enter 2-letter country code (Press Enter for 'us'): ").strip().lower()
    if not user_input:
        return "us"
    if user_input in VALID_COUNTRIES:
        return user_input
    print("⚠️ Invalid country code. Defaulting to 'us'.")
    return "us"


def fetch_news_from_api(endpoint, params):
    """Centralized API fetch helper with response validation, status checks, and exceptions.

    Args:
        endpoint (str): NewsAPI endpoint target (e.g., 'top-headlines', 'everything').
        params (dict): Dictionary of query parameters.

    Returns:
        list: List of article dictionaries returned by NewsAPI, or empty list on failure.
    """
    url = f"{BASE_URL}/{endpoint}"
    params["apiKey"] = API_KEY
    
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        if not isinstance(data, dict):
            print("❌ Malformed payload received from NewsAPI.")
            return []

        if data.get("status") == "error":
            print(f"❌ API Error: {data.get('message', 'Unknown error occurred.')}")
            return []
            
        articles = data.get("articles")
        if not isinstance(articles, list):
            print("❌ Malformed 'articles' array received from API.")
            return []

        return articles
    except requests.exceptions.RequestException as e:
        print(f"❌ Network or Connection Error: {e}")
        return []


def print_article_list(articles):
    """Prints a formatted numbered list of articles on the CLI.

    Args:
        articles (list): List of article dictionaries to print.
    """
    if not articles:
        print("No articles to display.")
        return

    for idx, article in enumerate(articles, start=1):
        title = article.get('title', 'No Title')
        source = article.get('source', {}).get('name', 'Unknown Source')
        raw_date = article.get('publishedAt', 'N/A')
        formatted_date = format_published_date(raw_date)
        print(f"[{idx}] {title}\n    Source: {source} | Published: {formatted_date}\n")


# ==========================================
# NEWS FETCHING FUNCTIONS
# ==========================================
def today_top_headlines():
    """Fetches top breaking news headlines filtered by country choice."""
    print("\n" + "=" * 50)
    print("           TODAY'S TOP HEADLINES 🌐")
    print("=" * 50)
    
    country = get_country_code()
    articles = fetch_news_from_api("top-headlines", {"country": country, "pageSize": 3})
    
    if not articles:
        print("No headlines retrieved.")
        return []

    print_article_list(articles)
    return articles


def browse_by_category():
    """Normalizes, validates category selection, and fetches top category headlines."""
    print("\n" + "=" * 50)
    print("             BROWSE BY CATEGORY 🏷️")
    print("=" * 50)
    print(f"Available Categories: {', '.join(VALID_CATEGORIES)}")
    
    user_input = input("\nEnter category: ").strip().lower()
    
    if user_input not in VALID_CATEGORIES:
        print(f"❌ '{user_input}' is not a valid category.")
        return []

    country = get_country_code()
    articles = fetch_news_from_api("top-headlines", {"category": user_input, "country": country, "pageSize": 5})
    
    if not articles:
        print(f"No articles found for category '{user_input}'.")
        return []

    print(f"\nFound {len(articles)} articles under '{user_input}':\n")
    print_article_list(articles)
    return articles


def search_by_date_time():
    """Queries everything endpoint filtered by keyword and date bounds with range validation."""
    print("\n" + "=" * 50)
    print("         SEARCH BY DATE / TIMEFRAME 📅")
    print("=" * 50)
    query = input("Enter search keyword (e.g., AI, Crypto, Election): ").strip()
    if not query:
        print("❌ Search keyword cannot be empty.")
        return []

    print("\n--- Enter Date Range ---")
    from_dt = get_valid_date_obj("Enter start date (YYYY-MM-DD): ")
    if not from_dt:
        return []

    to_dt = get_valid_date_obj("Enter end date (YYYY-MM-DD): ")
    if not to_dt:
        return []

    if from_dt > to_dt:
        print("❌ Start date cannot be later than end date.")
        return []

    from_str = from_dt.strftime("%Y-%m-%d")
    to_str = to_dt.strftime("%Y-%m-%d")

    params = {
        "q": query,
        "from": from_str,
        "to": to_str,
        "sortBy": "publishedAt",
        "pageSize": 5
    }
    
    articles = fetch_news_from_api("everything", params)
    
    if not articles:
        print("No articles found matching criteria.")
        return []

    print(f"\nFound {len(articles)} articles from {from_str} to {to_str}:\n")
    print_article_list(articles)
    return articles


def search_by_source():
    """Queries top-headlines endpoint using user-provided news publisher identifier."""
    print("\n" + "=" * 50)
    print("           SEARCH BY PUBLISHER / SOURCE 📰")
    print("=" * 50)
    source_id = input("Enter news source identifier (e.g., bbc-news, cnn, techcrunch): ").strip().lower()
    
    if not source_id:
        print("❌ Source identifier cannot be empty.")
        return []

    articles = fetch_news_from_api("top-headlines", {"sources": source_id, "pageSize": 5})
    
    if not articles:
        print(f"No articles retrieved for source '{source_id}'.")
        return []

    print(f"\nFound {len(articles)} articles from source '{source_id}':\n")
    print_article_list(articles)
    return articles


# ==========================================
# LOCAL STORAGE & EXPORT FUNCTIONS
# ==========================================
def load_saved_articles_from_file():
    """Reads articles from local JSON storage safely, resetting corrupted files if necessary."""
    if not os.path.exists(SAVED_ARTICLES_FILE):
        return []
    try:
        with open(SAVED_ARTICLES_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            print("⚠️ Storage format invalid. Resetting saved articles file...")
    except (json.JSONDecodeError, OSError) as e:
        print(f"⚠️ Corrupted saved file detected ({e}). Resetting storage file...")

    # Recover corrupted storage safely
    try:
        with open(SAVED_ARTICLES_FILE, "w", encoding="utf-8") as f:
            json.dump([], f)
    except OSError as e:
        print(f"❌ Failed to reset storage file: {e}")
    return []


def save_article(article):
    """Appends an article dictionary to local JSON storage, avoiding duplicate URL entries."""
    saved = load_saved_articles_from_file()
    
    if any(item.get("url") == article.get("url") for item in saved):
        print("ℹ️ Article is already saved in bookmarks.")
        return

    saved.append(article)
    try:
        with open(SAVED_ARTICLES_FILE, "w", encoding="utf-8") as f:
            json.dump(saved, f, indent=4)
        print("✓ Article saved to JSON storage successfully!")
    except OSError as e:
        print(f"❌ Failed to save article to file: {e}")


def delete_article(article_index):
    """Deletes an article from local JSON storage using its index."""
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


def export_article_to_txt(article):
    """Exports a single article summary to an external formatted text file."""
    try:
        with open(EXPORT_TXT_FILE, "a", encoding="utf-8") as f:
            f.write("=" * 60 + "\n")
            f.write(f"TITLE: {article.get('title', 'No Title')}\n")
            f.write(f"SOURCE: {article.get('source', {}).get('name', 'Unknown')}\n")
            f.write(f"PUBLISHED: {format_published_date(article.get('publishedAt', 'N/A'))}\n")
            f.write(f"URL: {article.get('url', 'N/A')}\n")
            f.write(f"DESCRIPTION: {article.get('description', 'N/A')}\n")
            f.write("=" * 60 + "\n\n")
        print(f"✓ Article exported to '{os.path.basename(EXPORT_TXT_FILE)}'!")
    except OSError as e:
        print(f"❌ Export failed: {e}")


def saved_articles():
    """Saved articles menu interface supporting deletion, playback, and export."""
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
        print("3. 📄 Export a Saved Article to Text File")
        print("4. 🔙 Back to Main Menu")
        print("-" * 50)
        
        choice = input("Enter choice (1-4): ").strip()
        
        if choice in ("1", "2", "3"):
            selected_num = get_user_choice_in_range("Enter article number: ", 1, len(saved))
            if selected_num is not None:
                selected_article = saved[selected_num - 1]
                if choice == "1":
                    delete_article(selected_num - 1)
                elif choice == "2":
                    add_to_speech_queue(selected_article)
                    play_speech_queue()
                elif choice == "3":
                    export_article_to_txt(selected_article)
        elif choice == "4":
            break
        else:
            print("❌ Invalid choice. Try again.")


# ==========================================
# TEXT-TO-SPEECH QUEUE ENGINE
# ==========================================
def add_to_speech_queue(article):
    """Appends an article to the global TTS queue."""
    speech_queue.append(article)
    print(f"✓ Queued for reading: '{article.get('title')}'")


def play_speech_queue():
    """Processes queued articles sequentially via SAPI.SpVoice with Windows OS check."""
    if not speech_queue:
        print("The speech queue is empty!")
        return

    if sys.platform != "win32":
        print("⚠️ Text-to-Speech is only supported on Windows OS (win32com dependency).")
        speech_queue.clear()
        return

    try:
        import win32com.client
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
    """Sub-menu enabling users to perform queue, save, or export actions on listed articles."""
    if not articles:
        return

    while True:
        print("\n" + "-" * 50)
        print("[ ACTIONS ]")
        print("1. 🔊 Queue Article to Read Aloud & Play")
        print("2. 💾 Save an Article")
        print("3. 📄 Export an Article to Text File")
        print("4. 🔙 Back to Main Menu")
        print("-" * 50)
        
        choice = input("Enter choice (1-4): ").strip()
        
        if choice in ("1", "2", "3"):
            selected_num = get_user_choice_in_range("Which article number? ", 1, len(articles))
            if selected_num is not None:
                selected_article = articles[selected_num - 1]
                if choice == "1":
                    add_to_speech_queue(selected_article)
                    play_speech_queue()
                elif choice == "2":
                    save_article(selected_article)
                elif choice == "3":
                    export_article_to_txt(selected_article)
        elif choice == "4":
            break
        else:
            print("❌ Invalid option. Enter 1-4.")


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
        print("4. 📰 Search by Publisher / Source")
        print("5. 🔖 View Saved Articles")
        print("6. ❌ Exit")
        print("-" * 50)

        choice = input("Enter choice (1-6): ").strip()

        if choice == "1":
            handle_article_actions(today_top_headlines())
        elif choice == "2":
            handle_article_actions(browse_by_category())
        elif choice == "3":
            handle_article_actions(search_by_date_time())
        elif choice == "4":
            handle_article_actions(search_by_source())
        elif choice == "5":
            saved_articles()
        elif choice == "6":
            print("\nThank you for using Ayush News House! Goodbye. 👋")
            break
        else:
            print("❌ Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()
