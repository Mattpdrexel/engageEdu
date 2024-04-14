# engageEdu

# Inspiration
* Virtual lectures are an essential part of modern education, growing in use significantly since the pandemic (ref. 1)
* However, it's clear from both the academic research and personal anecdote that pure online lectures are not ideal for learning
* This is primarily due to the passive nature of consuming online lectures, which is not as effective as active learning (ref. 2)
* hat if we could make online lectures more engaging, improving student retention and providing valuable statistics for curriculum analysis?

# What it does
* The concept is simple: insert automated prompts for student engagement on online lectures.
* During a recorded lecture, our application, engageEdu, consumes the video transcript data and automatically translates questions the presenter asks during the lecture into interactive prompts
* For example, when a presenter asks in the middle of a lecture "Poll: Which country has the second largest population in the world? China, India, the United States or Brazil," engageEdu detects this prompt and provides it as an interactive question for the students, allowing them to engage actively with the material.

# How we built it
* For proof of concept, we have focused on development using youtube videos as a source of video content
* Youtube automatically transcribes these videos, with the transcription text available for consumption using YouTubeTranscriptApi
* This data is then fed to openai to parse the data, detecting the specific questions as they appear in the video
* This data is ultimately packaged into a json file with a list of questions, each with a timestamp, duration, and list of poll options (if applicable)
* This output is produced on demand for any given youtube video, and integrated into our frontend to display the questions as they are mentioned during the video
* These questions prompt a user for a response (either select from a list of options or enter into text box)
* This response data is then stored in our database for later evaluation / statistical analysis

# Challenges we ran into
* Audio transcription
    * Automated youtube transcriptions of video text are good, but not perfect
    * While perfect for clear indoor audio, some transcription errors occured with audio recorded outside and with a non-native speaker's pronunciation
    * While not perfect, translation was >90% accurate even in these circumstances 
* Prompt Engineering
    * Engineering the appropriate prompts for openai to provide consistent responses was challenging, and took many iterations
    * This was eventually resolved by reducing temperature of the chatbot, and specifying the desired output format in exact detail
* Transcipt Length Limitations
    * We also encountered limitations in the gpt-4 model context window, which cannot accept a large input of text
    * This can easily be resolved in the future by splitting the video transcript data into smaller chunks, and then handling each section in sequence before being reintegrated

# Accomplishments that we're proud of
* The backend tool was successfully tested on 4 separate youtube videos of variable length, audio quality, and user speaking styles
* For each video, each question was detected and appropriately captured by our program, summarizing with the question, the list of presented options (if any) and accurate timestamp/duration


# What we learned
* AI solutions are remarkable, but not perfect. 
* Care must be taken in how to utilize these tools in any application. 

# What's next for Engage Edu
* We intend to expand the tool beyond Youtube videos, applying to essentially any online lecture content (i.e., Canvas)
* This would require addressing additional technical questions, such as expanding the video duration that can be analyzed and buidling partnerships with academic institutions to test and refine our application further

# Built With
* YouTubeTranscriptApi: https://pypi.org/project/youtube-transcript-api/ 
* openai API: https://openai.com/blog/openai-api
* Flask: https://flask.palletsprojects.com/en/3.0.x/
* Postgresql: https://www.postgresql.org/


# References
1. With Online Learning, ‘Let’s Take a Breath and See What Worked and Didn’t Work’: 
https://www.nytimes.com/2022/10/06/education/learning/online-learning-higher-education.html
2. Measuring actual learning versus feeling of learning in response to being actively engaged in the classroom: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6765278/