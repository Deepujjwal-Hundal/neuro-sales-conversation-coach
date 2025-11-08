from transformers import pipeline

def analyze_sentiment(transcript):
    sentiment_pipeline = pipeline("sentiment-analysis")
    results = sentiment_pipeline(transcript)
    return results

def extract_sentiment_scores(transcript_segments):
    sentiment_scores = []
    for segment in transcript_segments:
        sentiment_result = analyze_sentiment(segment['text'])
        sentiment_scores.append({
            'speaker': segment['speaker'],
            'text': segment['text'],
            'label': sentiment_result[0]['label'],
            'score': sentiment_result[0]['score']
        })
    return sentiment_scores