# question.py
import re

class Question:
    def __init__(self, index, timestamp, duration, question, question_type, options):
        self.index = index
        self.timestamp = timestamp
        self.duration = duration
        self.question = question
        self.question_type = question_type
        self.options = options
    
    def __repr__(self):
        return f"{self.index}"



def extract_questions(response_text):
    # Define a regex pattern to match each question block
    pattern = r"Question_Number: (Question_\d+), Timestamp: ([\d.]+), Duration: ([\d.]+), Question: (.+?), Question_type: (\w+), Options: \[(.*?)\]"

    # Use findall to extract all matches
    matches = re.findall(pattern, response_text, re.DOTALL)

    # Initialize an empty list to store Question objects
    question_objects = []

    # Iterate through matches and create Question objects
    for match in matches:
        index = match[0]
        timestamp = float(match[1])
        duration = float(match[2])
        question = match[3]
        question_type = match[4]
        options = [opt.strip().strip("'") for opt in match[5].split(",")] if match[5] else []
        question_objects.append(Question(index, timestamp, duration, question, question_type, options))
    return question_objects
