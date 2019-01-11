from word_generator import get_words_by_length, filter_non_words

letters = ['u', 'n', 'c', 'i', 'o', 'r', 'n']
word_length = 5

words = get_words_by_length(letters, word_length)
#print(words)
print('len of words: ' + str(len(words)))
real_words = filter_non_words(words)
print(real_words)
