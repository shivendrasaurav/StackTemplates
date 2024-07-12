import { useParams, useNavigate } from 'react-router-dom';

const quotes = [
  "The only limit to our realization of tomorrow is our doubts of today.",
  "The best way to predict the future is to invent it.",
  "Do not wait to strike till the iron is hot, but make it hot by striking.",
  "Success usually comes to those who are too busy to be looking for it.",
  "You miss 100% of the shots you don’t take.",
];

const QuoteGenerator = () => {
  const { index } = useParams<{ index: string }>();
  const quoteIndex = parseInt(index || '0', 10);
  const navigate = useNavigate();

  const showNextQuote = () => {
    const nextIndex = (quoteIndex + 1) % quotes.length;
    navigate(`/quote/${nextIndex}`);
  };

  const showPreviousQuote = () => {
    const prevIndex = (quoteIndex - 1 + quotes.length) % quotes.length;
    navigate(`/quote/${prevIndex}`);
  };

  const quote = quotes[quoteIndex] || "Quote not found.";

  return (
    <div>
      <h2>Quote Generator</h2>
      <p>{quote}</p>
      <button onClick={showPreviousQuote}>Previous Quote</button>
      <button onClick={showNextQuote}>Next Quote</button>
    </div>
  );
};

export default QuoteGenerator;
