from mw_api.mw import *
from db import *

words = get_real_words()
non_words = get_non_words()

def is_a_word(word):
  global words
  global non_words
  if word in words: return True
  if word in non_words: return False
  try:
    dictionary = CollegiateDictionary('9ec3c5f4-167f-43b0-8351-dd8c8661bea3')
    dictionary.lookup(word)
    words.add(word)
    add_real_word(word)
    return True
  except WordNotFoundException as err:
    non_words.add(word)
    add_non_word(word)
    return False
