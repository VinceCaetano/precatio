from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from assistant import process_question, read_bible_text
from utils import speak

app = Flask(__name__)
CORS(app)

bible_text = read_bible_text('bible.txt')

## flask p redenizar o template html
@app.route('/')
def home():
    return render_template('index.html', message='Welcome to Mana One!')

@app.route('/ask', methods=['POST'])
def ask():
    try:
        data = request.get_json()
        question = data['question']
        response = process_question(question, bible_text)
        speak(response['answer'])  
        return jsonify(response)
    except Exception as e:
        return jsonify(answer=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
