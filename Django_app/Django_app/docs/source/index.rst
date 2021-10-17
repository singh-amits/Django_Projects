===========================================
Welcome to Django-Quiz-App's documentation!
===========================================
----------------------------------
A configurable quiz app in django
----------------------------------

Features
=================
* User registration and login.
* OTP verification at registration.
* Timer for each quiz.
* Storing of quiz results under each user.
* Previous quiz scores, and answers can be viewed.
* Registered users can return to an incomplete quiz to finish it.
* Each quiz is limited to one attempt per user.
* Questions can be given a category.
* Multiple choice question type.
* One word answer question type.

Installation
=================
1. Clone the repository
::
   git clone https://github.com/humshubham/django-quiz-app.git

2. Change to project directory, create and activate a virtual environment
::
   virtualenv venv
   source venv/bin/activate

3. Install requirements
::
   pip install -r requirements.txt

Usage
=================
1. Create a superuser account
::
   python manage.py createsuperuser

2. Apply migrations
::
   python manage.py makemigrations
   python manage.py migrate

2. Start the server
::
   python manage.py runserver



