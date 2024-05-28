from better_profanity import profanity
import requests

# Load custom bad words from online repositories
def load_custom_badwords():
    # URLs to the raw wordlists from GitHub
    wordlist_urls = {
        'en': 'https://raw.githubusercontent.com/chucknorris-io/swear-words/master/en',
        'es': 'https://raw.githubusercontent.com/chucknorris-io/swear-words/master/es',
        'fr': 'https://raw.githubusercontent.com/chucknorris-io/swear-words/master/fr',
        'it': 'https://raw.githubusercontent.com/chucknorris-io/swear-words/master/it',
        'pt': 'https://raw.githubusercontent.com/chucknorris-io/swear-words/master/pt',
        'de': 'https://raw.githubusercontent.com/chucknorris-io/swear-words/master/de',
        'ar-latn': 'https://raw.githubusercontent.com/words/cuss/main/data/ar-latn',
        # Add other languages as needed
    }

    for lang, url in wordlist_urls.items():
        response = requests.get(url)
        if response.status_code == 200:
            custom_badwords = response.text.splitlines()
            profanity.add_censor_words(custom_badwords)

def censor_text(text):
    return profanity.censor(text)

# Initialize profanity filter with custom bad words
load_custom_badwords()
