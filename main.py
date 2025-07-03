import sys

def main():
    from stats import count_words, char_occurrences, get_sorted_char_list

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    text = get_book_text(sys.argv[1])
    num_words = count_words(text)
    char_counts = char_occurrences(text)
    sorted_char_counts = get_sorted_char_list(char_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count -----------")
    print(f"Found {num_words} total words")
    print("-------- Character Count --------")
    for item in sorted_char_counts:
        print(f"{item["char"]}: {item["num"]}")
    print("============== END ==============")

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()
    
main()