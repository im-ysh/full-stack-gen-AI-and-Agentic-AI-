from dotenv import load_dotenv
from openai import OpenAI
import json

load_dotenv()

client = OpenAI()
# api_key = "AIzaSyASrdibwDzsLV6TZCIs0tWCRA2lsbmsDhA",
# base_url = "https://generativelanguage.googleapis.com/v1beta/"


SYSTEM_PROMPT = """
You nare an expert AI Assisstant in resolving user queries using chain of thought.You work on START. PLAN and Output steps.
you need to first PLAN what needs to be done. THE PLAN can be multiple steps.
Once you think enough PLAN has been done, finally you can give an OUTPUT.

Rules:
- Strictly Follow the given JSON output format.
- only run one step at a time
- The sequence of steps is START (Where user gives an input), PLAN (That can be multiple times 
) and finally OUTPUT (hich is gng to be dislayed to the user).

Output JSON Format:
{"step" : "START" | "PLAN" | "OUTPUT", "content" : "string"}

Example:
START: Hey, Can you solve 2 + 3 * 5 / 10
PLAN : {"step" : "PLAN": "content": "Seems like user is interested in math problem} 

PLAN : {"step" : "PLAN" : "content": "looking at the problem, we should solve this using BODMAS method"}
PLAN : {"step": "PLAN": "content" : "YES", The BODMAS is correct thing to be done here"}
PLAN : {"step": "PLAN": "content" : "first we must multiply 3 * 5 which is 15"}
PLAN : {"step": "PLAN": "content" : "Now the equation is 2 + 15 / 10"}
PLAN : {"step": "PLAN": "content" : "first we must perform divide that is 15 / 10 which is 1.5"}
PLAN : {"step": "PLAN": "content" : "first we must perform divide that is 15 / 10 which is 1.5"}
PLAN : {"step": "PLAN": "content" : "Now the equation is 2 + 1.5"}
PLAN : {"step": "PLAN": "content" : "Now finally lets perform addition "}
PLAN : {"step": "PLAN": "content" : "Now we have solved and have the answer as 3.5 as answer"}
OUTPUT : {"step": "OUTPUT": "content" : "3.5"}
"""
print("\n\n\n")
message_history = [
    {
        "role" : "system" , 
        "content": SYSTEM_PROMPT
    },
]

user_query = input("--->")
message_history.append({"role":"user","content":user_query})

while True:
    response = client.chat.completions.create(
        model = "gpt-4o",
        response_format = {"type" : "json_object"},
        messages = message_history
    )

    raw_result = (response.choices[0].message.content)
    message_history.append({"role":"assistant","content":raw_result})

    parsed_result  = json.loads(raw_result)

    if parsed_result.get("step") == "START":
        print("started" , parsed_result.get("content"))
        continue

    if parsed_result.get("step") == "PLAN":
        print("planned" , parsed_result.get("content"))
        continue
    
    if parsed_result.get("step") == "OUTPUT":
        print("output" , parsed_result.get("content"))
        break


response = client.chat.completions.create(
    model = "gemini-2.5-flash",
    response_format = {
        "type": "json_object"
    },
    messages = [
        {"role" : "system" , "content": SYSTEM_PROMPT},
        {"role": "user", "content": "Hey, write a code to add n numbers in js"},
        # Manually keep adding messages to History 
        {"role" : "assistant", "content": json.dumps({
            "step" : "START",
            "content" : "You want a js code to add 'n' numbers." 
        })}
    ]
)

print(response.choices[0].message.content)
print("\n\n\n")