# dating_app

## Description
This is a dating app built with Django and Django Rest Framework.

# My app is :core 
# My project is:dating_app


## Prerequisites
- Python 3.8+
- pip
- virtualenv

## Technical Specifications
- Python version: 3.11.5 
- Django version: 5.1.1
- Django Rest Framework version: 3.15.2
- Pillow version: 10.4.0

## Installation
1. Ensure you have Python 3.8 or higher installed. You can check your Python version with:
   ```
   python --version
   ```

2. Clone the repository:
   ```
   git clone https://github.com/yourusername/dating-app.git
   cd dating_app
   ```

3. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

5. Set up the database:
   ```
   python manage.py migrate
   ```

6. Create a superuser (optional):
   ```
   python manage.py createsuperuser
   ```

7. Run the development server:
   ```
   python manage.py runserver
   ```

## Usage
- Access the admin interface at `http://localhost:8000/admin/`
- API endpoints can be found at `http://localhost:8000/api/`


## API Documentation
API documentation is available at `http://localhost:8000/swagger/` when the server is running.



