import re
import main

should_be_quote = [
    '"If you don\'t hire me, you are losing a valuable asset"',
    '"and what is the use of a book,"',
    '"without pictures or conversations?"',
    '"Oh dear! Oh dear! I shall be late!"',
    '"Oh dear! Oh dear! I shall be late!"'
]

with open("quotes.md") as test:
    data = test.read()
    citation = main.get_quotes(data[:])

with open("quotes.md") as test:
    words, x = main.word_paragraph(test)
    top_words = main.count_words(words)

for word, num in top_words.items():
    print(f"word: {word}\nnum:{num}")

assert should_be_quote == citation
assert type(top_words) == dict
