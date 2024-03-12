# Flask網站前後端互動 09 - 超連結與圖片
# 載入Flask、Request、render_template
from flask import Flask, request, render_template

# 建立 Application 物件,設定靜態檔案的路徑處理
# http://127.0.0.1:5000/head.png 為圖片路徑
app = Flask(__name__, static_folder="public", static_url_path="/")

# 處理路徑 / 的對應函市
@app.route("/")

def main():
    return render_template("main.html")

@app.route("/page")

def page():
    #從main.html頁面中讀取姓名，存在name中
    name = request.args.get("nameis")
    #將name的資料轉給pate.html中的變數namepage
    return render_template("page.html", namepage=name)
# 啟動Server

app.run()