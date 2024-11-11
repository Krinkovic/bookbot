def main():
    book = "books/frankenstein.txt"
    print(f"--- Begin report of {book} ---")
    
    text = get_contents(book)
    num_words = count_words(text)
    
    print(f"{num_words} words found in the document")
    print()

    chars_dict = count_characters(text)
    sorted_list = sort_dict(chars_dict)

    for c in sorted_list:
        print(f"The letter {c['letter']} has {c['num']} occurances!")
    print("--- End report ---")

def get_contents(book):
    with open(book) as file:
        return file.read()

def count_words(text):
    num_words = len(text.split())
    return num_words

def count_characters(text):
    character_count = {}
    for char in text:
        char = char.lower()
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1
    return character_count

def sort(dict):
    return dict["num"]

def sort_dict(chars_dict):
    sorted_chars = []
    for c in chars_dict:
        if c.isalpha() == True:
            sorted_chars.append({"letter" : c.lower(), "num" : chars_dict[c]})
    sorted_chars.sort(reverse=True, key=sort)
    return sorted_chars

if __name__ == "__main__":
    main()