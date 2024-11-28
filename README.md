# Todo-List

## Prerequisites
- Python 3.x installed
- (Optional) A virtual environment set up

## Installation
1. Clone the repository:
```
git clone https://github.com/your-username/todo-list-flask.git
```
2. Navigate to the project directory:
```
cd todo-list-flask
```
3. (Optional) Create and activate a virtual environment:
```
python -m venv venv
source venv/bin/activate 
```
4. Install the required dependencies:
```
pip install -r requirements.txt
```
5. Create .env file and these keys 
```
SECRET_KEY=your-secret-key-here

# Mongo Configuration
DB_USER=
DB_PASSWORD=
DB_NAME= 
DB_COLLECTION=
DEV_DB_URI=
PROD_DB_URI=

# Flask Configuration
FLASK_APP=wsgi.py
FLASK_ENV=development
CONFIG=dev
```
## Running the App

1. Run the development server:
```
flask --debug run
```
2. Run Celery Worker:
```
celery -A app.celery_obj worker --loglevel=INFO -E
```
3. Start Redis Docker Container
```
docker run -d -p 6379:6379
```
4. Open your web browser and visit `http://localhost:5000` to access the TODO list app.

## Testing
To run the test suite:
```
pytest -v
```

## Folder Structure
The project has the following folder structure:
```
TODO-LIST-FLASK/
├── wsgi.py
├── requirements.txt
├── .gitignore
├── app/
    |── config.py
    |── __init__.py
    ├── db/
        ├── _init_.py
        ├── connection.py
        ├── module.py
        ├── schema.py
    ├── services/
        ├── _init_.py
    └── resources/
        ├── _init_.py
        ├── todo.py
    └── utils/
        ├── _init_.py
        ├── feature_flag.py
    └── tests
        ├── _init_.py
        ├── conftest.py
        └── test_app.py
```