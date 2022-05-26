# Write a python program that will replace a word with a given length by the provided word
# Example if I have a sentence:
# This is a brown fox
# Add more tests for this as an example below

sentence = "Beginners when start programming often get bored if they do not get a chance to " \
           "play with some interesting code."
# print(sentence.split())

def replace_words(sentence, length=3):
    if len(sentence) == length:
            return 'test'
    else:
            return sentence

split_sent = sentence.split()
new_split_sent = [replace_words(word) for word in split_sent]
new_sent = ' '.join(new_split_sent)
print(new_sent)

# assert replace_words(sentence, 3,
#                      "test") == "Beginners when start programming often test bored if they do test test a chance " \
#                                 "to play with some interesting code."
