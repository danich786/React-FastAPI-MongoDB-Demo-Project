# Demo Project with Next.js Frontend, FastAPI backend, and MongoDB database


## Setup

For working in the local development environment, clone the repository:

```sh
git clone https://github.com/danich786/React-FastAPI-MongoDB-Demo-Project.git
```

# For_Frontend

```sh
cd frontend
```

Install the project dependencies:

```sh
npm install
```

Start a local server:

```sh
npm run dev
```

## Code Quality (React)

### Linting and Formatting:

1.  Configure ESLint with a popular style guide (e.g., Airbnb) for JavaScript.
2.  Use Prettier for code formatting with a pre-commit hook to enforce style consistency.

### Component Structure:

1. Functional Components: Always use functional components over class components to leverage hooks.
2. Single Responsibility: Each component should focus on a single functionality.

### File Naming:

1. Use PascalCase for component files (e.g., ReservationCard.js).
2. Use camelCase for non-component files (e.g., useFetch.js).

### Hooks:

1. Follow the rules of hooks (only call hooks at the top level and from React functions).
2. For side effects needing cleanup, ensure the return of a cleanup function in useEffect.

### CSS and Styling:

1. CSS and Styling Guidelines will be updated soon


# For Backend

```sh
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
