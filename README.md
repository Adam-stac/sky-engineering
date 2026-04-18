# Sky Engineering - Teams Registry

A web application for SKY's Engineering Department to manage and visualise engineering teams, departments, and dependencies.

Built with Django, Python, SQLite and Bootstrap 5.

---

## Project Setup

### Prerequisites
- Python 3.13+
- Git
- VS Code (recommended)

### Step 1 - Clone the repository
Open a terminal and run:
```
git clone https://github.com/YOUR_ACTUAL_LINK_HERE.git
cd sky-engineering
```

### Step 2 - Open in VS Code
```
code .
```

### Step 3 - Create and activate virtual environment
```
python -m venv venv
venv\Scripts\activate
```
You should see (venv) at the start of your terminal line.

### Step 4 - Install dependencies
```
pip install -r requirements.txt
```

### Step 5 - Run migrations
```
python manage.py migrate
```

### Step 6 - Create your superuser (admin account)
```
python manage.py createsuperuser
```

### Step 7 - Run the server
```
python manage.py runserver
```

### Step 8 - Open your browser
```
http://127.0.0.1:8000
```

---

## Project Structure

```
sky-engineering/
├── core/           - Shared models, auth, dashboard (do not edit without discussing with team)
├── teams/          - Student 1 - Team management
├── organisation/   - Student 2 - Departments and org structure
├── messages_app/   - Student 3 - Messaging
├── schedule/       - Student 4 - Meeting scheduling
├── reports/        - Student 5 - Reports
├── static/css/     - Shared CSS files
├── templates/core/ - Shared base templates (do not edit without discussing with team)
├── requirements.txt
└── manage.py
```

---

## Branching Strategy

Each student has their own branch. You must only work on your own branch.

| Student | Branch | Feature |
|---------|--------|---------|
| Student 1 | student1-teams | Team management |
| Student 2 | student2-organisation | Departments and org structure |
| Student 3 | student3-messages | Messaging |
| Student 4 | student4-schedule | Meeting scheduling |
| Student 5 | student5-reports | Reports |

### Switching to your branch
Run this once when you first clone the repo - replace with your own branch name:
```
git checkout student1-teams
```

Check you are on the right branch before doing any work:
```
git branch
```
The branch with * next to it is your current branch.

---

## How to Commit Your Work

Every time you finish a piece of work, save it to Git using these 3 commands:

```
git add .
git commit -m "feat: description of what you did"
git push origin your-branch-name
```

### Commit message format
Always use this format so the history is clean and readable:

```
feat: added department list view
fix: fixed login redirect bug
style: updated sidebar colours
docs: updated README
```

### How often to commit
- After finishing a new page or view
- After fixing a bug
- After adding a new feature
- At the end of every work session

Do not go days without committing — small regular commits are better than one large one.

---

## Styling Guide - Please Read Carefully

The project uses two shared CSS files that control the look and feel of the entire application:

- static/css/style.css — controls the sidebar, dashboard, stat cards, tables and layout
- static/css/auth.css — controls the login and register pages only

### Rules for styling

- Do NOT edit static/css/auth.css under any circumstances — the login and register pages are complete and must stay consistent
- Do NOT edit static/css/style.css without discussing with the team first — changes here affect every page
- Do NOT add inline styles to your templates (no style="..." in HTML) — all CSS goes in a separate file
- For your own app, create your own CSS file at static/css/your_app_name.css and load it using the extra_css block in your templates like this:

```
{% block extra_css %}
<link href="{% static 'css/your_app_name.css' %}" rel="stylesheet">
{% endblock %}
```

- All your templates must extend core/base.html — this ensures the sidebar and layout are consistent across all pages
- Do NOT edit templates/core/base.html, templates/core/login.html, templates/core/register.html or templates/core/dashboard.html
- Use the existing CSS classes where possible (stat-card, page-title, page-sub, card, badge-status etc.) — check style.css before writing new styles
- Keep fonts, colours and spacing consistent with the rest of the app — use the same dark sidebar colour (#0f172a) and background (#f8fafc)

---

## Rules - Please Read

- Only work on your own branch
- Never push directly to main
- Never edit another student's app folder
- Do not edit core/ or templates/core/base.html without discussing with the team first
- Do not edit core/models.py without discussing with the team first - everyone depends on these models
- Do not touch static/css/auth.css or static/css/style.css without team agreement
- If you need to change a shared file, message the group first

---

## Merging Into Main

When your feature is complete and tested, tell the team. One person (Student 2 - Adam) will review and merge branches into main.

To merge your branch into main:
```
git checkout main
git merge student1-teams
git push origin main
git checkout student1-teams
```

---

## Tech Stack

- Backend: Django 6, Python 3.13
- Database: SQLite
- Frontend: Bootstrap 5, Bootstrap Icons
- Version Control: Git + GitHub
