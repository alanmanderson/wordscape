from flask import Flask, request, jsonify
from word_generator import get_words_by_length, filter_non_words
app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
