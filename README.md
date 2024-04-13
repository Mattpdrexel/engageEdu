# engageEdu!

## YouTube Transcription Question Extractor

This project utilizes transcription data from YouTube videos and leverages OpenAI's GPT-4 model to extract questions from the video content.

## Overview

YouTube videos often contain valuable information presented in spoken or written form. Extracting questions from video transcripts can aid in understanding the content and facilitating discussions or quizzes related to the video topics. This project aims to automate the extraction of questions from YouTube video transcripts using advanced natural language processing techniques.

## Features

- Extracts video transcript data from YouTube using the YouTube Data API.
- Utilizes OpenAI's GPT-4 model to process the transcript data and generate responses.
- Parses the response to identify and extract questions posed within the video.
- Saves the extracted questions in JSON format for further analysis or integration with other applications.

## Installation

1. Clone the repository to your local machine:
git clone https://github.com/your-username/your-repository.git

2. Install the required dependencies:
pip install -r requirements.txt
3. Create a `.env` file in the project directory and add your API keys:

4. Run the `main.py` script to extract questions from a YouTube video:
python main.py


## Dependencies

- `youtube_transcript_api`: Used to fetch video transcript data from YouTube.
- `openai`: Provides access to the GPT-4 model for generating responses.
- `python-dotenv`: Enables loading environment variables from a `.env` file.

## Usage

- Replace the `video_link_dict` variable with the URLs of the YouTube videos you want to extract questions from.
- Customize the `extract_questions` function in the `question.py` file to suit your specific needs for question extraction.
- Adjust the `max_attempts` variable in the `main.py` file to control the maximum number of attempts to extract questions from the video transcript.

## Contributions

Contributions are welcome! Feel free to submit bug reports, feature requests, or pull requests to help improve this project.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
