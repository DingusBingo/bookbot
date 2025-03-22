from stats import get_word_count, get_character_count, sort_character_dictionary, create_character_list

character_totals = {}

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def print_report(words, characters):
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")



def main():
    text = get_book_text("books/frankenstein.txt")
    count = get_word_count(text)
    character_totals = get_character_count(text)
    print(f"{count} words found in the document")
    print(character_totals)

main()