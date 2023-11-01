import re

path1 = 'alice.txt'

def get_quotes(string):
    """Takes the handle of a file, and returns a list containing quotes found
    using regex. If not quotes are found, returns an empty list"""

    citation = re.findall('[“"].+?["”]', string)
    return citation


def word_paragraph(handle):
    """Returns a tuple with the number of words and an approximate number of
    paragraphs"""

    words = 0
    lines = []
    paragraph = 1

    for line in handle:
        if len(line) <= 1: paragraph += 1
        lines.append(line)

    for line in lines[:]:
        line = line.split()
        words += len(line)

    return words, paragraph

with open(path1) as book:
    words, paragraphs = word_paragraph(book)

inf = f"General information about the file:\n{words}: words\n{paragraphs}"\
    " paragraphs approximately"

print(inf)

with open(path1) as book:
    quotes = get_quotes(book.read())


length = len(quotes)

try:
    answer = int(input(f"How many quotes would you like to list? (Max "\
                       f"{length})\n"))

except ValueError:
    print("You should have entered a number a whole number")
    exit()

for num in range(answer):
    print(quotes[num])
