# Book Analyzer
This program is meant to be a practice for parsing documents and extrating information using regex and other python tools. README file serves in this case as a roadmap for the thought process followed in the development of the project. 

Book Analyzer will take a .txt, or other equivalent file such as .md, and will return basic statistics for the file (word count, number of paragraphs), also will look for the quotations inside of it. 

The appended alice.txt file is a copy of the book 'Alice's Adventures in Wonderland' by Lewis Carroll, which is of public domain in the US and was downloaded from the website of the Project Gutenber. Said book is meant to serve a sample for testing the program.


## Features

### General Book Stats

Utilizing HtDF

Book handle > (words, paragraph_number) **Signature** 

Takes a file handle, a returns a tuple with the words and an approximation of the paragraphs inside of the file**Purpose**

def word_paragraps(handle): (tuple) **Stub**


**Ex:**

word_paragrap(handle1) >>> (tuple ,350)
word_paragrap(handle2) >>> (tuple , 50)



#### Count number of words
The number of words that the word contained is obtained by breaking down the lines into sentences, and then into non-white character string greater than 1. I could do that by just taking out white spaces, but I have to tear apart the book into lines for next step.

#### Get Number of Paragraphs
This is achieve by counting the number of empty strings when breaking down the book into sentences, denotating the end of a paragraph. This will of course be an approximation and not an exact number 

#### Most Repeated Words

As for the most repeated words, I will change slightly the implementation for counting the number of words; instead of giving me directly the amount of words, it will give me back a tuple with words, so that I can check the size and analyze the data while only going through it once.

- A function to count what are the most used words

Word list -> dictionary **Signature**

Takes a list of words as argument and returns a dicionary that contains a word as a key, and its value represents its repetition throughout the file **Purpose**

Ex.

count_words(list1) = {'attention': 5, 'mindful': 10, 'caring': 3, 'calmness':15, 'peacefull': 20}
count_words(list2) = {'keyboard': 7, 'workflow': 2, 'proficiency': 8}

def count_words(word_list): return dictionary


- Show the most used words along, like 10 of them:

- Function to swap values for being able to organized. 

Dictionary -> List **Signature**

Takes a dictionary as argument and then returns a list of binary tuples, where the first element is the value and the second element is the key.  **Purpose**

def dict_to_list(): list() **Stub**



These two can be the same, I'll just add an extra parameter to indicate that. Even, when I finish the sorting practice, I can implement that instead of the Python built-in function.

- Function to show most used
- Function to show less used


### Get Quotes from the Book

Here I would need to go through the book, extracting all instances that are quotes. This would require to identify some kind of patter, given that sometimes quotes are separated by a text like:

These are the main patter spotted inside of the example file: 

> "phrase" said someone "continuing the phrase".
> "phrase" said someone

The regex patters should look like: ".+" \S+ \S+\. ".+"?


by HtDF definition

handle > list: **Signature**

Takes the handle of a file, and returns a list containing quotes found using regex. If not quotes are found, returns an empty list. **Purpose**

def quotes(handle): list **stub**

Ex.


' "If you don't hire me, you are losing a valuable asset" said as a matter of fact the humble developer'  >>>>> "If you don't hire me, you are losing a valuable asset"


Alice was beginning to get very tired of sitting by her sister on the
bank, and of having nothing to do: once or twice she had peeped into
the book her sister was reading, but it had no pictures or
conversations in it, “and what is the use of a book,” thought Alice
“without pictures or conversations?” >>>>>>  “and what is the use of a book,” thought Alice “without pictures or conversations?” 


There was nothing so _very_ remarkable in that; nor did Alice think it
so _very_ much out of the way to hear the Rabbit say to itself, “Oh
dear! Oh dear! I shall be late!” (when she thought it over afterwards,
it occurred to her that she ought to have wondered at this, but at the
time it all seemed quite natural) >>>> “Oh dear! Oh dear! I shall be late!”


I need to make a patter which starts with something inside quotes, and optionally it will have some characters followed by another set of quotation marks.

".+" ?.+?? ".+?"?



### Search sentences containing certain words

The idea is to look for sentences containing word or set of related words and returns the occurence of them. 

Ex. (Knowledge, Intelligence, Wit, Intelligent, Wise, Smart)




### Replace any character name with yours!

If you ever wanted to be in your favorite book, now it's your time. Kinda. This feature lets you change the name of the main character for yours, or change each instance of any name in the text for yours.

The way for implementing this is by using the method .sub() from re.

