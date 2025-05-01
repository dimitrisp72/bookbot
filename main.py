from stats import *
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        book = f.read()
    return book

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]

    book = get_book_text(filepath)
    num_words = get_num_words(book)
    my_bookdict = get_chars(book)
    my_booklist = get_list(my_bookdict)
    my_sorted_list = sort_list(my_booklist)
    print(f"{'=' * 12} BOOKBOT {'=' * 12}")
    print(f"Analyzing book found at {filepath}...")
    print(f"{'-' * 11} Word Count {'-' * 10}")
    print(f"Found {num_words} total words")
    print(f"{'-' * 9} Character Count {'-' * 7}")
    for item in my_sorted_list:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")
    print(f"============= END ===============")

main()