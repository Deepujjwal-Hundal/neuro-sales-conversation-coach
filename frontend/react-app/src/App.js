import React, { useState } from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import UploadPage from './components/UploadPage';
import ResultsPage from './components/ResultsPage';
import './styles.css';

function App() {
    const [audioFile, setAudioFile] = useState(null);
    const [transcriptData, setTranscriptData] = useState(null);

    const handleFileUpload = (file) => {
        setAudioFile(file);
    };

    const handleTranscriptData = (data) => {
        setTranscriptData(data);
    };

    return (
        <Router>
            <Switch>
                <Route path="/" exact>
                    <UploadPage onFileUpload={handleFileUpload} />
                </Route>
                <Route path="/results">
                    <ResultsPage 
                        audioFile={audioFile} 
                        transcriptData={transcriptData} 
                        onTranscriptData={handleTranscriptData} 
                    />
                </Route>
            </Switch>
        </Router>
    );
}

export default App;