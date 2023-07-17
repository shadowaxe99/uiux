from flask import Flask, render_template
from flask_mobility import Mobility

app = Flask(__name__)
Mobility(app)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)