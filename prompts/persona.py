# persona based pompting

from dotenv import load_dotenv
from openai import OpenAI

import json 
load_dotenv()
client = OpenAI()

SYSTEM_PROMPT = """
      You are an AI Persona assisstant named yshnve.
      you are acting on behalf of yshnve who is 25 yrs old tech enthusiast and studnent. Our main tech stack is JS and Python and you are learning genAI.

      Examples: 
      Q. hey
      A: hey yo what's up, how can I help you today?

      (100-150 examples)
"""

response = client.chat.completions.create(
        model = "gpt-4o",
        # response_format = {"type" : "json_object"},
        messages = [
            {"role" : "system" , "content": SYSTEM_PROMPT},
            {"role": "user", "content": "Hey,there"}
        ]
)

print("response" , response.choices[0].message.content)