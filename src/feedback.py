```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/feedback.db'
db = SQLAlchemy(app)
ma = Marshmallow(app)

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)
    feedback = db.Column(db.String(500), nullable=False)

    def __init__(self, project_id, timestamp, feedback):
        self.project_id = project_id
        self.timestamp = timestamp
        self.feedback = feedback

class FeedbackSchema(ma.Schema):
    class Meta:
        fields = ('id', 'project_id', 'timestamp', 'feedback')

feedback_schema = FeedbackSchema()
feedbacks_schema = FeedbackSchema(many=True)

@app.route('/feedback', methods=['POST'])
def add_feedback():
    project_id = request.json['project_id']
    timestamp = request.json['timestamp']
    feedback = request.json['feedback']

    new_feedback = Feedback(project_id, timestamp, feedback)

    db.session.add(new_feedback)
    db.session.commit()

    return feedback_schema.jsonify(new_feedback)

@app.route('/feedback', methods=['GET'])
def get_feedback():
    all_feedback = Feedback.query.all()
    result = feedbacks_schema.dump(all_feedback)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
```