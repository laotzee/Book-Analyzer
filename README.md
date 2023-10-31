# Book Analyzer
This program is meant to be a practice for parsing documents and extrating information using regex and other python tools. README file serves in this case as a roadmap for the thought process followed in the development of the project. 

Book Analyzer will take a .txt, or other equivalent file such as .md, and will return basic statistics for the file (word count, number of paragraphs), also will look for the quotations inside of it. 

The appended alice.txt file is a copy of the book 'Alice's Adventures in Wonderland' by Lewis Carroll, which is of public domain in the US and was downloaded from the website of the Project Gutenber. Said book is meant to serve a sample for testing the program.


## Features

### General Book Stats

Utilizing HtDF

Book handle > (word_count, paragraps) **Signature** 

Takes a book handle, a returns a tuple with the number of words and an approximation of the paragraphs **Purpose**

def word_paragraps(handle): (tuple) **Stub**


**Ex:**

word_paragrap(handle1) >>> (3234,350)
word_paragrap(handle2) >>> (238, 50)



#### Count number of words
The number of words that the word contained is obtained by breaking down the lines into sentences, and then into non-white character string greater than 1. I could do that by just taking out white spaces, but I have to tear apart the book into lines for next step

#### Get Number of Paragraphs
This is achieve by counting the number of empty strings when breaking down the book into sentences, denotating the end of a paragraph. This will of course be an approximation and not an exact number 

### Get Quotes from the Book

Here I would need to go through the book, extracting all instances that are quotes. This would require to identify some kind of patter, given that sometimes quotes are separated by a text like:

These are the main patter spotted inside of the example file: 

> "phrase" said someone "continuing the phrase".
> "phrase" said someone

The regex patters should look like: ".+" \S+ \S+\. ".+"?

### Search sentences containing certain words

The idea is to look for sentences containing word or set of related words and returns the occurence of them. 

Ex. (Knowledge, Intelligence, Wit, Intelligent, Wise, Smart)
