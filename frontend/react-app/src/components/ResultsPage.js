import React from 'react';
import Transcript from './Transcript';
import EngagementGraph from './EngagementGraph';
import SuggestionsPanel from './SuggestionsPanel';

const ResultsPage = ({ transcriptData, engagementData, suggestions }) => {
    return (
        <div className="results-page">
            <h1>Sales Call Analysis Results</h1>
            <Transcript transcriptData={transcriptData} />
            <EngagementGraph engagementData={engagementData} />
            <SuggestionsPanel suggestions={suggestions} />
        </div>
    );
};

export default ResultsPage;