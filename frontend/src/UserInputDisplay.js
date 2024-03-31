import React, { useState } from 'react';
import './Style.css';
import InputField from './InputField';

function UserInputDisplay() {
  const [displayedValue, setDisplayedValue] = useState('');

  // Function to fetch response from the Flask API
  const fetchResponse = async (message) => {
    try {
      const response = await fetch('http://localhost:5000/send_message', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ "prompt": message }),
      });
      const data = await response.json();
      console.log(response);
      if (response.ok) {
        setDisplayedValue(data.response);
      } else {
        // Handle server errors or no prompt provided
        console.error(data.error);
        setDisplayedValue(data.error);
      }
    } catch (error) {
      // Handle network errors
      console.error('Network error:', error);
      setDisplayedValue('Failed to fetch data. Check console for more details.');
    }
  };

  const handleSubmit = (submittedMessage) => {
    fetchResponse(submittedMessage);
  };

  // Static user image URL
  const userImage = 'User Profile Photo.png';

  return (
    <div className="user-input-display-container">
      <div className="input-with-image-container">
        <InputField onSubmit={handleSubmit} />
        <img src={userImage} alt="User Profile" className="user-image" />
      </div>
      {displayedValue && (
        <div className="displayed-value-container">
          <p>{displayedValue}</p>
        </div>
      )}
    </div>
  );
}

export default UserInputDisplay;
