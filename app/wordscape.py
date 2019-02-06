from app.word_generator import get_words_by_length, filter_non_words

def get_wordscape_words(letters, word_lengths):
    returned_words = []
    for i in range(len(word_lengths)):
        words = get_words_by_length(letters, word_lengths[i])
        print('len of words: ' + str(len(words)))
        words = filter_non_words(words)
        words.sort()
        returned_words.append(words)
    return returned_words
