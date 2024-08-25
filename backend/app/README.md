# Ramped JobSearch APP Backend

## Setup

For working in the local development environment, clone the repository:

```sh
git clone https://github.com/Ramped-JS/backend.git
cd backend
```

Create and activate the virtual environment for Python:

#### Note: You must have the latest version of Python installed on your machine.

```sh
$ python3 -m venv venv
$ source venv/bin/activate
```

Add .env file to the root directory of your project and add these variables.

```sh
MONGO_DB_URI= <Your_Mongo_Atlas_URI>
MONGO_DB_DATABASE = <Your_MONGO_DB_DATABASE_NAME>
```

Install project dependencies or required modules:

```sh
pip3 install -r requirements.txt
```

Upload data to your MongoDB Atlas database by

```sh
python3 upload_data.py
```

This will create a collection named '_jobPosts' in the db.


Run the project using:

```sh
$ uvicorn main:app --reload
```

## API Documentation

You can access the API documentation using Swagger by navigating to:

http://127.0.0.1:8000/docs

This page provides detailed documentation for all the exposed API endpoints and their schemas.

In order to explore these endpoints, create a user by trying out the create user endpoint and providing your name, email, and username in the string format. Then, authorize with your email and password to test other endpoints.


## Code Structure and Documentation (FastAPI)

### Database:

1.  database.py file in the app folder, contains all the necessary configurations for database connections.
2.  MongoDB Atlas being used as the databases for the project.

### Routes

All the API routes can be found in the routes module in the JobSearch folder. For example, all the authentication-related API routes can be found in the authentication.py file.
