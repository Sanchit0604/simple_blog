Simple Blog — Experiment 5
A simple blog platform built with Flask (Python) supporting full CRUD operations (Create, Read, Update, Delete) on blog posts stored in memory.
---
Project Structure
```
simple_blog/
├── app.py                  # Main Flask application
├── templates/
│   ├── base.html           # Base layout (navbar, footer)
│   ├── index.html          # Home page — lists all posts
│   ├── create.html         # Form to create a new post
│   └── edit.html           # Form to edit an existing post
├── static/
│   └── style.css           # Stylesheet
└── README.md
```
---
How to Run
1. (Optional) Create and activate a virtual environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```
2. Install Flask
```bash
pip install flask
```
3. Run the app
```bash
python app.py
```
4. Open in browser
Visit: http://127.0.0.1:5000
---
Features
Feature	Description
Create	Add new blog posts via a form
Read	View all posts on the home page
Update	Edit existing posts (pre-filled form)
Delete	Remove posts with a confirmation prompt
---
References
Flask Documentation
Jinja2 Templating
Google Fonts — Playfair Display & Source Sans 3
---
Academic Integrity
This project was written independently as part of Experiment 5.  
All code is original. External references are listed above.
