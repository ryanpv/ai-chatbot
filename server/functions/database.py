import json
import random


# Get recent messges
def get_recent_messages():
    file_name = "stored_data.json"
    learn_instruction = {
        "role": "system",
        "content": "You are interviewing the user for a job as a retail assistant. Ask short questions that are relevant to the junior position. Your name is Jefferson. The user is called Ryan. Keep your answers under 30 seconds",
    }

    messages = []

    # Randomly include additional instructions/factors to the prompt
    x = random.uniform(0, 1)
    if x < 0.5:
        learn_instruction["content"] = (
            learn_instruction["content"] + " Your response will include some dry humor."
        )
    else:
        learn_instruction["content"] = (
            learn_instruction["content"] + " Your response will include some sarcasm."
        )

    messages.append(learn_instruction)

    try:
        with open(file_name) as user_file:
            data = json.load(user_file)

            if data:
                if len(data) < 5:
                    for item in data:
                        messages.append(item)
                else:
                    for item in data[-5]:
                        messages.append(item)
    except Exception as e:
        print(e)
        return {"message": "Error decoding audio"}

    return messages
