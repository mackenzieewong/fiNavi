import React, { useState } from 'react';
import './Style.css';

function InputField({ onSubmit }) { // Accept an onSubmit prop
  const [message, setMessage] = useState('');

  const handleMessageChange = (event) => {
    setMessage(event.target.value);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    onSubmit(message); // Call the passed onSubmit function with the message
  };

  return (
    <form onSubmit={handleSubmit}>
      <div className="input-container">
        <input
          type="text"
          value={message}
          onChange={handleMessageChange}
          placeholder="Type your message here..."
          className="input-field"
        />
        <button className="send-button" type="submit"></button>
      </div>
    </form>
  );
}

export default InputField;
