from flask import Flask, request, jsonify, render_template
from app.word_generator import get_words_by_length, filter_non_words
from google.cloud import storage

app = Flask(__name__, template_folder='app/templates')

@app.route('/')
def index():
    word = list(request.args.get('w',''))
    length = request.args.get('l', '')
    if length == '':
        length = range(3, len(word)+1)
    else:
        length = [int(length)]
    all_words = []
    for i in range(len(length)):
        words = get_words_by_length(word, length[i])
        print('len of words: '+ str(len(words)))
        real_words = filter_non_words(words)
        all_words.append(real_words)
    return jsonify(all_words)

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
    length = request.form['length']
    return render_template(
        'posted_word.html',
        word=word,
        length=length)

if __name__ == '__main__':
    app.run(
        debug=True,
        host='0.0.0.0', 
        port=8080)
