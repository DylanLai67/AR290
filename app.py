from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/aboutpompeii')
def aboutpompeii():
    return render_template('aboutpompeii.html')





