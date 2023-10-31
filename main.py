import re

path1 = 'alice.txt'


def word_paragraph(handle):
    """Returns a tuple with the number of words and an approximate number of paragraphs"""

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



print(f"General Information about the book:\n{words} words\n{paragraphs} paragraphs approximately")



