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

def sort_character_dictionary(char_dict):
    character_list = create_character_list(char_dict)
    character_list.sort(reverse=True, key=sort_num)
    return character_list

def create_character_list(char_dict):
    character_list = []
    for k in char_dict:
        c = char_dict[k]
        d = {"name": k, "num": c}
        character_list.append(d)
    return character_list


def sort_num(dict):
    return dict["num"]