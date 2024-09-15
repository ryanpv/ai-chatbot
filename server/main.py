from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from functions.database import reset_messages, store_messages

# Module imports
from functions.openai_requests import convert_audio_to_text, get_chat_response
from functions.text_to_speech import convert_text_to_speech

app = FastAPI()

# CORS origins
origins = [
    "http://localhost:5173",
    "http://localhost:5174",
    "http://localhost:4173",
    "http://localhost:4174",
    "http://localhost:3000",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
async def check_health():
    return {"message": "Hello World"}


@app.post("/audio")
async def post_audio(file: UploadFile = File(...)):
    try:
        with open(file.filename, "wb") as buffer:
            buffer.write(file.file.read())
        audio_input = open(file.filename, "rb")

        message_decoded = convert_audio_to_text(audio_input)
        print("USER message Decoded: ", message_decoded)

        if not message_decoded:
            return HTTPException(status_code=400, detail="Failed to decode audio")

        chat_response = get_chat_response(message_decoded)

        if not chat_response:
            return HTTPException(status_code=400, detail="Failed to get chat response")
        print("CHAT RESPONSE", chat_response)

        store_messages(message_decoded, chat_response)

        audio_output = convert_text_to_speech(chat_response)

        if not audio_output:
            return HTTPException(
                status_code=400, detail="Failed to get Eleven Labs audio response"
            )

        def iterfile():
            yield audio_output

        return StreamingResponse(iterfile(), media_type="application/octet-stream")
    except Exception as e:
        print("GET_AUDIO ERROR: ", e)
        return {"message": "Error decoding audio"}


@app.get("/reset")
def reset_conversation():
    reset_messages()
    return {"message": "Conversation has been resetreset"}