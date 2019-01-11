from merriam_webster.api import *
from db import *
from time import sleep
from os import getenv

words = get_real_words()
non_words = get_non_words()

def is_a_word(word):
  global words
  global non_words
  if word in words: return True
  if word in non_words: return False
  api_key = getenv('MERRIAM_WEBSTER_COLLEGIATE_KEY')
  retry = 0
  while retry < 3:
    try:
      dictionary = CollegiateDictionary(api_key)
      dictionary.lookup(word)
      words.add(word)
      add_real_word(word)
      return True
    except WordNotFoundException as err:
      non_words.add(word)
      add_non_word(word)
      return False
    except TypeError as err:
      if retry >= 3: raise err
      print(err)
      print("sleeping for 60 seconds")
      sleep(60)
      retry += 1

