import requests

video_link_dict = {
    "main": "https://www.youtube.com/watch?v=kzJZWO21PVw&t",
    "main_short": "https://www.youtube.com/shorts/vfbIOZgTers",
    "low_quality": "https://www.youtube.com/watch?v=u3wxPCWcDiA&t",
    "anqie": "https://www.youtube.com/watch?v=Se5WXQ9Hqhw"
}

url = "http://127.0.0.1:8000/generate_questions/"

for video_name, video_link in video_link_dict.items():
    params = {"video_link": video_link}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        questions = response.json()
        assert len(questions) == 4, f"Test failed for {video_name}: Expected 4 questions, but got {len(questions)}"
        print(f"Test passed for {video_name}: Found 4 questions")
    else:
        print(f"Failed to generate questions for {video_name}. Status code:", response.status_code)
