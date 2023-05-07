import re

text = 'The quick brown fox jumps over the lazy dog is an ' \
       'English-language pangram-a sentence that ' \
       'contains all of the letters of the English alphabet'

words = re.split('[ -]', text)
length_of_words = [len(word) for word in words if word not in ('The', 'the')]
