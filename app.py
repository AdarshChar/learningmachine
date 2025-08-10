from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_cors import CORS
import json
import os
from datetime import datetime
import markdown
import pygments
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

app = Flask(__name__)
CORS(app)

# Load lesson data
def load_lessons():
    with open('data/lessons.json', 'r') as f:
        return json.load(f)

def load_resources():
    with open('data/resources.json', 'r') as f:
        return json.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/lessons')
def lessons():
    lessons_data = load_lessons()
    return render_template('lessons.html', lessons=lessons_data)

@app.route('/lesson/<lesson_id>')
def lesson_detail(lesson_id):
    lessons_data = load_lessons()
    lesson = None
    for category in lessons_data['categories']:
        for l in category['lessons']:
            if l['id'] == lesson_id:
                lesson = l
                break
        if lesson:
            break
    
    if not lesson:
        return redirect(url_for('lessons'))
    
    return render_template('lesson_detail.html', lesson=lesson)

@app.route('/resources')
def resources():
    resources_data = load_resources()
    return render_template('resources.html', resources=resources_data)

@app.route('/practice')
def practice():
    return render_template('practice.html')

@app.route('/api/run_code', methods=['POST'])
def run_code():
    data = request.get_json()
    code = data.get('code', '')
    
    # This is a simplified version - in production you'd want proper sandboxing
    try:
        # Create a safe execution environment
        local_vars = {}
        exec(code, {"__builtins__": {}}, local_vars)
        return jsonify({"success": True, "output": str(local_vars.get('result', 'Code executed successfully'))})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

@app.route('/progress')
def progress():
    return render_template('progress.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)