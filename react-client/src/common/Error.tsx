import React from 'react';

interface ErrorProps {
  errors: { error_code: string; error_details: string }[];
}

const Error: React.FC<ErrorProps> = ({ errors }) => {
  return (
    <div className="alert alert-danger">
      <strong>Error:</strong>
      <ul>
        {errors.map((error, index) => (
          <li key={index}>
            {error.error_code}: {error.error_details}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Error;
