from fastapi import FastAPI
from openai import BadRequestError

app = FastAPI()

@app.get("/generate_questions/")
async def generate_questions(video_link: str):
    import json
    from youtube_api import extract_video_id
    from youtube_transcript import get_video_transcript
    from openai_client import generate_response
    from question import extract_questions

    try:
        # Extract video ID from link
        video_id = extract_video_id(video_link)

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
            return {"message": "Failed to extract questions after maximum attempts."}
        else:
            # Convert questions to JSON format
            questions_json = [question.__dict__ for question in questions]

            return questions_json

    except BadRequestError:
        return {"message": "Error: Input size is too large. This code is still in development and not intended for long lectures yet. Video size should be restricted for 5-10min for testing."}
