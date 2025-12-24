import base64
import os
os.makedirs('static', exist_ok=True)
img_data = b'iVBORw0KGgoAAAANSUhEUgAAAGQAAABkCAIAAAD/gAIDAAAAE0lEQVR4nGP4z8DQzsDQAEnzqHk0j5pH86h5NI+aR/OoeTQPAwMA9XO/xHkAA54AAAAASUVORK5CYII='
with open('static/ONE.png', 'wb') as f:
    f.write(base64.b64decode(img_data))
print('✅ 成功產生圖片！')