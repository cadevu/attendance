# Description
This application consists of a simple system in which the teacher will log in, create the class, and provide the code to their students, who will copy the code and fill out the attendance form, responding to the roll call.

# Install Dependencies
`poetry install`
# Start poetry virtual env
`poetry shell`
# Export flask path env
`export FLASK_APP=app/webapp.py`
# Create db
## Put your db credentials and app secret-key  in .env file and run

`flask shell`

`from app.webapp import app,db`

`from app.models import Aula, Professor`

`app.app_context().push()`

`db.create_all()`

`exit()`
# Run app
`flask run`
# Next steps
- Improve front-end (do it by myself)
- Add anti-fraud features
- Provide a csv file with students
