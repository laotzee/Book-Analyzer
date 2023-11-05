import re
import main

test_dict1 = {
        'Laotze': 5,
        'Python':1,
        'Focus':6,
        'Zen': 7
        }

test_dict2 = {
        'glass': 1111,
        'Laptop': 5, 
        'Linux': 4,
        'Book': 1200,
        'Cardboard': 1
        }

should_be_list1 = [
        (5, 'Laotze'),
        (1, 'Python'),
        (6, 'Focus'),
        (7, 'Zen')
        ]

should_be_list2 = [
        (1111, 'glass'),
        (5, 'Laptop'),
        (4, 'Linux'),
        (1200, 'Book'),
        (1, 'Cardboard')
        ]

test_string1 = "This should be a string that does not have a meaningful message or anything"

test_string1_result = {'this': 1,
                       'should': 1,
                       'be': 1,
                       'a': 2,
                       'string': 1,
                       'that': 1,
                       'does': 1, 
                       'not': 1,
                       'have': 1, 
                       'meaningful': 1,
                       'message': 1,
                       'or': 1,
                       'anything': 1
                       }

should_be_quote = [
    '"If you don\'t hire me, you are losing a valuable asset"',
    '"and what is the use of a book,"',
    '"without pictures or conversations?"',
    '"Oh dear! Oh dear! I shall be late!"',
    '"Oh dear! Oh dear! I shall be late!"'
]
word_list1 = main.dict_to_list(test_dict1)
word_list2 = main.dict_to_list(test_dict2)

assert word_list1 == should_be_list1
assert  word_list2 == should_be_list2

main.show_words(word_list2, False)


with open("quotes.md") as test:
    data = test.read()
    citation = main.get_quotes(data[:])

words_list = test_string1.split()
words_counted = main.count_words(words_list)

assert words_counted == test_string1_result
assert should_be_quote == citation
