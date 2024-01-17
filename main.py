from collections import Counter

def get_counter(str):
    raw_counter = Counter(str.lower())
    letter_counter =  {char: raw_counter[char] for char in raw_counter if char.isalpha()}
    return sorted(letter_counter.items(), key=lambda x: x[1], reverse=True)

def print_report(filename, nb_words, letter_counter):
    print(f"--- Begin report of {filename} ---")
    print(f"{nb_words} found in the document")
    print()
    for letter, count in letter_counter:
        print(f"The '{letter}' character was found {count} times")
    print(f"--- End report ---")

def main():
    filename = "books/frankenstein.txt"
    with open(filename, 'r', encoding='utf8') as f:
        text = f.read()
        print_report(filename, len(text.split()), get_counter(text))

if __name__ == "__main__":
    main()
