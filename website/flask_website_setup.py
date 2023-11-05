import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route("/")
def home():
    return redirect("https://nfrc.club/")


@app.route("/uploader", methods = ["GET", "POST"])
def upload_file():
    if request.method == "POST":
        f = request.files["file"]
        f.save(secure_filename(f.filename))
        #return "file uploaded successfully"

if __name__ == "__main__":
    app.run()