# youtube_api.py
import re


def extract_video_id(youtube_link):
    pattern = r"(?:https?:\/\/)?(?:www\.)?(?:youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|\S*?[?&]v=)|youtu\.be\/|youtube\.com\/shorts\/)([a-zA-Z0-9_-]{11})"
    match = re.match(pattern, youtube_link)
    if match:
        return match.group(1)
    else:
        return None
    
# Other related functions...
