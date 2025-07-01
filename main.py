def main():
    from stats import count_words
    from stats import count_char

    text = get_book_text("books/frankenstein.txt")
    num_words = count_words(text)
    print(f"{num_words} words found in the document")
    num_char = count_char(text)
    print(num_char)

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()
    
main()