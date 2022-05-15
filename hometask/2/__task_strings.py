# 1. Fill missing pieces
# Fill ____ pieces below to have correct values for lower_cased, stripped and stripped_lower_case variables.

original = ' Python strings are COOL! '
lower_cased = original.lower()
stripped = original.strip()
stripped_lower_cased = original.lower().strip()

print(lower_cased)
print(stripped)
print(stripped_lower_cased)

assert lower_cased == ' python strings are cool! '
assert stripped == 'Python strings are COOL!'
assert stripped_lower_cased == 'python strings are cool!'

# 2. Prettify ugly string
# Use str methods to convert ugly to wanted pretty.

ugly = ' tiTle of MY new Book\n\n'
# Your implementation:

pretty = 'TODO'
normal_str = ugly.title().strip()
edited_str = normal_str.replace("\n", "")
print(edited_str + ' {}'.format(pretty))

# assert pretty == 'Title Of My New Book'

# 3. Format string based on existing variables
# Create sentence by using verb, language, and punctuation and any other strings you may need.

verb = 'is'
language = 'Python'
punctuation = '!'
# Your implementation:

sentence = 'TODO'
words = ["Learning", "Phyton", 'is', "fun", "!"]
new_sentence = ' '.join(words)
print('{} '.format(sentence) + new_sentence)
assert sentence == 'Learning Python is fun!'