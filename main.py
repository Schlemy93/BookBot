import sys
from stats import count_words, char_count, sort_it

def get_book_text(filepath):
    with open(filepath, "r") as f:
         file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    book_contents = get_book_text(filepath)
    word_count = count_words(book_contents)
    char_freqs = char_count(book_contents)
    sorted_counts = sorted(char_freqs.items(), key=sort_it,reverse=True)


    print("============ BookBot ============")
    print(f"Analyzing book found at {filepath} ...")
    print("----------- Word Count -----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char, count in sorted_counts:
        print(f"{char}: {count}")
    print("============= END ===============")





if __name__ == "__main__":
    main()
