import os

file_path = os.path.dirname(os.path.abspath(__file__))

WORDS_FILE = file_path + '/../words/collegiate/words.txt'
NOT_WORDS_FILE = file_path + '/../words/collegiate/not_words.txt'

def get_words(filename):
  with open(filename, 'r') as f:
    words = f.read()
    words = words.split(',')
  return set(words)

def get_real_words():
  return get_words(WORDS_FILE)

def get_non_words():
  return get_words(NOT_WORDS_FILE)

def save_words(filename, words):
  with open(filename, 'w') as f:
    f.write(','.join(words))

def add_word(filename, word):
  with open(filename, 'a') as f:
    f.write(',' + word)

def add_real_word(word):
  return add_word(WORDS_FILE, word)

def add_non_word(word):
  return add_word(NOT_WORDS_FILE, word)
