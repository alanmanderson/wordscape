from word_generator import get_words_by_length, filter_non_words

letters = ['t', 'e', 'n', 'i', 'f', 'f', 'e']
word_length = 7

words = get_words_by_length(letters, word_length)
print(words)

real_words = filter_non_words(words)
print(real_words)
