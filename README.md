# engageEdu!

## YouTube Video Question Extractor

This project extracts questions from YouTube videos using transcription data and the power of OpenAI's GPT-4 model.

## Overview

YouTube videos often contain valuable information delivered through speech or text. Extracting questions from video transcripts can enhance comprehension and facilitate discussions or quizzes related to the video topics. This project automates the extraction of questions from YouTube video transcripts using publicly available APIs.

## Features

- Retrieves video transcript data from YouTube using the YouTube Data API.
- Utilizes OpenAI's GPT-4 model to process transcript data and generate responses.
- Parses the response to identify and extract questions embedded within the video.
- Saves the extracted questions in JSON format for further analysis or integration with other applications.

## Installation

1. Clone the repository to your local machine:
git clone https://github.com/Mattpdrexel/engageEdu.git

2. Install the required dependencies
pip install -r requirements.txt

3. Create a `.env` file in the project directory and add your API keys.

4. Run the `main.py` script to extract questions from a YouTube video:
python main.py


## Dependencies

- `youtube_transcript_api`: Fetches video transcript data from YouTube.
- `openai`: Accesses the GPT-4 model for generating responses.
- `python-dotenv`: Loads environment variables from a `.env` file.

## Usage

- Replace the `video_link_dict` variable with the URLs of the YouTube videos from which you want to extract questions.
- Customize the `extract_questions` function in the `question.py` file to suit your specific needs for question extraction.
- Adjust the `max_attempts` variable in the `main.py` file to control the maximum number of attempts to extract questions from the video transcript.

## Contributions

Contributions are welcome! Feel free to submit bug reports, feature requests, or pull requests to help improve this project.
