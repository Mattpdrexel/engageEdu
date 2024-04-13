# youtube_transcript.py
from youtube_transcript_api import YouTubeTranscriptApi 

def get_video_transcript(video_id):
    # Your get_video_transcript function code here...
    return YouTubeTranscriptApi.get_transcript(video_id)
# Other related functions...
