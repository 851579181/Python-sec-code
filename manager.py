# -*- coding：utf-8 -*-
from flask import Flask
from RCE import RCE
from SqlInjection import SqlInjection
from DownloadFile import DownloadFile
from SSRF import SSRF

app = Flask(__name__)

app.register_blueprint(RCE.RCE, url_prefix="/RCE")
app.register_blueprint(SqlInjection.SqlInjection, url_prefix="/SqlInjection")
app.register_blueprint(DownloadFile.DownloadFile, url_prefix="/DownloadFile")
app.register_blueprint(SSRF.SSRF, url_prefix="/SSRF")

@app.route("/")
def hello():
    return "hello world"

if __name__ == "__main__":
    app.run()


