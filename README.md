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

1. **Clone the Repository**

   Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/vite-react-invrz-template.git
   cd vite-react-invrz-template
   ```

2. **Install Dependencies**

   Run the following command to install all necessary dependencies:

   ```bash
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

   Open your browser and navigate to `http://localhost:3000` to see the application in action.

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

### Adding a New Route

To add a new route, follow these steps:

1. **Create a New Component**

   Add a new component in the `routes` directory.

2. **Import the Component**

   Import the new component into `App.tsx`:

   ```tsx
   import NewPage from './routes/newpage/page';
   ```

3. **A. Add the Route**

   Add a new `<Route />` element in the `Routes` block of `App.tsx`:

   ```tsx
   <Route path="/newpage" element={<NewPage />} />
   ```

   For example, to add an "About" page:

   ```tsx
   import About from './routes/about/page';
   // Add this line in the <Routes> block
   <Route path="/about" element={<About />} />
   ```
   ```

4. **B. Or Modify a Route**

   Replace any `<Route />` element in the `Routes` block of `App.tsx`:

   ```tsx
   <Route path="/newpage" element={<NewPage />} />
   ```

   For example, to replace the "Counter" with "About" page:

   ```tsx
   - import Counter from './routes/counter/page';
   + import About from './routes/about/page';
     // Change this line in the <Routes> block
   - <Route path="/counter" element={<Counter />} />
   + <Route path="/about" element={<About />} />
   ```
   If you haven't worked with diff before, in the above example, "-" represents lines of code which existed earlier, whilst "+" represent the code which replaces earlier code.

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