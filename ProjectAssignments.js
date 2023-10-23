// ProjectAssignments.js

import React from 'react';

function ProjectAssignments({ assignments, onTakeNewProject }) {
  return (
    <div>
      <h2>Assignments</h2>
      <ul>
        {assignments.map((assignment, index) => (
          <li key={index}>{assignment}</li>
        ))}
      </ul>
      <button onClick={onTakeNewProject}>Take New Project</button>
    </div>
  );
}

export default ProjectAssignments;
