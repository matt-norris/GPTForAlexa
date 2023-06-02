from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from gpt4free import you


app = Flask(__name__)


CORS(app, resources={r"/*": {"origins": "*"}})


chat = []


@app.route('/ask_question', methods=['POST'])
def ask_question():

    question = request.json.get('question', '')
    if not question:
        return jsonify({'error': 'No question provided'}), 400
    # simple request with links and details
    gptresponse = you.Completion.create(prompt=question, detailed=True, include_links=True,  chat=chat)
    chat.append({"question": question, "answer": gptresponse.text})

    return jsonify({'answer': gptresponse.text})
    # return jsonify({'answer': gptresponse.text, 'audio': audio_base64string})


if __name__ == '__main__':
    app.run(port=5300, debug=True)
