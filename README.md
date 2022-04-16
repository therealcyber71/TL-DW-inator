# 🧪The TLDW-inator (Too Long; Didn't Watch)

"Perry the Platypus, behold my new evil scheme, the TLDW-inator!" \
Tired of watching long videos just to grasp a concept? Or maybe you aren't that much of a visual learner, here's an awesome tool that you can use for free. Read on to learn more.

## 🤓 Detailed explanation for nerds

The TLDW-inator is a light weight Desktop app for students or researchers to understand the content of a video in a few words. 

### >How is this done?
All you have to do is enter a YouTube video link whose content you want to understand. 
Now simply wait for a few minutes as the program understands the audio in the file using the [Deepgram API](https://deepgram.com/) and then shortens it using the [NLTK Package](https://www.nltk.org/). Hence, using Deepgrams advanced AI speech recognition and NLTKs data summarization model the whole video is summarized in a few sentences or words.

### >Limitations
1. Videos that are too small can't be summarized, because of the API rnot catching those words (latency).
2. Local files arent supported, this feature will be added ASAP, couldn't be added due to the time limitation.
3. Cannot be used as a Binary (Due to the Hackathon being held for less than 24 hours, I didn't have the time to build a binary, but it's on the roadmap.)

### >Other Technical Details
1. Programming Language used: [Python 3.9](https://www.python.org/)
2. GUI designing and programming done using [PySimpleGUI](https://pysimplegui.readthedocs.io/) and [PyAutoGUI](https://pyautogui.readthedocs.io/)
3. Audio Speech Recognition done using [Deepgram Python SDK](https://deepgram.com/)
4. Natural Language Processing and Text Summarization done using [NLTK](https://www.nltk.org/) and [Pysummarization](https://pypi.org/project/pysummarization/)
5. Source code and Docs Hosted on [GitHub](https://github.com/)


## ⚙️Installation and Usage
### >Steps for installation and usage:
1. Install the Source Code from the [Official GitHub page]()
2. Enter the API keys in the `db.txt` file from the [deepgram](https://deepgram.com/) website.
3. The GUI will now appear, enter the YouTube link .
4. Wait for sometime (a few seconds approximately) and your video transcript plus video summary will be ready.

### >Links to get the API keys:
1. [Deepgram](https://console.deepgram.com/signup)

### >What to do with the API key
Step 1. Make a `.txt` file called `db.txt` in the same location as the App (binary or script file).
Step 2. Enter the key in the first line in the text file and close it.
Step 3. You're good to go!!

### >Installation video
[YouTube video](https://youtu.be/pA92zUpsCmM) \
Click on the image (can't believe I'm saying this) \
[![Watch the video](https://raw.githubusercontent.com/therealcyber71/Sonoma-Hackathon-2.0/main/download%20(1).png?token=GHSAT0AAAAAABTUGXKRE5YAVS2HB6QXSX56YS3J3ZA)](https://youtu.be/pA92zUpsCmM)


## ❤️ Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
