from flask import Flask
from flask import send_file

# 第三方模块

app = Flask(__name__)


# 根路径页面
@app.route('/')
def home():
    return send_file('./头像1.jpg', mimetype='image/gif')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3001, ssl_context=(
        "C:/Users/v_psmpeng/cert.pem", "C:/Users/v_psmpeng/key.pem"))

