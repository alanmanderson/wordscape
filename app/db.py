import os
from google.cloud import storage

#file_path = os.path.dirname(os.path.abspath(__file__))

#WORDS_FILE = file_path + '/../words/collegiate/words.txt'
#NOT_WORDS_FILE = file_path + '/../words/collegiate/not_words.txt'

WORDS_FILE = 'collegiate/words.txt'
NOT_WORDS_FILE = 'collegiate/not_words.txt'
BUCKET = os.getenv('WORDS_BUCKET')
client = storage.Client()
bucket = client.get_bucket(BUCKET)
words_blob = bucket.get_blob(WORDS_FILE)
not_words_blob = bucket.get_blob(NOT_WORDS_FILE)

def get_words(blob):
    words = blob.download_as_string().decode()
    words = words.split(',')
    return set(words)

def get_real_words():
  return get_words(words_blob)

def get_non_words():
  return get_words(not_words_blob)

#def save_words(filename, words):
#  with open(filename, 'w+') as f:
#    f.write(','.join(words))

def save_words(blob, words):
    content = blob.download_as_string().decode()
    content += ',' + ','.join(words)
    blob.upload_from_string(content)

def save_real_words(words):
    save_words(words_blob, words)

def save_non_words(words):
    save_words(not_words_blob, words)

def add_word(filename, word):
  with open(filename, 'a+') as f:
    f.write(',' + word)

def add_real_word(word):
  return add_word(WORDS_FILE, word)

def add_non_word(word):
  return add_word(NOT_WORDS_FILE, word)
