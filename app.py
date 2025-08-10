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
        # Create a safe execution environment with basic builtins
        safe_builtins = {
            '__builtins__': {
                'print': print,
                'len': len,
                'range': range,
                'str': str,
                'int': int,
                'float': float,
                'list': list,
                'dict': dict,
                'set': set,
                'tuple': tuple,
                'bool': bool,
                'type': type,
                'isinstance': isinstance,
                'abs': abs,
                'min': min,
                'max': max,
                'sum': sum,
                'sorted': sorted,
                'reversed': reversed,
                'enumerate': enumerate,
                'zip': zip,
                'map': map,
                'filter': filter,
                'round': round,
                'pow': pow,
                'divmod': divmod,
                'bin': bin,
                'hex': hex,
                'oct': oct,
                'ord': ord,
                'chr': chr,
                'hash': hash,
                'id': id,
                'dir': dir,
                'vars': vars,
                'getattr': getattr,
                'hasattr': hasattr,
                'setattr': setattr,
                'delattr': delattr,
                'property': property,
                'super': super,
                'object': object,
                'Exception': Exception,
                'ValueError': ValueError,
                'TypeError': TypeError,
                'IndexError': IndexError,
                'KeyError': KeyError,
                'AttributeError': AttributeError,
                'NameError': NameError,
                'ZeroDivisionError': ZeroDivisionError,
                'OverflowError': OverflowError,
                'MemoryError': MemoryError,
                'RecursionError': RecursionError,
                'StopIteration': StopIteration,
                'GeneratorExit': GeneratorExit,
                'SystemExit': SystemExit,
                'KeyboardInterrupt': KeyboardInterrupt,
                'EOFError': EOFError,
                'ImportError': ImportError,
                'ModuleNotFoundError': ModuleNotFoundError,
                'OSError': OSError,
                'FileNotFoundError': FileNotFoundError,
                'PermissionError': PermissionError,
                'ProcessLookupError': ProcessLookupError,
                'TimeoutError': TimeoutError,
                'ConnectionError': ConnectionError,
                'BrokenPipeError': BrokenPipeError,
                'ConnectionAbortedError': ConnectionAbortedError,
                'ConnectionRefusedError': ConnectionRefusedError,
                'ConnectionResetError': ConnectionResetError,
                'BlockingIOError': BlockingIOError,
                'ChildProcessError': ChildProcessError,
                'FileExistsError': FileExistsError,
                'InterruptedError': InterruptedError,
                'IsADirectoryError': IsADirectoryError,
                'NotADirectoryError': NotADirectoryError,
                'BufferError': BufferError,
                'ArithmeticError': ArithmeticError,
                'FloatingPointError': FloatingPointError,
                'AssertionError': AssertionError,
                'LookupError': LookupError,
                'UnboundLocalError': UnboundLocalError,
                'ReferenceError': ReferenceError,
                'RuntimeError': RuntimeError,
                'NotImplementedError': NotImplementedError,
                'SyntaxError': SyntaxError,
                'IndentationError': IndentationError,
                'TabError': TabError,
                'SystemError': SystemError,
                'UnicodeError': UnicodeError,
                'UnicodeDecodeError': UnicodeDecodeError,
                'UnicodeEncodeError': UnicodeEncodeError,
                'UnicodeTranslateError': UnicodeTranslateError,
                'Warning': Warning,
                'UserWarning': UserWarning,
                'DeprecationWarning': DeprecationWarning,
                'PendingDeprecationWarning': PendingDeprecationWarning,
                'SyntaxWarning': SyntaxWarning,
                'RuntimeWarning': RuntimeWarning,
                'FutureWarning': FutureWarning,
                'ImportWarning': ImportWarning,
                'UnicodeWarning': UnicodeWarning,
                'BytesWarning': BytesWarning,
                'ResourceWarning': ResourceWarning,
                'None': None,
                'True': True,
                'False': False,
                'Ellipsis': Ellipsis,
                'NotImplemented': NotImplemented,
            }
        }
        
        # Capture stdout to get print output
        import io
        import sys
        from contextlib import redirect_stdout
        
        output = io.StringIO()
        with redirect_stdout(output):
            exec(code, safe_builtins, {})
        
        result = output.getvalue()
        return jsonify({"success": True, "output": result if result else "Code executed successfully"})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

@app.route('/progress')
def progress():
    return render_template('progress.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)