from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key = "AIzaSyASrdibwDzsLV6TZCIs0tWCRA2lsbmsDhA",
    base_url = "https://generativelanguage.googleapis.com/v1beta/"
)

SYSTEM_PROMPT = "You need to anser only coding related question or else strictly say sorry. you are alexa."

response = client.chat.completions.create(
    model = "gemini-2.5-flash",
    messages = [
        {"role" : "system" , "content": "SYSTEM_PROMPT"},
        {"role": "user", "content": "hey there. can you code a python program that can print hello"}
    ]
)

print(response.choices[0].message.content)
