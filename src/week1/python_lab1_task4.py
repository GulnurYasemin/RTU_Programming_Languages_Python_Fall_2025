"""
Task 4 – Text-based Arithmetic Analyzer
--------------------------------------
Create a text-based analyzer that:
1. Counts non-space characters.
2. Counts words.
3. Extracts numbers and computes their sum and average.
Use helper functions:
- count_characters(text)
- count_words(text)
- extract_numbers(text)
- analyze_text(text)
Print formatted summary in main.
"""

import re


def count_characters(text):
    """Count non-space characters in a string."""
    return sum(1 for ch in text if not ch.isspace())


def count_words(text):
    """Count number of words in a string."""
    return len(text.split())


def extract_numbers(text):
    """Return list of integers found in text."""
    # Yakalar: 42, -7, 003 gibi tamsayıları
    matches = re.findall(r"-?\d+", text)
    return [int(m) for m in matches]


def analyze_text(text):
    """Perform text-based arithmetic analysis."""
    char_count = count_characters(text)
    word_count = count_words(text)
    numbers = extract_numbers(text)
    total = sum(numbers) if numbers else 0
    average = (total / len(numbers)) if numbers else None
    # İstenirse tuple döndürelim: (non-space chars, words, numbers, total, average)
    return char_count, word_count, numbers, total, average


if __name__ == "__main__":
    txt = input("Enter text: ")
    chars, words, nums, total, avg = analyze_text(txt)

    print(f"Non-space characters: {chars}")
    print(f"Word count: {words}")
    print(f"Numbers found: {nums if nums else 'None'}")
    print(f"Sum of numbers: {total}")
    print(f"Average of numbers: {avg if avg is not None else 'N/A'}")
