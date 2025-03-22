from stats import get_word_count, get_character_count

character_totals = {}

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents



def main():
    text = get_book_text("books/frankenstein.txt")
    count = get_word_count(text)
    print(f"{count} words found in the document")


main()