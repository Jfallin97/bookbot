import string

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(word_count(text))
    report(letter_count(text))

def get_book_text(path):
    with open(path) as f:
        return f.read()


def word_count(book_string):
    count = 0
    for i in book_string.split():
        count += 1
    return f"There are {count} words in this text"

def letter_count(text):
    keys = list(string.ascii_lowercase)
    lowered_string = text.lower()
    dict_count = dict()

    for i in keys:
        dict_count[f"{i}"] = 0
    for i in dict_count:
        for x in lowered_string:
            if x == i:
                dict_count[i] += 1
    return(dict_count)

def report(dict):
    for i in dict:
        print(f"The '{i}' was found {dict[i]} times.")

main()