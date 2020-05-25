from flask import Flask, jsonify
import urllib.request as req
import bs4

app = Flask(__name__)

@app.route("/")

def retrive():
    url = "https://www.ptt.cc/bbs/Stock/index.html"
    # 幫request加上一個header
    request = req.Request(url, headers = {
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:72.0) Gecko/20100101 Firefox/72.0"
    })
    
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
    return data
    root = bs4.BeautifulSoup(data,"html.parser")
    titles = root.find("div", class_="title")
    titles = root.find_all("div", class_="title")

    res = []
    for title in titles:
        if title.a.string.find("Re:"):
            res.append(title.a.string)
    return res

def hello():
    title = "<title>Advanced Materials of Python</title>"
    h1 = "<h1>Python based web</h1>"
    p1 = "<p>Hello python</p>"
    return jsonify(retrive())

if __name__ == "__main__":
    app.run()

