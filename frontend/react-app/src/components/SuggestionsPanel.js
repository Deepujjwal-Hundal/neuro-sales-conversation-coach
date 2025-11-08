import React from 'react';

const SuggestionsPanel = ({ suggestions }) => {
    return (
        <div className="suggestions-panel">
            <h2>Suggestions for Improvement</h2>
            <ul>
                {suggestions.map((suggestion, index) => (
                    <li key={index}>{suggestion}</li>
                ))}
            </ul>
        </div>
    );
};

export default SuggestionsPanel;