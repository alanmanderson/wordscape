from word_generator import get_words_by_length, filter_non_words

from arg_parser import get_args

args = get_args()

letters = args.w
letters = list(letters)
if args.a:
    word_lengths = range(3, len(letters)+1)
else:
    word_lengths = [args.l] 

for i in range(len(word_lengths)):
    words = get_words_by_length(letters, word_lengths[i])
    print('len of words: ' + str(len(words)))
    real_words = filter_non_words(words)
    print(real_words)
