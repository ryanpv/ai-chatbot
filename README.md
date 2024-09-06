# Voice Chatbot Project

## Overview

I created this project with the intended purpose of having a personalized chatbot assistant that I can have a conversation with.

This project is a chatbot that allows users to interact with it using their voice recordings and receive an audio response. The server handles the interaction by leveraging OpenAI's Whisper-1 model and Chat Completions API. The voice comes from Elevenlabs API, which has many other options for voices.

## Features
* Record audio of your voice
* Recieve audio response from server
* Replay chat recordings
* Store recent chat history 
* Clear entire chat history

## Technologies
These are the core technologies. You can view the rest in package.json / requirements.txt / requirements-dev.txt
### Frontend
* Typescript
* ReactJS / Vite
* React-media-recorder

### Backend
* FastAPI
* OpenAI
* Uvicorn

## Setup backend

Change directory to backend

```shell
cd server
```

### Setup python virtual environment

```shell
python3 -m venv venv
```

### Activate virtual environment (Windows)

```shell
source venv/bin/activate
```

### Activate virtual environment (Mac)

```shell
source venv/Scripts/activate
```

### Install python packages

```shell
pip3 install -r requirements.txt
```

### Create environment variables
Create a .env file at the root of the server directory. Replace "your_own_key" with your own actual keys.

```shell
ELEVEN_LABS_API_KEY=your_own_key
ELEVEN_LABS_VOICE_ID=your_own_key
OPENAI_API_KEY=your_own_key
OPENAI_ORG_ID=your_own_key
```

### Start the server

```shell
uvicorn main:app
```

To have server reset after each update, run this instead:

```shell
uvicorn main:app --reload
```

## Setup frontend

Change directory to the frontend. 

```shell
cd ..
cd client
```

### Install client-side packages

```shell
npm install
```

### Run the application
Application should be running on http://localhost:5173

```shell
npm run dev
```

See package.json for other available scripts.