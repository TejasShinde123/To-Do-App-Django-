# Django Todo Application

## Project Overview
This is a simple Todo application built using Django, providing user authentication and task management functionality.

## Features
- User Registration and Authentication
- Create, Read, Update, and Delete (CRUD) Todo Tasks
- Task Status Tracking
- User-specific Todo Lists

## Prerequisites
- Python 3.8+
- Django 3.2+
- pip (Python Package Manager)

## Installation

### 1. Clone the Repository
```bash
git clone <your-repository-url>
cd todo-project
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 3. Install Dependencies
```bash
pip install django
```

### 4. Database Setup
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser (Optional)
```bash
python manage.py createsuperuser
```

### 6. Run the Development Server
```bash
python manage.py runserver
```

## Project Structure
```
todo_project/
│
├── todo/
│   ├── models.py       # Database models
│   ├── views.py        # View functions
│   └── templates/      # HTML templates
│
├── manage.py           # Django project management script
└── README.md           # Project documentation
```

## Models
### TODOO Model
The application uses a `TODOO` model with the following fields:
- `srno`: Auto-incrementing primary key
- `title`: Task title (max 100 characters)
- `description`: Task description (max 1000 characters)
- `date`: Timestamp of task creation
- `user`: Foreign key to Django's User model
- `due_date`: Optional task due date
- `status`: Task status (Open, Working, Pending Review, Completed, Overdue, Cancelled)
- `tag`: Optional task tag

## Authentication Routes
- `/signup`: User registration
- `/login`: User login
- `/signout`: User logout

## Todo Routes
- `/todopage`: View and create todos
- `/edit_todo/<task_id>`: Edit a specific todo
- `/delete_todo/<task_id>`: Delete a specific todo

## Status Choices
Todo tasks can have the following statuses:
- Open
- Working
- Pending Review
- Completed
- Overdue
- Cancelled

## Security Notes
- User authentication is required to access todo features
- Each user can only view and modify their own todos

## Potential Improvements
- Add task priority
- Implement task filtering and searching
- Create more advanced status management
- Add task reminders and notifications

## Troubleshooting
- Ensure all dependencies are installed
- Check database migrations
- Verify user authentication settings

## License
[Specify your license here, e.g., MIT, Apache 2.0]

## Contributing
Please read CONTRIBUTING.md for details on our code of conduct and the process for submitting pull requests.
