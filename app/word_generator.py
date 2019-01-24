from app.memo_dictionary import is_a_word

def get_words_by_length(letters, length):
  if length > len(letters): raise Exception('length is too big for these letters')
  if length == 1:
    return letters
  words = set([])
  for i in range(len(letters)):
    cur_letters = letters.copy()
    cur_letter = cur_letters.pop(i)
    smaller_words = get_words_by_length(cur_letters, length - 1)
    for word in smaller_words:
      words.add(cur_letter + word)
  return words

def filter_non_words(words):
  real_words = []
  for word in words:
    if is_a_word(word):
      real_words.append(word)
  return real_words
