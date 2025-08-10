# Learning Machine - AI-Powered Learning Platform

A comprehensive web application for learning AI and machine learning concepts through interactive lessons, practice exercises, and real-time code execution.

## Features

- **Interactive Lessons**: Structured learning paths with detailed explanations
- **Real-time Code Execution**: Write and run Python code directly in the browser
- **Practice Exercises**: Hands-on coding challenges with instant feedback
- **Progress Tracking**: Monitor your learning journey with detailed analytics
- **Resource Library**: Curated collection of books, videos, articles, and tools
- **Modern UI**: Beautiful, responsive design built with Bootstrap 5

## Technology Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **Code Editor**: CodeMirror
- **Styling**: Font Awesome icons, custom CSS
- **Data**: JSON files for lessons and resources

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd learning-machine
   ```

2. **Create a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install Flask flask-cors markdown pygments
   ```

4. **Run the application**:
   ```bash
   python app.py
   ```

5. **Access the application**:
   Open your browser and navigate to `http://localhost:5001`

## Project Structure

```
learning-machine/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── templates/            # HTML templates
│   ├── index.html        # Homepage
│   ├── lessons.html      # Lessons listing
│   ├── lesson_detail.html # Individual lesson view
│   ├── resources.html    # Learning resources
│   ├── practice.html     # Code practice environment
│   └── progress.html     # Progress tracking
├── data/                 # Data files
│   ├── lessons.json      # Lesson content
│   └── resources.json    # Resource library
└── venv/                 # Virtual environment (created during setup)
```

## API Endpoints

- `GET /` - Homepage
- `GET /lessons` - List all lessons
- `GET /lesson/<lesson_id>` - Individual lesson details
- `GET /resources` - Learning resources
- `GET /practice` - Interactive code practice
- `GET /progress` - Learning progress tracking
- `POST /api/run_code` - Execute Python code

## Code Execution API

The `/api/run_code` endpoint allows safe execution of Python code:

```bash
curl -X POST http://localhost:5001/api/run_code \
  -H "Content-Type: application/json" \
  -d '{"code": "print(\"Hello, World!\")"}'
```

Response:
```json
{
  "success": true,
  "output": "Hello, World!\n"
}
```

## Features in Detail

### 1. Interactive Lessons
- Categorized learning paths (Python Basics, Data Structures, OOP, ML)
- Difficulty levels (Beginner, Intermediate, Advanced)
- Code examples with syntax highlighting
- Progress tracking per lesson

### 2. Practice Environment
- Real-time code editor with syntax highlighting
- Pre-built exercises and examples
- Instant code execution and feedback
- Error handling and debugging support

### 3. Progress Tracking
- Visual progress indicators
- Achievement system
- Learning streak tracking
- Detailed activity timeline

### 4. Resource Library
- Filterable by type (Books, Videos, Articles, Tools)
- Difficulty-based recommendations
- External links to learning materials

## Security Features

- Sandboxed code execution environment
- Restricted access to system functions
- Input validation and sanitization
- Safe built-in function access

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support and questions, please open an issue in the GitHub repository.

---

**Learning Machine** - Empowering learners to master AI and machine learning through interactive, hands-on experience.