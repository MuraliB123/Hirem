// Admin.js

import React, { useState } from 'react';
import axios from 'axios';

function Admin() {
  const [description, setDescription] = useState('');
  const [result, setResult] = useState('');

  const handleProjectSubmit = async () => {
    try {
      const response = await axios.post('http://your-flask-backend-url/', { description });
      setResult(response.data.ans);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div>
      <h1>Admin Page</h1>
      <label>Project Description</label>
      <input
        type="text"
        value={description}
        onChange={(e) => setDescription(e.target.value)}
      />
      <button onClick={handleProjectSubmit}>Submit Project</button>
      {result && <div>Result: {result}</div}
    </div>
  );
}

export default Admin;
