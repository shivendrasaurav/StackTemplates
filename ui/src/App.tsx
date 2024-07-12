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
