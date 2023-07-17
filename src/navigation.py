```python
from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('project_dashboard'))

@app.route('/project_dashboard')
def project_dashboard():
    return render_template('dashboard.py')

@app.route('/project_timeline')
def project_timeline():
    return render_template('timeline.py')

@app.route('/code_editor')
def code_editor():
    return render_template('code_editor.py')

@app.route('/feedback')
def feedback():
    return render_template('feedback.py')

@app.route('/agent_management')
def agent_management():
    return render_template('agent_management.py')

@app.route('/chat_interface')
def chat_interface():
    return render_template('chat_interface.py')

@app.route('/testing_interface')
def testing_interface():
    return render_template('testing_interface.py')

@app.route('/search')
def search():
    return render_template('search.py')

@app.route('/data_visualization')
def data_visualization():
    return render_template('data_visualization.py')

@app.route('/integrations')
def integrations():
    return render_template('integrations.py')

@app.route('/clippy_avatar')
def clippy_avatar():
    return render_template('clippy_avatar.py')

if __name__ == '__main__':
    app.run(debug=True)
```