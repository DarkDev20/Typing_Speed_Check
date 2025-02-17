from flask import Flask, render_template, request, jsonify
import time
import random

app = Flask(__name__)

phrases = [
    "Python is an interpreted, high-level programming language",
    "Typing fast and accurately is a valuable skill",
    "Practice makes perfect, keep improving your speed",
    "Artificial intelligence is shaping the future of technology",
    "Debugging is like being the detective in a crime movie where you are also the murderer"
]

def get_random_phrase():
    return random.choice(phrases)

@app.route('/')
def home():
    phrase = get_random_phrase()
    return render_template('index.html', phrase=phrase)

@app.route('/calculate_results', methods=['POST'])
def calculate_results():
    data = request.get_json()
    input_text = data.get("input_text", "")
    phrase = data.get("phrase", "")
    t0 = float(data.get("start_time", 0))
    t1 = float(data.get("end_time", 0))

    input_words = input_text.split()
    phrase_words = phrase.split()
    length_of_input = len(input_words)
    word_count = len(phrase_words)

    accuracy = len(set(input_words) & set(phrase_words)) / word_count if word_count > 0 else 0
    time_taken = t1 - t0
    words_per_minute = (length_of_input / time_taken) * 60 if time_taken > 0 else 0

    return jsonify({
        "total_words": length_of_input,
        "time_used": round(time_taken, 2),
        "accuracy": round(accuracy * 100, 2),
        "words_per_minute": round(words_per_minute, 2)
    })

if __name__ == '__main__':
    app.run(debug=True)
