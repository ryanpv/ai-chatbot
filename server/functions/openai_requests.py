import openai
from decouple import config

openai.organization = config("OPENAI_ORG_ID")
openai.api_key = config("OPENAI_API_KEY")


# OpenAI - Whisper
def convert_audio_to_text(audio_file):
    try:
        transcript = openai.Audio.transcribe("whisper-1", audio_file)
        message_text = transcript["text"]
        return message_text
    except Exception as e:
        print(e)
        return
