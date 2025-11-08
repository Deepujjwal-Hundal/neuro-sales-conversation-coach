def compute_engagement_score(transcript_segments):
    engagement_scores = []
    
    for segment in transcript_segments:
        tone_score = segment['tone_change'] * 0.5
        loudness_score = segment['loudness_dynamics'] * 0.3
        sentiment_score = segment['sentiment_polarity'] * 0.2
        
        engagement_score = tone_score + loudness_score + sentiment_score
        engagement_scores.append({
            'speaker': segment['speaker'],
            'text': segment['text'],
            'engagement_score': engagement_score
        })
    
    return engagement_scores

def calculate_rolling_engagement(engagement_scores, window_size=5):
    rolling_scores = []
    for i in range(len(engagement_scores)):
        start_index = max(0, i - window_size + 1)
        window = engagement_scores[start_index:i + 1]
        rolling_average = sum(score['engagement_score'] for score in window) / len(window)
        rolling_scores.append(rolling_average)
    
    return rolling_scores

def highlight_engagement_moments(engagement_scores, threshold=0.5):
    highlights = []
    for i, score in enumerate(engagement_scores):
        if score['engagement_score'] > threshold:
            highlights.append({
                'moment': 'Increased Interest',
                'speaker': score['speaker'],
                'text': score['text'],
                'engagement_score': score['engagement_score']
            })
        elif score['engagement_score'] < -threshold:
            highlights.append({
                'moment': 'Decreased Interest',
                'speaker': score['speaker'],
                'text': score['text'],
                'engagement_score': score['engagement_score']
            })
    
    return highlights