// Employee.js

import React, { useState, useEffect } from 'react';
import axios from 'axios';
import EmployeeForm from './EmployeeForm';
import ProjectAssignments from './ProjectAssignments';

function Employee() {
  const [assignments, setAssignments] = useState([]);
  const [creditScore, setCreditScore] = useState(0);

  useEffect(() => {
    // Fetch employee assignments and credit score from the server
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

  const handleTakeNewProject = async () => {
    try {
      // Implement functionality to allow the employee to take a new project
      // Make an API request to the server to assign a new project to the employee
      const response = await axios.post('http://your-flask-backend-url/take-new-project');
      // Handle the response or update the assignments state as needed
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div>
      <h1>Employee Page</h1>
      <ProjectAssignments assignments={assignments} onTakeNewProject={handleTakeNewProject} />
      <h2>Credit Score: {creditScore}</h2>
      <EmployeeForm />
    </div>
  );
}

export default Employee;
