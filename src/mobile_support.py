```python
from flask import Flask, render_template
from flask_mobility import Mobility

app = Flask(__name__)
Mobility(app)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
```
This code initializes a Flask application with Flask-Mobility, a library that detects mobile devices and serves a mobile-friendly version of the Clippy UI. The 'index.html' template would contain the mobile-friendly version of the Clippy UI.