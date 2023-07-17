import subprocess
from flask import Flask, request, jsonify

app = Flask(__name__)

# Shared variables
testOutputs = {}

@app.route('/runTest', methods=['POST'])
def run_test():
    data = request.get_json()
    project_id = data['project_id']
    code = data['code']

    # Run the code and capture the output
    output = subprocess.check_output(["python", "-c", code])

    # Store the output
testOutputs[project_id] = output.decode('utf-8')

    return jsonify({'output': output.decode('utf-8')}), 200

@app.route('/getTestOutput', methods=['GET'])
def get_test_output():
    project_id = request.args.get('project_id')

    # Return the output of the test
    if project_id in testOutputs:
        return jsonify({'output': testOutputs[project_id]}), 200
    else:
        return jsonify({'error': 'No test output found for this project'}), 404

if __name__ == '__main__':
    app.run(port=5000, debug=True)