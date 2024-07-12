import reactLogo from '../../assets/react.svg'
import viteLogo from '../../assets/vite.svg'

const Home = () => {

  return (
    <>
      <div>
        <a href="https://vitejs.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
        <a href="https://invrz.com" target="_blank">
          <img src='https://www.invrz.com/icon.png' className="logo" alt="Invrz logo" />
        </a>
      </div>
      <h1>Vite + React + Invrz</h1>
      <h2>React Router + Invrz Patterns Template</h2><br/><br/>
      <div className="card">
        <p>
          <strong>
            This is a simple example to get you started with React Router with Invrz Patterns. 
          </strong>
        </p>
        <p>
          In this example, you can see how different components are rendered based on the URL. The app uses <code>react-router-dom</code> to handle routing.
        </p>
        <p>
          Here’s a quick overview of how routing works in this app:
        </p><br/>
        <ul>
          <li><strong><code>path="/"</code></strong> renders the <code>Home</code> component. This is where you are now.</li>
          <li><strong><code>path="/counter"</code></strong> renders the <code>Counter</code> component.</li>
          <li><strong><code>path="/todos"</code></strong> renders the <code>TodoList</code> component.</li>
          <li><strong><code>path="/contact"</code></strong> renders the <code>ContactForm</code> component.</li>
          <li><strong><code>path="/quote/:index"</code></strong> renders the <code>QuoteGenerator</code> component, where <code>:index</code> is a dynamic parameter to select a specific quote.</li>
        </ul><br/>
        <p>
          To modify the routes or add new ones, you can update the <code>App.tsx</code> file.
        </p>
        <p><br/>
          <strong>How to Add a New Route:</strong>
        </p>
        <ol>
          <li>Create a new component for the page you want to add.</li>
          <li>Import the new component into <code>App.tsx</code>.</li>
          <li>Add a new <code>&lt;Route /&gt;</code> in the <code>&lt;Routes&gt;</code> component with the desired path and component.</li>
        </ol>
        <p>
          For example, to add a new "About" page, you would:
        </p>
        <pre>
          <code>
            {`
    import About from './routes/about/page';
    // Add this line in the <Routes> block
    <Route path="/about" element={<About />} />
            `}
          </code>
        </pre>
        <p>
          Feel free to explore the components and routes to get a better understanding of how they work together!
        </p><br/>
        <p>
          <strong>
            Patterns-UI is already installed when you bootstrap this project template. Visit <a href='https://patterns.invrz.com' target='_blank'>Invrz Patterns Docs</a> to learn more about how to use invrz patterns ui and grid in your react app.
          </strong>
        </p>
      </div><br/>
      <h3 className="read-the-docs">
        Click on the Vite, React and Invrz logos to learn more
      </h3>
    </>
  )
}

export default Home;
