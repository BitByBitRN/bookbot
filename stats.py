def count_words(text):
    return len(text.split())

def char_occurrences(text):
    text_lower = text.lower()
    char_dict = {}

    for char in text_lower:
        if char not in char_dict:
            char_dict[char] = 0
        char_dict[char] += 1

    return char_dict

def sort_on(chars):
    return chars["num"]

def get_sorted_char_list(char_counts):
    char_list = []

    for char in char_counts:
        if char.isalpha():
            char_entry = {"char": char, "num": char_counts[char]}
            char_list.append(char_entry)

    char_list.sort(reverse=True, key=sort_on)

    return char_list