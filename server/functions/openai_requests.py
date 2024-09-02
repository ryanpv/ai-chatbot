import openai
from decouple import config
from functions.database import get_recent_messages

# OpenAI API Keys
openai.organization = config("OPENAI_ORG_ID")
openai.api_key = config("OPENAI_API_KEY")


# OpenAI - Whisper
def convert_audio_to_text(audio_file):
    try:
        transcript = openai.Audio.transcribe("whisper-1", audio_file)
        message_text = transcript["text"]
        return message_text
    except Exception as e:
        print("CONVERT_AUDIO_TO_TEXT ERROR: ", e)
        return


# Openai - ChatGPT
def get_chat_response(message_input):
    messages = get_recent_messages()
    user_message = {"role": "user", "content": message_input}
    messages.append(user_message)

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
        )
        # Returned message from ChatGPT
        message_text = response["choices"][0]["message"]["content"]
        return message_text
    except Exception as e:
        print("GET_CHAT_RESPONSE ERROR: ", e)
        return {"message": "Error getting chat response"}