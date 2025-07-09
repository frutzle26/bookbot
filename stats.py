import sys

def word_count(path_to_book):
    with open(path_to_book) as f:
        words = f.read()
    count = words.split()
    print(f"{len(count)} words found in the document")

def letter_count(path_to_book):
    letters = {}
    with open(path_to_book) as f:
        words = f.read()
    for i in words.lower():
        if i in letters:
            letters[i] += 1
        else:
            letters[i] = 1
    return(letters)

def sorted_list(path_to_book):
    letters = letter_count(path_to_book)
    letters_list = []
    for char, count in letters.items():
        if char.isalpha():
            letters_list.append({"char": char, "num": count})
    letters_list.sort(reverse=True, key=lambda x: x["num"])
    return letters_list