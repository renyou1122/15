import os

print("開始修復你的網站...")

# 1. 強制建立正確的資料夾 (如果原本是壞的檔案會忽略，確保是資料夾)
os.makedirs('static', exist_ok=True)
os.makedirs('templates', exist_ok=True)
print("✅ 資料夾檢查完畢")

# 2. 自動產生一張紅色的測試圖片 (避免上傳失敗)
#這是一張 1x1 像素的紅色 PNG圖片的二進位資料
red_dot = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x02\x00\x00\x00\x90wS\xde\x00\x00\x00\x0cIDAT\x08\xd7c\xf8\xcf\xc0\x00\x00\x03\x01\x01\x00\x18\xdd\x8d\xb0\x00\x00\x00\x00IEND\xaeB`\x82'

with open('static/demo.png', 'wb') as f:
    f.write(red_dot)
print("✅ 圖片 (demo.png) 已重新產生")

# 3. 重寫一個保證路徑正確的 HTML
html_content = """
<!DOCTYPE html>
<html>
<head><meta charset="utf-8"></head>
<body style="text-align:center; padding: 50px;">
    <h1>🎉 維修成功！</h1>
    <p>如果看到下面有一個紅色的正方形，代表圖片路徑完全正確了：</p>
    <br>
    <img src="{{ url_for('static', filename='demo.png') }}" style="width: 100px; height: 100px; border: 3px solid black;">
</body>
</html>
"""
with open('templates/index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)
print("✅ 網頁 (index.html) 已更新")

print("-" * 30)
print("👉 修復完成！請在終端機輸入 python app.py 啟動網站")