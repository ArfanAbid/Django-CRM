# CRM App with Django, Python, and MySQL.

A Customer Relationship Management (CRM) application developed using Django, Python, MySQL. This application facilitates user registration, authentication, and CRUD (Create, Read, Update, Delete) operations on records.

## Features

- **User Authentication:** Allows users to register, log in, and log out securely.
- **Record Management:** Perform CRUD operations to manage customer records efficiently.
- **Database:** Utilizes MySQL as the primary database.

## Installation

### Prerequisites

- Python [Install Python](https://www.python.org/downloads/)
- Django (install using pip): `pip install django`

1. Clone the repository:

   ```bash
   git clone https://github.com/ArfanAbid/Django-CRM.git

2. Navigate to project directory:
    `cd core`
   
3. Create and activate Virtual Environment:
   `python -m venv venv` then
   `.\venv\Scripts\activate`
4. Set up MySQL:

   - Create a MySQL database named "my_database".
   - Update the database configuration in settings.py with your MySQL credentials:

```
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'my_database',   # Name database according to your choice
        'USER': 'root',
        'PASSWORD': ' ', #you set while Settingup MySQL
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

```

5. Run Data base migrations:
   `python manage.py migrate`

6. Create a superuser (admin account) to access the Django admin panel:
   `python manage.py createsuperuser`

7. Run the development server:
   `python manage.py runserver`

8. Access the development server at  `http://127.0.0.1:8000/`

## Usage:

- Register: Create a new user account.
- Log In: Enter your credentials to access the CRM functionality.
- Add Records: Create new customer records.
- View Records: Browse and search through existing customer records.
- Update Records: Modify customer information as needed.
- Delete Records: Remove customer records from the database.

## Contributing:

Contributions are welcome! Fork the repository, make your changes, and submit a pull request explaining the improvements or additions you've made.