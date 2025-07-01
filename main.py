def main():
    from stats import count_words, count_char, get_sorted_char_list

    text = get_book_text("books/frankenstein.txt")
    num_words = count_words(text)
    char_counts = count_char(text)
    sorted_char_list = get_sorted_char_list(char_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at books/frankenstein.txt")
    print("----------- Word Count -----------")
    print(f"Found {num_words} total words")
    print("-------- Character Count --------")
    for item in sorted_char_list:
        print(f"{item["char"]}: {item["num"]}")
    print("============== END ==============")

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()
    
main()