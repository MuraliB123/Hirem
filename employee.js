// Employee.js

import React, { useState, useEffect } from 'react';
import axios from 'axios';

function Employee() {
  const [assignments, setAssignments] = useState([]);
  const [creditScore, setCreditScore] = useState(0);

  // Fetch and set employee assignments and credit score
  useEffect(() => {
    async function fetchData() {
      try {
        const response = await axios.get('http://your-flask-backend-url/employee-data');
        setAssignments(response.data.assignments);
        setCreditScore(response.data.creditScore);
      } catch (error) {
        console.error(error);
      }
    }

    fetchData();
  }, []);

  return (
    <div>
      <h1>Employee Page</h1>
      <h2>Assignments</h2>
      <ul>
        {assignments.map((assignment, index) => (
          <li key={index}>{assignment}</li>
        ))}
      </ul>
      <h2>Credit Score: {creditScore}</h2>
    </div>
  );
}

export default Employee;
