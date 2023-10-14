from flask import Flask
from flask import render_template, request, jsonify
import pyqrcode

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/make_qrcode", methods=["POST"])
def make_qrcode():
    text = request.get_json()['text']
    q = pyqrcode.create(text)
    base64 = q.png_as_base64_str(scale=5, module_color=[0,0,0,255])
    return jsonify(error="ok", data=base64)

if __name__ == "__main__" :
    app.run(port=8999, debug=True)