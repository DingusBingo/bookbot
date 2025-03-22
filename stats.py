def get_word_count(text):
    seperated_text = text.split()
    count = 0
    for word in seperated_text:
        count += 1
    return count

def get_character_count(text):
    low = text.lower()
    total_chars = {}
    for char in low:
        if char in total_chars:
            total_chars[char] += 1
        else:
            total_chars[char] = 1
    return total_chars