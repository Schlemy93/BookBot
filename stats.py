
def count_words(file_contents):
    num_of_words = len(file_contents.split())
    return num_of_words

def char_count(file_contents):
    char_count: dict[str, int] = {}
    file_contents = file_contents.lower()

    for char in file_contents:
        if char.isalpha():
           if char in char_count:
               char_count[char] += 1
           else:
               char_count[char] = 1
    return char_count

def sort_it(item):
    return item[1]


