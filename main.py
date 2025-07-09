import sys
from stats import word_count, sorted_list


def main(path_to_book):
    result = sorted_list(path_to_book)
    for entry in result:
        print(f"{entry["char"]}: {entry["num"]}")        

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    path_to_book = sys.argv[1]    

print("============ BOOKBOT ============")
print("Analyzing book found at <path_to_book>...")
print("----------- Word Count ----------")
word_count(path_to_book)
print("--------- Character Count -------")
main(path_to_book)
print("============= END ===============") 