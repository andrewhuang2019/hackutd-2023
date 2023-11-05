import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename

class file_reader:
    UPLOAD_FOLDER = "upload_folder"
    ALLOWED_EXTENSIONS = {"csv"}

    app = Flask(__name__)
    app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

    @app.route("/uploader", methods = ["GET", "POST"])
    def upload_file():
        if request.method == "POST":
            f = request.files["file"]
            f.save(secure_filename(f.filename))
            #return "file uploaded successfully"

test = file_reader()
