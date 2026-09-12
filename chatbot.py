from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("ERROR: GEMINI_API_KEY was not found")
    exit()

client = genai.Client(api_key=api_key)

chat = client.chats.create(model = "gemini-3.6-flash")

 
while True:
    question = input("\nYou: ")

    if question.lower() == "quit":
        print("Goodbye!")
        break

    # response = client.models.generate_content(
    #     model="gemini-3.6-flash",
    #     contents=question
    #     # Every request is basically independent
    # )
    response = chat.send_message(question)

    print("\nAI:")
    print(response.text)