import React, { useState, useRef } from 'react';
import { useHistory } from 'react-router-dom';
import { uploadAudio } from '../api';

const UploadPage = ({ onFileUpload, onTranscriptData }) => {
    const [selectedFile, setSelectedFile] = useState(null);
    const [uploading, setUploading] = useState(false);
    const [error, setError] = useState(null);
    const [filePreview, setFilePreview] = useState(null);
    const fileInputRef = useRef(null);
    const history = useHistory();

    const handleFileChange = (event) => {
        const file = event.target.files[0];
        if (file) {
            setSelectedFile(file);
            setError(null);
            
            // Create preview for video files
            if (file.type.startsWith('video/')) {
                const videoUrl = URL.createObjectURL(file);
                setFilePreview({ type: 'video', url: videoUrl });
            } else if (file.type.startsWith('audio/')) {
                const audioUrl = URL.createObjectURL(file);
                setFilePreview({ type: 'audio', url: audioUrl });
            } else {
                setFilePreview(null);
            }
        }
    };

    const handleDragOver = (e) => {
        e.preventDefault();
        e.stopPropagation();
    };

    const handleDrop = (e) => {
        e.preventDefault();
        e.stopPropagation();
        
        const file = e.dataTransfer.files[0];
        if (file) {
            // Check if it's a video or audio file
            if (file.type.startsWith('video/') || file.type.startsWith('audio/') || 
                /\.(mp4|avi|mov|mkv|flv|wmv|webm|m4v|3gp|wav|mp3|m4a|ogg)$/i.test(file.name)) {
                setSelectedFile(file);
                setError(null);
                
                if (file.type.startsWith('video/')) {
                    const videoUrl = URL.createObjectURL(file);
                    setFilePreview({ type: 'video', url: videoUrl });
                } else if (file.type.startsWith('audio/')) {
                    const audioUrl = URL.createObjectURL(file);
                    setFilePreview({ type: 'audio', url: audioUrl });
                }
            } else {
                setError('Please select a video or audio file.');
            }
        }
    };

    const handleUpload = async () => {
        if (!selectedFile) {
            setError('Please select a video or audio file to upload.');
            return;
        }

        setUploading(true);
        setError(null);

        try {
            const response = await uploadAudio(selectedFile);
            
            if (onFileUpload) {
                onFileUpload(selectedFile);
            }
            
            if (onTranscriptData) {
                onTranscriptData(response);
            }
            
            // Navigate to results page
            history.push('/results');
        } catch (err) {
            // Extract error message from the error object
            const errorMessage = err.message || err.response?.data?.error || 'Failed to upload and process file.';
            setError(errorMessage);
            console.error('Upload error:', err);
        } finally {
            setUploading(false);
        }
    };

    const handleClearFile = () => {
        setSelectedFile(null);
        setFilePreview(null);
        if (fileInputRef.current) {
            fileInputRef.current.value = '';
        }
    };

    const formatFileSize = (bytes) => {
        if (bytes === 0) return '0 Bytes';
        const k = 1024;
        const sizes = ['Bytes', 'KB', 'MB', 'GB'];
        const i = Math.floor(Math.log(bytes) / Math.log(k));
        return Math.round(bytes / Math.pow(k, i) * 100) / 100 + ' ' + sizes[i];
    };

    return (
        <div className="upload-page">
            <div className="upload-container">
                <h1>Upload Sales Call</h1>
                <p className="subtitle">Choose a video or audio file from your device</p>
                
                <div 
                    className="file-drop-zone"
                    onDragOver={handleDragOver}
                    onDrop={handleDrop}
                    onClick={() => fileInputRef.current?.click()}
                >
                    {filePreview ? (
                        <div className="file-preview">
                            {filePreview.type === 'video' ? (
                                <video 
                                    src={filePreview.url} 
                                    controls 
                                    style={{ maxWidth: '100%', maxHeight: '300px' }}
                                    onClick={(e) => e.stopPropagation()}
                                />
                            ) : (
                                <audio 
                                    src={filePreview.url} 
                                    controls 
                                    style={{ width: '100%' }}
                                    onClick={(e) => e.stopPropagation()}
                                />
                            )}
                            <div className="file-info">
                                <p><strong>{selectedFile.name}</strong></p>
                                <p>{formatFileSize(selectedFile.size)}</p>
                            </div>
                            <button 
                                className="clear-button"
                                onClick={(e) => {
                                    e.stopPropagation();
                                    handleClearFile();
                                }}
                            >
                                Remove File
                            </button>
                        </div>
                    ) : (
                        <div className="drop-zone-content">
                            <div className="upload-icon">📁</div>
                            <p className="drop-text">Drag & drop your file here</p>
                            <p className="or-text">or</p>
                            <button className="browse-button">Browse Files</button>
                            <p className="file-types">Supports: MP4, AVI, MOV, MKV, WAV, MP3, and more</p>
                        </div>
                    )}
                </div>

                <input
                    ref={fileInputRef}
                    type="file"
                    accept="video/*,audio/*,.mp4,.avi,.mov,.mkv,.flv,.wmv,.webm,.m4v,.3gp,.wav,.mp3,.m4a,.ogg"
                    onChange={handleFileChange}
                    style={{ display: 'none' }}
                />

                {selectedFile && (
                    <button 
                        className="upload-button" 
                        onClick={handleUpload} 
                        disabled={uploading}
                    >
                        {uploading ? (
                            <>
                                <span className="spinner"></span>
                                Processing...
                            </>
                        ) : (
                            'Analyze File'
                        )}
                    </button>
                )}

                {error && (
                    <div className="error-message">
                        <span>⚠️</span>
                        <p>{error}</p>
                    </div>
                )}
            </div>
        </div>
    );
};

export default UploadPage;