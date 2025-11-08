from pyannote.audio import Pipeline

def diarize_audio(file_path):
    # Load the pre-trained speaker diarization pipeline
    pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization")

    # Apply the pipeline to the audio file
    diarization = pipeline(file_path)

    # Prepare the results
    segments = []
    for turn, _, speaker in diarization.itertracks(yield_label=True):
        segments.append({
            "start": turn.start,
            "end": turn.end,
            "speaker": speaker
        })

    return segments