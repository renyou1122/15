import os
import shutil
from flask_frozen import Freezer
from app import app

# 1. 初始化設定
app.config['FREEZER_RELATIVE_URLS'] = True
app.config['FREEZER_DESTINATION'] = 'docs'
freezer = Freezer(app)

print("🚀 開始建置靜態網站...")

# 2. 清理舊的 docs 資料夾
if os.path.exists('docs'):
    shutil.rmtree('docs')
    print("🧹 清除舊資料完成")

# 3. 執行轉檔 (產生 HTML)
try:
    freezer.freeze()
    print("❄️ HTML 轉檔完成")
except Exception as e:
    print(f"⚠️ 轉檔過程警告: {e}")

# 4. 【強制搬運】把 static 資料夾完整複製過去
# 這樣保證圖片影片一定會在
source_static = 'static'
dest_static = 'docs/static'

if os.path.exists(source_static):
    if os.path.exists(dest_static):
        shutil.rmtree(dest_static) # 如果 freezer 已經建了一部分，先清掉避免衝突
    shutil.copytree(source_static, dest_static)
    print(f"📦 靜態檔案 (圖片/影片) 已強制複製到 {dest_static}")
else:
    print("❌ 警告：找不到你的 static 資料夾！")

# 5. 【暴力修正】直接修改 HTML 裡的錯誤路徑
# 這是為了修復 GitHub Pages 常見的 404 問題
index_path = 'docs/index.html'
if os.path.exists(index_path):
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 把絕對路徑 /static 改成相對路徑 static
    # 這樣不管放在哪裡都讀得到
    new_content = content.replace('src="/static', 'src="static')
    new_content = new_content.replace('href="/static', 'href="static')
    
    # 順便修正影片路徑，如果它也是寫死的話
    new_content = new_content.replace('src="/static', 'src="static')

    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("🔧 路徑修正完畢 (已將 /static 改為 static)")

print("-" * 30)
print("✅ 建置完成！請執行 git push 上傳更新。")