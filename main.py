def main():
    book = "books/frankenstein.txt"
    text = get_contents(book)
    words = count_words(text)
    
    print(f"{words} found in document")

def get_contents(book):
    with open(book) as file:
        return file.read()

def count_words(text):
    words = len(text.split())
    return words
        
main()