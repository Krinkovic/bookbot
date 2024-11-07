def main():
    book = "books/frankenstein.txt"
    text = get_contents(book)
    words = count_words(text)
    characters = count_characters(text)
    print(characters)

def get_contents(book):
    with open(book) as file:
        return file.read()

def count_words(text):
    words = len(text.split())
    return words

def count_characters(text):
    character_count = {}
    for char in text:
        char = char.lower()
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1
    return character_count
        
main()