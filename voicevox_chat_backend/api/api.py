from dotenv import load_dotenv
import os
from flask import Flask,request,jsonify
from chat.src.functions.chat_gpt import callChatGPT
from chat.src.functions.answerWav import playWav,makeWav

load_dotenv()
path = os.environ.get('PYTHONPATH')

app = Flask(__name__)

@app.route('/api',methods=['GET','POST'])
def api():
    try:
        data = request.get_json()
        text = data['post_text']

        res = callChatGPT(text)
        playWav(makeWav(text))
        response = {'result':res}
        return jsonify(response)
    except Exception as e:
        res = "エラーなのだ。もう一度内容を入力してほしいのだ"
        response = {'result':res}
        return jsonify(response)

app.run()