"""
Assignment 4 – Functions and Error Handling
"""

APP_NAME = "Text Analyzer Pro"


def clean_text(text: str, lowercase: bool = True) -> str:
    """Return cleaned text; optionally lowercase it."""
    if not isinstance(text, str):
        raise TypeError("Text must be provided as a string.")
    if not text.strip():
        raise ValueError("Text cannot be empty.")

    cleaned = " ".join(text.split())
    if lowercase:
        cleaned = cleaned.lower()
    return cleaned


def count_words(text: str) -> int:
    """Return the number of words in text."""
    return len(text.split())


def average_word_length(text: str) -> float:
    """Return the average word length."""
    words = text.split()
    total_letters = sum(len(word.strip(".,!?;:\"'()[]{}")) for word in words)
    return total_letters / len(words)


def count_character(text: str, character: str) -> int:
    """Return how many times one character appears in text."""
    if len(character) != 1:
        raise ValueError("Please enter exactly one character.")
    return text.count(character)


def scope_demo() -> str:
    """Show local and global variable scope."""
    APP_NAME = "Local Scope Demo"
    return f"Inside the function, APP_NAME = {APP_NAME}"


def run_demo() -> None:
    """Run a short interactive demo."""
    print(f"Welcome to {APP_NAME}!")

    try:
        user_text = input("Enter a sentence or paragraph: ")
        cleaned = clean_text(user_text)

        print("\nAnalysis Results")
        print("-" * 20)
        print(f"Cleaned text: {cleaned}")
        print(f"Word count: {count_words(cleaned)}")
        print(f"Average word length: {average_word_length(cleaned):.2f}")

        char_to_count = input("Enter one character to count in the text: ")
        print(f"'{char_to_count}' appears {count_character(cleaned, char_to_count)} times.")

    except ValueError as ve:
        print(f"Input error: {ve}")
    except TypeError as te:
        print(f"Type error: {te}")
    except ZeroDivisionError:
        print("Math error: Cannot calculate an average because there are no words.")

    print("\nScope Demonstration")
    print(scope_demo())
    print(f"Outside the function, APP_NAME = {APP_NAME}")


if __name__ == "__main__":
    sample = clean_text("  Hello   World from Python!  ")
    print("Quick Tests")
    print("-" * 20)
    print(f"Sample cleaned text: {sample}")
    print(f"Sample word count: {count_words(sample)}")
    print(f"Sample average word length: {average_word_length(sample):.2f}")
    print(f"Count of 'o': {count_character(sample, 'o')}")
    print()

    run_demo()
