def count_words(text):
    return len(text.split())

def count_char(text):
    text_lower = text.lower()
    char_dict = {}

    for char in text_lower:
        if char not in char_dict:
            char_dict[char] = 0
        char_dict[char] += 1

    return char_dict