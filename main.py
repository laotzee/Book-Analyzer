import re

def get_quotes(string):
    """Takes the handle of a file, and returns a list containing quotes found
    using regex. If not quotes are found, returns an empty list"""

    quotes = re.findall('[“"].+?["”]', string)
    return quotes

def dict_to_list(dictionary):
    """Take a dictionary as argument and then returns a list of binary tuples,
    where the first element is the value and the second the key."""
    binary_list = []
    for key, value in dictionary.items():
        binary_list.append((value, key))

    return binary_list

def show_words(word_list, most_used=True): 
    """Take a list with binary tuples and prints to the screen 10 most used words,
    False in the second parameter show the less used ones."""
    counter = 0
    msg1 = 'These are the most used words'
    msg2 = 'These are the least used words'
    word_list.sort()
    if most_used:
        word_list.reverse()
        msg2 = msg1

    print(msg2)
    for word, value in word_list:
        if counter == 10:
            break

        print(f'{word}: {value}')
        counter += 1

    return None

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
    """Take a list of words as argument and returns a dictionary that contains
    a word as a key, and its value represents the number of repetition 
    throughout the file"""

    word_counter = {}
    for word in word_list:
        word = word.lower()
        if word in word_counter:
            word_counter[word] += 1
        else:
            word_counter[word] = 1

    return word_counter

path1 = 'alice.txt'

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
counted_words = count_words(words)
organized_words = dict_to_list(counted_words)
show_words(organized_words)

try:
    answer = int(input(f"How many quotes would you like to list? (Max "\
                       f"{length})\n"))
    for num in range(answer):
        print(quotes[num])

except ValueError:
    print("You should have entered a number a whole number")
    exit()

except IndexError:
    print("There is not more quotes than these :(")
