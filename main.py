from stats import get_word_count, get_character_count, sort_character_dictionary, create_character_list
import sys

character_totals = {}
character_list = []
book_filepath = ""

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def print_report(words, characters, book):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for dict in characters:
        c = ""
        n = 0
        for key, value in dict.items():
            if key == "name":
                c = value
            elif key == "num":
                n = value
        if c.isalpha():
            print(f"{c}: {n}")
    print("============= END ===============")



def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_filepath = sys.argv[1]
    text = get_book_text(book_filepath)
    count = get_word_count(text)
    character_totals = get_character_count(text)
    character_list = sort_character_dictionary(character_totals)
    print_report(count, character_list, book_filepath)

main()