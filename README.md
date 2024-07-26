# Stack templates for popular stacks
### Add this git repo as remote and pull branchName to pull stack template. Here's a list of templates added:

- `react-w-router` - to pull template for React with Vite app initialized with React Router and Patterns UI by Invrz
- `fastapi-postgres` - to pull template for FastAPI initialized with Router and a Microservice with PostgreSQL Connection.
# Vite + React + Invrz Template

## Introduction

Welcome to the **Vite + React + Invrz** project template! 🎉 This template is designed to help you quickly get started with a new React application using Vite as the build tool and Invrz Patterns for UI components and design.

This project includes a basic setup with React Router for routing and a few example components to demonstrate how to structure your app and add new pages.

## Project Overview

In this template, you will find an example of how to use `react-router-dom` for routing and how to integrate Invrz Patterns into your React application.

### Key Features

- **React Router v7** for client-side routing
- **Invrz Patterns UI** for modern and responsive design components
- Example components including a counter, contact form, and quote generator

## Getting Started

### Prerequisites

Before you start, make sure you have the following installed:

- [Node.js](https://nodejs.org/) (v14 or later)
- [npm](https://www.npmjs.com/) or [Yarn](https://yarnpkg.com/) for package management

### Installation

1. **Fetch the template from Repository**

   Follow these `git` commands to setup your project with this template:

   a. Create a folder for your project and navigate into it:
   ```bash
   mkdir {projectName}
   cd {projectName}
   ```

   b. Initialize Git and add template as remote: 
   ```bash
   git init
   git remote add template https://github.com/shivendrasaurav/StackTemplates.git
   ```

   c. Fetch the template and pull the latest code from the `react-w-router` branch:
   ```bash
   git fetch template
   git pull template react-w-router
   ```

   \* You can pull other branches to get different templates. Check out [Invrz Templates](https://github.com/) to know more.

   d. Remove the template remote and add your own project's remote with a suitable remote name:
   ```bash
   git remote remove template
   git remote add {remoteName} {gitURL}
   ```


2. **Install Dependencies**

   Navigate to the `ui` folder where the `react-w-router` code resides, and then install the packages using `npm` or `yarn`, or any other package manager you prefer:

   ```bash
   cd ui

   npm install
   # or
   yarn install
   ```

3. **Start the Development Server**

   Start the Vite development server:

   ```bash
   npm run dev
   # or
   yarn dev
   ```

   Open your browser and navigate to `http://localhost:5173`(default) to see the application in action.

## Project Structure

Here's an overview of the project structure:

```
/src
  /assets
    react.svg
    vite.svg
  /routes
    /_home
      page.tsx
    /contact
      page.tsx
    /counter
      page.tsx
    /quotes
      page.tsx
    /todo
      page.tsx
  App.tsx
  App.css
  index.css
  main.tsx
  other react files
```

### Components

- **`Home`**: Welcome page and introduction to the template
- **`Counter`**: Simple counter example component
- **`ContactForm`**: Contact form with a basic `handleSubmit` function
- **`QuoteGenerator`**: Component that displays quotes based on the URL parameter
- **`TodoList`**: Basic todo list example

### Routes

The `App.tsx` file configures the routes for the application:

```tsx
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Counter from './routes/counter/page';
import ContactForm from './routes/contact/page';
import QuoteGenerator from './routes/quotes/page';
import TodoList from './routes/todo/page';
import Home from './routes/_home/page';

import "./App.css";
import "patterns-ui/styles/main.css";

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/counter" element={<Counter />} />
        <Route path="/todos" element={<TodoList />} />
        <Route path="/contact" element={<ContactForm />} />
        <Route path="/quote/:index" element={<QuoteGenerator />} />
      </Routes>
    </Router>
  );
};

export default App;
```

- **`/`**: Renders the `Home` component
- **`/counter`**: Renders the `Counter` component
- **`/todos`**: Renders the `TodoList` component
- **`/contact`**: Renders the `ContactForm` component
- **`/quote/:index`**: Renders the `QuoteGenerator` component with a dynamic `:index` parameter

### Adding/Modifying a New/Existing Route

To add a new route or modify existing route, follow these steps:

1. **Create a New Component**

   Add a new component in the `routes` directory.

2. **Import the Component**

   Import the new component into `App.tsx`:

   ```tsx
   import NewComponent from './routes/newpage/page';
   ```

3. **Add or Modify a Route**

   * **To add a new Route**: Add a new `<Route />` element in the `Routes` block of `App.tsx`:

        ```tsx
        <Route path="/newroute" element={<NewComponent />} />
        ```

        For example, to add an "About" page:

        ```tsx
        + import About from './routes/about/page';
          // Add this line in the <Routes> block
        + <Route path="/about" element={<About />} />
        ```

    * **To Modify an Existing Route**: Replace any `<Route />` element in the `Routes` block of `App.tsx`:

        ```tsx
        <Route path="/modifiedroute" element={<NewComponent />} />
        ```

        For example, to replace the "Counter" with "About" page:

        ```tsx
        - import Counter from './routes/counter/page';
        + import About from './routes/about/page';
            // Change this line in the <Routes> block
        - <Route path="/counter" element={<Counter />} />
        + <Route path="/about" element={<About />} />
        ```
        
   \* If you haven't worked with diff before, in the above example, "-" represents lines of code which existed earlier, whilst "+" represents the new or modified code.

## Links

- [Vite Documentation](https://vitejs.dev/)
- [React Documentation](https://react.dev/)
- [Invrz Patterns Documentation](https://patterns.invrz.com/)
- [React Router Documentation](https://reactrouter.com/)

## Contributing

If you have suggestions for improvements or find issues, feel free to open an issue or submit a pull request!

## License

This project is licensed under the [MIT License](LICENSE).

---

This `README.md` provides a comprehensive guide for users to understand the purpose of the project, how to get started, and how to modify the routes. It also includes links to relevant resources for Vite, React, and Invrz Patterns.
