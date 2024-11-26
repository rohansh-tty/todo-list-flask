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

## Running the App
1. Set the Flask app environment variable:
```
export FLASK_APP=app
```
2. Run the development server:
```
flask run
```
3. Run Celery Worker:
```
celery -A app.celery_obj worker --loglevel=INFO -E
```
4. Start Redis Docker Container
```
docker run -d -p 6379:6379
```
5. Open your web browser and visit `http://localhost:5000` to access the TODO list app.

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
    ├── extensions/
        ├── _init_.py
    └── resources/
        ├── _init_.py
        ├── todo.py
    └── tests
        ├── _init_.py
        ├── conftest.py
        └── test_app.py
```