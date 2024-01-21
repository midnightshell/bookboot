
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = words_count(text=text)
    # print(num_words)
    num_letter = get_count_letters(text=text)
    # print(num_letter)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    for key in num_letter:
        print(f"The {key} character was found {num_letter[key]} times")

def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_count_letters(text):
    letters_dict = {}
    lowercase = text.lower()
    for x in lowercase:
        if x in letters_dict:
            letters_dict[x] += 1
        else:
            letters_dict[x] = 1

    return letters_dict



def words_count(text):
    text_in_array = text.split()
    count = len(text_in_array)
    return count

main()
