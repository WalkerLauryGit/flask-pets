from flask import Flask, render_template
app = Flask(__name__)
app._static_folder = "templates/static/images"


@app.route('/')
def index():
    return render_template('index.html')
