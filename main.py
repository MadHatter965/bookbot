import sys
from stats import get_word_count, get_char_count, get_sorted_list

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path to book>")
    sys.exit(1)

def get_book_text(book_path):
    with open(book_path) as f:
        book_text = f.read()
    return book_text

def main():
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    word_count = get_word_count(book_text)
    char_count = get_char_count(book_text)
    sorted_list = get_sorted_list(char_count)


    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
   
    for char_dict in sorted_list:
        char = char_dict["char"]
        count = char_dict["count"]
        if char.isalpha():
            print(f"{char}: {count}")

    print("============= END ===============")
    
# never have I done this before nor was it explained in the basics. Thank god for Boots.
if __name__ == "__main__":
    main()