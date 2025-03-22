from stats import get_word_count, get_character_count, sort_character_dictionary, create_character_list

character_totals = {}
character_list = []

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
    text = get_book_text("books/frankenstein.txt")
    count = get_word_count(text)
    character_totals = get_character_count(text)
    character_list = sort_character_dictionary(character_totals)
    print_report(count, character_list)

main()