# Ramped_JS_Frontend

## Setup

For working in the local development environment, clone the repository:

```sh
git clone https://github.com/Ramped-JS/frontend.git
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
