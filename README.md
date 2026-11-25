# Mavi

**Project under development**

Mavi is a voice assistant written in Python. It listens to what you say, asks Groq, and speaks the answer out loud.

## How it works

1. Your speech is converted to text by Google's speech recognition.
2. The text is sent to Groq, which answers (it can search the internet).
3. The answer is cleaned and read out loud with a Portuguese (Brazil) Windows voice.

Everything you say is sent to Google, and the question is sent to Groq, so an internet connection is required.

## Setup

1. Install Python 3.13.
2. Install the dependencies: `pip install -r requirements.txt`
3. Create a `.env` file with two variables:
   - `GROQ_API_KEY`: your Groq API key.
   - `regras`: the rules the assistant follows when answering (for example: short answers, in Brazilian Portuguese, as if reading out loud).
4. Make sure a Portuguese (Brazil) voice, such as Microsoft Maria, is installed in Windows.

## Run
