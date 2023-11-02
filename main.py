import re

path1 = 'alice.txt'

def get_quotes(string):
    """Takes the handle of a file, and returns a list containing quotes found
    using regex. If not quotes are found, returns an empty list"""

    quotes = re.findall('[“"].+?["”]', string)
    return quotes


def word_paragraph(handle):
    """Returns a tuple with the number of words and an approximate number of
    paragraphs"""

    words = []
    paragraph = 1

    for line in handle:
        if len(line) <= 2:
            paragraph += 1
            continue
        words += line.split()

    return words, paragraph

def count_words(word_list):
    """Take a list of words as argument and returns a dictionary that contains a word as a key, and its value represents the number of repetition throughout the file"""

    word_counter = {}

    for word in word_list:
        if word in word_counter:
            word_counter[word] += 1
        else:
            word_counter[word] = 1

        return word_counter

with open(path1) as book:
    words, paragraphs = word_paragraph(book)
    #The contents of the file are empty by the time I use get_quotes()
    #So I need to open the file in order access the information again
    #Perhaps change implementation of word_paragraph so that it takes data
    #Instead of the handle itself

with open(path1) as book:
    quotes = get_quotes(book.read())


word_length = len(words)
length = len(quotes)
inf = f"General information about the file:\n{word_length}: words\n{paragraphs}"\
    " paragraphs approximately"

print(inf)
print(words)

try:
    answer = int(input(f"How many quotes would you like to list? (Max "\
                       f"{length})\n"))

except ValueError:
    print("You should have entered a number a whole number")
    exit()

for num in range(answer):
    print(quotes[num])
