django-notes-management
Django Notes Management App  This is a Django application that allows users to create, read, update, and delete personal notes. Each user can only access their own notes, and the notes are paginated, displaying 10 notes per page.  ## Features  - User authentication (signup, login, logout) - CRUD operations for notes .
Clone the repository 
git clone https://github.com/TusharChautala/django-notes-management.git
cd django-notes-management
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
http://127.0.0.1:8000/admin/
http://127.0.0.1:8000/notes/
