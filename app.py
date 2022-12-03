from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/aboutpompeii')
def aboutpompeii():
    return render_template('aboutpompeii.html')

@app.route('/newdiscovery')
def newdiscovery():
    return render_template('newdiscovery.html')

@app.route('/humanenv')
def humanenv():
    return render_template('humanenv.html')

@app.route('/archadvance-modernday')
def archadvancemodernday():
    return render_template('archadvance-modernday.html')


@app.route('/sources')
def sources():
    return render_template('sources.html')