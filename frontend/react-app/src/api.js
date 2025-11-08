import axios from 'axios';

// Use relative URL when served from same origin, or absolute URL for development
const API_BASE_URL = process.env.REACT_APP_API_URL || window.location.origin;

export const uploadAudio = async (audioFile) => {
    const formData = new FormData();
    formData.append('file', audioFile); // Changed from 'audio' to 'file' to match backend

    try {
        const response = await axios.post(`${API_BASE_URL}/api/upload`, formData, {
            headers: {
                'Content-Type': 'multipart/form-data',
            },
            timeout: 300000, // 5 minutes timeout for large video files
        });
        return response.data;
    } catch (error) {
        console.error('Error uploading audio:', error);
        if (error.response) {
            // Server responded with error
            throw new Error(error.response.data?.error || `Server error: ${error.response.status}`);
        } else if (error.request) {
            // Request made but no response
            throw new Error('Network error: Could not reach the server. Make sure the Flask server is running.');
        } else {
            // Something else happened
            throw new Error(error.message || 'An unexpected error occurred');
        }
    }
};

export const getTranscript = async (callId) => {
    try {
        const response = await axios.get(`${API_BASE_URL}/transcript/${callId}`);
        return response.data;
    } catch (error) {
        console.error('Error fetching transcript:', error);
        throw error;
    }
};

export const getEngagementData = async (callId) => {
    try {
        const response = await axios.get(`${API_BASE_URL}/engagement/${callId}`);
        return response.data;
    } catch (error) {
        console.error('Error fetching engagement data:', error);
        throw error;
    }
};

export const getSuggestions = async (callId) => {
    try {
        const response = await axios.get(`${API_BASE_URL}/suggestions/${callId}`);
        return response.data;
    } catch (error) {
        console.error('Error fetching suggestions:', error);
        throw error;
    }
};