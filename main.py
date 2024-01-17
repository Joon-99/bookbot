"""
Prints a report on the number of words of a text file and its letter distribution.
"""
from collections import Counter

def get_counter(txt):
    """
    Returns a list of tuples with format (letter, letter_count)
    sorted in descending order on letter_count.
    """
    raw_counter = Counter(txt.lower())
    letter_counter =  {char: raw_counter[char] for char in raw_counter if char.isalpha()}
    return sorted(letter_counter.items(), key=lambda x: x[1], reverse=True)

def print_report(filename, nb_words, letter_counter):
    """
    Given a file name, the number of words in that file (space delimited)
    and a list returned by get_counter(), prints a report.
    """
    print(f"--- Begin report of {filename} ---")
    print(f"{nb_words} found in the document")
    print()
    for letter, count in letter_counter:
        print(f"The '{letter}' character was found {count} times")
    print("--- End report ---")

def main():
    """ main """
    filename = "books/frankenstein.txt"
    with open(filename, 'r', encoding='utf8') as f:
        text = f.read()
        print_report(filename, len(text.split()), get_counter(text))

if __name__ == "__main__":
    main()
