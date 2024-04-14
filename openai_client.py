# openai_client.py
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

def generate_response(video_transcript_data):
    client = OpenAI(api_key=openai_api_key)

    # Test if number of token is too high
    print(len(video_transcript_data))


    messages = [
    {
        "role": "user",
        "content": f"Read this video transcript. Provide timestamp and duration where poll questions are asked. The response should always be EXACTLY in this format: Question_Number: Question Number (Question_1, Question_2, etc.): Timestamp: inferred_timestamp, Duration: inferred_duration, Question: inferred_question, Question_type: inferred_question_type (Poll or Open), Options: extracted_options (in a list like ['A', 'B', 'C', ...])}}. Ensure questions and options are punctuated properly and make grammatical sense, even if transcription isn't perfect: {video_transcript_data}"
    }
    ]


    response = client.chat.completions.create(
    model="gpt-4",
    temperature=0,
    messages = messages)
    return response


# Other related functions...
