from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key = "AIzaSyASrdibwDzsLV6TZCIs0tWCRA2lsbmsDhA",
    base_url = "https://generativelanguage.googleapis.com/v1beta/"
)

response = client.chat.completions.create(
    model = "gemini-2.5-flash",
    messages = [
        {"role" : "system" , "content": "You are an expert in maths and only and only ans amths related questions.If the query is not related to maths.Just say sorry and do not answer that"},
        {"role": "user", "content": "hey there. can you code a python program that can print hello"}
    ]
)

print(response.choices[0].message.content)
