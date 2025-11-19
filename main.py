import sys
from stats import get_num_words, chars_count, sort_list_of_dict

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return str(file_contents)

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1] #'books/frankenstein.txt'
    book_contents = get_book_text(book_path)
    book_num_words = get_num_words(book_contents)
    book_char_count = chars_count(book_contents)
    book_sorted_char_cnt = sort_list_of_dict(book_char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {book_num_words} total words")
    print("--------- Character Count -------")
    for d in book_sorted_char_cnt:
        print(': '.join(str(x) for x in d.values()), sep="\n")
    print("============= END ===============")

if __name__ == "__main__":
    main()