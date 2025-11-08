import React from 'react';

const Transcript = ({ transcriptData }) => {
    return (
        <div className="transcript-container">
            <h2>Transcript</h2>
            <ul>
                {transcriptData.map((segment, index) => (
                    <li key={index} style={{ color: segment.engagementScore > 0.5 ? 'green' : 'red' }}>
                        <strong>{segment.speaker}:</strong> {segment.text} <em>(Engagement Score: {segment.engagementScore.toFixed(2)})</em>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default Transcript;