# Sky Engineering - Teams Registry

A web application for SKY's Engineering Department to manage and visualise engineering teams, departments, and dependencies.

Built with Django, Python, SQLite and Bootstrap 5.

## Project Setup

### Prerequisites
- Python 3.13+
- Git

### Installation

1. Clone the repository
   git clone https://github.com/Adam-stac/sky-engineering.git
   cd sky-engineering

2. Create and activate virtual environment
   python -m venv venv
   venv\Scripts\activate

3. Install dependencies
   pip install -r requirements.txt

4. Run migrations
   python manage.py migrate

5. Create a superuser (admin account)
   python manage.py createsuperuser

6. Run the server
   python manage.py runserver

7. Open your browser at http://127.0.0.1:8000

## Project Structure

sky-engineering/
├── core/           - Shared models, auth, dashboard
├── teams/          - Student 1 - Team management
├── organisation/   - Student 2 - Departments and org structure
├── messages_app/   - Student 3 - Messaging
├── schedule/       - Student 4 - Meeting scheduling
├── reports/        - Student 5 - Reports
├── static/css/     - Shared CSS files
├── templates/      - Shared base templates
└── manage.py

## Branching Strategy

Each student works on their own branch:
- student1-teams
- student2-organisation
- student3-messages
- student4-schedule
- student5-reports

## Tech Stack

- Backend: Django 6, Python 3.13
- Database: SQLite
- Frontend: Bootstrap 5, Bootstrap Icons
- Version Control: Git + GitHub