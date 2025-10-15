# Install this once (uncomment the next line if running locally)
# pip install better-profanity

from better_profanity import profanity

# Initialize the profanity filter
profanity.load_censor_words()

def check_vulgarity(text):
    """
    Checks if the given text contains vulgar or offensive words.
    Returns True if vulgar, False otherwise.
    Also returns the censored version of the text.
    """
    censored_text = profanity.censor(text)
    contains_profanity = profanity.contains_profanity(text)

    return contains_profanity, censored_text

# Example usage
if __name__ == "__main__":
    user_input = input("Enter a sentence: ")
    is_vulgar, cleaned_text = check_vulgarity(user_input)

    if is_vulgar:
        print("⚠️ Vulgarity detected!")
        print("Censored version:", cleaned_text)
    else:
        print("✅ No vulgarity detected.")
