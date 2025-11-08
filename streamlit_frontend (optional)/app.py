from streamlit import st
import requests

# Streamlit app for Neuro-Sales Conversation Coach
st.title("Neuro-Sales Conversation Coach")

# Page 1: Upload audio file
st.header("Upload Audio File")
uploaded_file = st.file_uploader("Choose a WAV or MP3 file", type=["wav", "mp3"])

if uploaded_file is not None:
    st.audio(uploaded_file, format='audio/wav')
    
    # Send the audio file to the backend for processing
    files = {'file': uploaded_file.getvalue()}
    response = requests.post("http://localhost:5000/api/analyze", files=files)
    
    if response.status_code == 200:
        data = response.json()
        
        # Page 2: Show transcript and engagement visualization
        st.header("Analysis Results")
        
        # Display transcript
        st.subheader("Transcript")
        st.write(data['transcript'])
        
        # Display engagement graph
        st.subheader("Engagement Over Time")
        st.line_chart(data['engagement_scores'])
        
        # Display suggestions
        st.subheader("Suggestions for Improvement")
        for suggestion in data['suggestions']:
            st.write(f"- {suggestion}")
    else:
        st.error("Error processing the audio file.")