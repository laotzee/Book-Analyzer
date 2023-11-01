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
    citation = main.get_quotes(test.read())

assert should_be_quote == citation
