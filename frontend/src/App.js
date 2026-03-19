import React, { useState } from "react";
import axios from "axios";

function App() {
  const [question, setQuestion] = useState("");
  const [data, setData] = useState(null);

  const askQuestion = async () => {
    const res = await axios.post("http://127.0.0.1:8000/ask", {
      question: question,
    });
    setData(res.data);
  };

  return (
    <div style={{ padding: "20px" }}>
      <h2>Text to SQL App</h2>

      <input
        type="text"
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        placeholder="Ask your question..."
        style={{ width: "400px" }}
      />

      <button onClick={askQuestion}>Ask</button>

      {data && (
        <div>
          <h3>SQL</h3>
          <pre>{data.sql}</pre>

          <h3>Result</h3>
          <pre>{JSON.stringify(data.result, null, 2)}</pre>

          <h3>Explanation</h3>
          <p>{data.explanation}</p>
        </div>
      )}
    </div>
  );
}

export default App;