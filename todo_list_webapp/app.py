from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Sample data storage (in-memory list)
tasks = []

@app.route('/')
def index():
    """Render the main index.html template."""
    return render_template('index.html')

@app.route('/api/tasks', methods=['POST'])
def add_task():
    """API endpoint to add a task."""
    data = request.json  # Assuming JSON data is sent
    if 'task' in data:
        task = data['task']
        tasks.append(task)
        return jsonify({'message': 'Task added successfully', 'task': task}), 201
    else:
        return jsonify({'error': 'Task not provided in request'}), 400



if __name__ == '__main__':
    app.run(debug=True)
