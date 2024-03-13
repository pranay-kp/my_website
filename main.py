from flask import Flask, abort, render_template, redirect, url_for, flash, request, send_file
from flask_bootstrap import Bootstrap5


app = Flask(__name__)
Bootstrap5(app)

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/cv")
def download_cv():
    file_path = "./Pranay's CV.pdf"
    return send_file(file_path, as_attachment=True)







if __name__ == "__main__":
    app.run(debug=True)