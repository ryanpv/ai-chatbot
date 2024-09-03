import requests
from decouple import config

ELEVEN_LABS_API_KEY = config("ELEVEN_LABS_API_KEY")


# Text to Speech
def convert_text_to_speech(message):
    body = {"text": message, "voice_settings": {"stability": 0, "similarity_boost": 0}}

    voice_id_charlotte = "XB0fDUnXU5powFXDhCwa"

    headers = {
        "xi-api-key": ELEVEN_LABS_API_KEY,
        "Content-Type": "application/json",
        "accept": "audio/mpeg",
    }
    endpoint = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id_charlotte}"

    try:
        response = requests.post(endpoint, json=body, headers=headers)
    except Exception as e:
        print("CONVERT_TEXT_TO_SPEECH ERROR: ", e)
        return {"message": "Error converting text to speech"}

    if response.status_code == 200:
        return response.content
    else:
        print("ERROR GETTING RESPONSE FOR TEXT-TO-SPEECH CONVERSION", response)
        return
