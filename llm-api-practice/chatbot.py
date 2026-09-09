from google import genai
from dotenv import load_dotenv
from google.genai.errors import ServerError

import time

import os

load_dotenv()

client = genai.Client(
    api_key = os.getenv("GEMINI_API_KEY")
)


while True:

    user_msg = input("You: ")

    if user_msg.lower().strip() == 'exit':
        break

    start = time.time()
    try: 
        response = client.models.generate_content(
            model="gemini-flash-latest",
            contents=user_msg
        )
    except ServerError:
        print("AI: Model server is busy. Please try again in few movements.")
        
    end = time.time()

    print("Time: ", round(end - start, 2), "seconds")
    print("AI: " + response.text)