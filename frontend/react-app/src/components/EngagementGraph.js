import React from 'react';
import { Line } from 'react-chartjs-2';

const EngagementGraph = ({ engagementData }) => {
    const data = {
        labels: engagementData.map(segment => segment.time),
        datasets: [
            {
                label: 'Engagement Score',
                data: engagementData.map(segment => segment.score),
                fill: false,
                backgroundColor: 'rgba(75,192,192,0.4)',
                borderColor: 'rgba(75,192,192,1)',
                tension: 0.1,
            },
        ],
    };

    const options = {
        scales: {
            x: {
                title: {
                    display: true,
                    text: 'Time (seconds)',
                },
            },
            y: {
                title: {
                    display: true,
                    text: 'Engagement Score',
                },
                min: 0,
                max: 100,
            },
        },
    };

    return (
        <div>
            <h2>Engagement Over Time</h2>
            <Line data={data} options={options} />
        </div>
    );
};

export default EngagementGraph;