
from flask_frozen import Freezer
from app import app
import shutil
import os

# 設定
app.config['FREEZER_RELATIVE_URLS'] = True
app.config['FREEZER_DESTINATION'] = 'docs'

freezer = Freezer(app)

# 1. 先清除舊的 docs
if os.path.exists('docs'):
    shutil.rmtree('docs')
    print("🧹 舊資料清理完畢")

# 2. 執行標準轉檔 (產生 HTML)
print("❄️ 正在產生 HTML...")
try:
    freezer.freeze()
except Exception as e:
    print(f"⚠️ 轉檔過程有小警告 (通常沒關係): {e}")

# 3. 【關鍵步驟】強制把 static 資料夾搬進去 docs
# 這一步保證圖片和影片一定會在！
print("📦 正在強制搬運圖片與影片...")
source_static = 'static'
dest_static = 'docs/static'

# 如果 static 資料夾還沒被複製過去，就手動複製
if os.path.exists(source_static):
    # 如果 docs/static 已經存在 (freezer 可能複製了一部分)，先刪掉避免衝突
    if os.path.exists(dest_static):
        shutil.rmtree(dest_static)
    
    # 複製整個資料夾
    shutil.copytree(source_static, dest_static)
    print(f"✅ 成功將 {source_static} 完整複製到 {dest_static}")
else:
    print("❌ 找不到原本的 static 資料夾！請檢查你的檔案結構。")

print("-" * 30)
print("🎉 轉檔完成！請檢查 docs 資料夾裡面有沒有東西。")