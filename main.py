from flask import Flask, request, jsonify, render_template
from app.word_generator import get_words_by_length, filter_non_words
from app.wordscape import get_wordscape_words
from google.cloud import storage

app = Flask(__name__, template_folder='app/templates',
static_folder='app/static')

@app.route('/')
def index():
    word = list(request.args.get('w',''))
    length = get_word_lengths(request.args.get('l', ''), len(word))
    return render_template(
        'posted_word.html',
        word=word,
        length=length,
        words=get_wordscape_words(word,length))

@app.route('/test')
def test():
    client = storage.Client()
    bucket = client.get_bucket('wordscape.appspot.com')
    blob = bucket.get_blob('words.txt')
    return blob.download_as_string()

@app.route('/word')
def word():
    return render_template('word.html')

@app.route('/word', methods=['POST'])
def post_word():
    word = request.form['word']
    length = get_word_lengths(request.form['length'], len(word))
    words = get_wordscape_words(list(word), length)
    return render_template(
        'posted_word.html',
        word=word,
        length=length,
        words=words)

def get_word_lengths(user_input, word_length):
    if user_input == '' or user_input == None:
        return range(3, word_length + 1)
    return [int(user_input)]

if __name__ == '__main__':
    app.run(
        debug=True,
        host='0.0.0.0', 
        port=8080)
