from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def home():
    # 這裡加個隨機數字，強迫瀏覽器不要用舊快取
    version = random.randint(1, 10000)
    return render_template('index.html', v=version)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
