from stats import get_num_words, get_book_text, get_num_char, sorted_list

import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
book_path = sys.argv[1]

def main():
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_dict = get_num_char(text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_list(char_dict):
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()