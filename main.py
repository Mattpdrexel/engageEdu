import json
from youtube_api import extract_video_id
from youtube_transcript import get_video_transcript
from openai_client import generate_response
from question import extract_questions

# Test links
video_link_dict = {"main": "https://www.youtube.com/watch?v=kzJZWO21PVw&t",
                   "main_short": "https://www.youtube.com/shorts/vfbIOZgTers",
                   "low_quality": "https://www.youtube.com/watch?v=u3wxPCWcDiA&t",
                   "anqie": "https://www.youtube.com/watch?v=Se5WXQ9Hqhw"}

# Extract video ID from link
video_id = extract_video_id(video_link_dict["main"])

# Fetch video transcript
video_transcript_data = get_video_transcript(video_id)

# Create loop to try to extract data up to 3 times
max_attempts = 3
attempts = 0
questions = []

while attempts < max_attempts:
    # Generate response
    response = generate_response(video_transcript_data)
    print(response)

    response_text = response.choices[0].message.content

    # Parse response and create Question objects
    questions = extract_questions(response_text)

    # If questions are not empty, break out of the loop
    if questions:
        break

    # Increment attempts counter
    attempts += 1

# Check if questions are still empty after maximum attempts
if not questions:
    print("Failed to extract questions after maximum attempts.")
else:
    # Convert questions to JSON format
    questions_json = [question.__dict__ for question in questions]

    # Write JSON data to a file
    with open("questions.json", "w") as json_file:
        json.dump(questions_json, json_file)

# https://www.youtube.com/embed/kzJZWO21PVw?si=AzdRtmBvEaKhqt_W