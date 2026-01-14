# News Capstone — Django Application

This repository contains my **Django News Application Capstone Project**, completed as part of the HyperionDev Software Engineering programme.

The goal of this project was not only to build a working Django application, but also to demonstrate professional development practices such as:

- Version control with Git and GitHub  
- Writing clear, maintainable code  
- Generating developer documentation using Sphinx  
- Containerising an application using Docker  

This repository is intended to form part of my **developer portfolio**.

---

## Project Overview

The News Application allows different user roles (Readers, Journalists, Editors) to interact with news articles in a structured workflow.

It demonstrates key Django concepts such as:

- Custom user models  
- Role-based permissions  
- Model relationships  
- API endpoints  
- Clean project structure  

---

## Running the Project Locally (Virtual Environment)

These steps assume you have **Python 3.10+** installed.

1. Clone the repository
bash
git clone https://github.com/Tumik27/news-capstone-consolidation.git
cd news-capstone-consolidation/news_capstone

2. Create and activate a virtual environment

Windows

python -m venv venv
venv\Scripts\activate


macOS / Linux

python3 -m venv venv
source venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

4. Configure environment variables

Create a file named .env in the project root and add:

SECRET_KEY=your-secret-key
DEBUG=True
DB_NAME=db.sqlite3

5. Run database migrations
python manage.py migrate

6. Create a superuser (admin account)
python manage.py createsuperuser

7. Start the development server
python manage.py runserver


Open:

http://127.0.0.1:8000/

Documentation (Sphinx)

Developer documentation is generated using Sphinx and is located in the docs/ directory.

To generate the HTML documentation:

cd docs
make html


Then open:

docs/_build/html/index.html

Docker (Optional)

If you prefer to run the project with Docker:

docker build -t news-capstone .
docker run -p 8000:8000 news-capstone


After you paste this and click **Commit changes**, send me a screenshot of the commit message section only, and I’ll give you the next single step.

