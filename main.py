import sys

from stats import get_word_count
from stats import get_char_count
from stats import dict_sort
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    words = get_book_text(path)
    count = get_word_count(words)
    uniques = get_char_count(words)
    char_list = dict_sort(uniques)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words") 
    print("--------- Character Count -------")
    for char_dict in char_list:
        char = char_dict["char"]
        qty = char_dict["num"]
        print(f"{char}: {qty}")
    print("============= END ===============")

def get_book_text(path):
    with open(path) as b:
        words = b.read()
    return words

main()