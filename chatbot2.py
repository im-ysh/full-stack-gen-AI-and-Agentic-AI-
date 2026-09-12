from google import genai
from dotenv import load_dotenv
from google.genai import types
import os 


load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if api_key is None:
    print("ERROR : API_KEY is not found")
    exit()


# above is configuring the api key and loading the environment variables.

# now leets create a cient to interact with LLMs

client = genai.Client(api_key = api_key)

def create_task(
        title : str,
        assignee : str,
        priority : str,
        status: str = "created"
): 
    task = {
        "title" : title,
        "assignee" : assignee,
        "priority" : priority,
        "status" : status    
    }

    print("TOOL ACTUALLY RAN:", task)


    return task

tools = [create_task]

chat = client.chats.create (
model = "gemini-3.6-flash",
config=types.GenerateContentConfig(
    system_instruction = """
    you are my coding mentor,
    explain things simply
    Assume I may have forgotten the basic
    Use examples when useful.
    """,
     
    tools = tools,
    automatic_function_calling=types.AutomaticFunctionCallingConfig(
            disable=True
        )
    )
)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
# task = create_task("Learn Python", "Vaishu", "high", "created")

# print(task)

while True:
    question = input("\nYou: ")
 
    if question.lower() == "quit":
        print("Goodbye!")
        break


#     response = client.models.generate_content(
#     model = "gemini-3.6-flash",
#     contents = question
# )

    # print("\nAI: " + response.text)
    # print("\nFULL RESPONSE:")
    # print(response)

    response = chat.send_message(question)

    function_call = response.candidates[0].content.parts[0].function_call


    if function_call:
       print("FUNCTION NAME:", function_call.name)
       print("ARGUMENTS:", function_call.args)

       if function_call.name == "create_task":
           result = create_task(**function_call.args)

           print("TOOL RESULT:", result)

           tool_response = types.Part.from_function_response(
               name=function_call.name,
               response=result
            )

    print("TOOL RESPONSE PART:", tool_response)

    final_response = chat.send_message(tool_response)

    print("\nAI:", final_response.text)

else:
    print("\nAI:", response.text)


    