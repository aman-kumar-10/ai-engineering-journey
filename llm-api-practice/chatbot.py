from google import genai
from dotenv import load_dotenv
from google.genai.errors import ServerError

import time

import os

load_dotenv()

client = genai.Client(
    api_key = os.getenv("GEMINI_API_KEY")
)

history = []

while True:

    user_msg = input("You: ")

    if user_msg.lower().strip() == 'exit':
        break

    # append message history
    history.append(
        {
            "role": "user",
            "parts": [{"text": user_msg}]
        }
    )

    start = time.time()
    try: 
        response = client.models.generate_content(
            model="gemini-flash-latest",
            contents=history
        )
    except ServerError:
        print("AI: Model server is busy. Please try again in few movements.")
        continue
        
    end = time.time()

    # append response
    history.append(
        {
            "role": "model",
            "parts": [{"text": response.text}]
        }
    )

    print("Time: ", round(end - start, 2), "seconds")
    print("AI: " + response.text)