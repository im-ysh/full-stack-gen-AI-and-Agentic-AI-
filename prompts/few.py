from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key = "AIzaSyASrdibwDzsLV6TZCIs0tWCRA2lsbmsDhA",
    base_url = "https://generativelanguage.googleapis.com/v1beta/"
)

SYSTEM_PROMPT = """
You need to only coding related questions. Do not an anything else. Your name is alexa. If user asks smng other than coding just say sorry.

Rule : 
- Strictly follow the output in JSON format 

output format :
{{
"code": "string" or null,
"isCodingQuestion" : boolean
}}
Examples :
Q: Can you explain the a + b whole sq?
A: {{
"code": null,
"isCodingQuestion" : false
}}
Q: Hey write a python program for adding two numbers
A: {{
"code": "def add(a,b):
         return a + b",
"isCodingQuestion" : false
}}
"""

response = client.chat.completions.create(
    model = "gpt-4o-mini",
     messages = [
        {"role" : "system" , "content": SYSTEM_PROMPT},
        {"role": "user", "content": "hey write a code to add n numbers in js"}
    ]
)

print(response.choices[0].message.content)
# So few short prompting.

# Actually, the model is provided with a few examples before asking it to generate the response.

# In reality, in real world, few

# short prompting is used a lot.