import json
import random


# Get recent messges
def get_recent_messages():
    file_name = "stored_data.json"
    learn_instruction = {
        "role": "system",
        "content": (
            "You are interviewing the user for a job as a software developer. "
            "Ask short questions that are relevant to the junior position. "
            "Your name is Jefferson. The user is called Ryan. Keep your answers under 30 seconds"
        ),
    }

    messages = []

    # Randomly include additional instructions/factors to the prompt
    x = random.uniform(0, 1)
    if x < 0.5:
        learn_instruction["content"] = (
            learn_instruction["content"] + " Your response will include some attitude."
        )
    else:
        learn_instruction["content"] = (
            learn_instruction["content"]
            + " Your response will include some dry humour."
        )
    messages.append(learn_instruction)

    try:
        with open(file_name) as user_file:
            data = json.load(user_file)

            # Use last 5 messages for most recent context
            if data:
                if len(data) < 5:
                    for item in data:
                        messages.append(item)
                else:
                    for item in data[-5]:
                        messages.append(item)
    except Exception as e:
        print("GET_RECENT_MESSAGES ERROR: ", e)
        return {"message": "Error decoding audio"}

    return messages


# Store messages
def store_messages(request_message, response_message):
    file_name = "stored_data.json"

    # exclude initial prompt from get_recent_messages
    messages = get_recent_messages()[1:]

    user_message = {"role": "user", "content": request_message}
    assistance_message = {"role": "assistant", "content": response_message}

    messages.append(user_message)
    messages.append(assistance_message)

    with open(file_name, "w") as f:
        json.dump(messages, f)


# Clear stored messages
def reset_messages():
    with open("stored_data.json", "w") as file:
        file.write("[]")