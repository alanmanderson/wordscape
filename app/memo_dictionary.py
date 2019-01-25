from merriam_webster.api import *
from app import db
from time import sleep
from os import getenv

words = db.get_real_words()
non_words = db.get_non_words()

new_words = set()
new_non_words = set()

def add_new_words():
    db.save_real_words(new_words)
    db.save_non_words(new_non_words)

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
      new_words.add(word)
      return True
    except WordNotFoundException as err:
      non_words.add(word)
      new_non_words.add(word)
      return False
    except TypeError as err:
      if retry >= 3: raise err
      print(err)
      print("sleeping for 60 seconds")
      sleep(60)
      retry += 1

