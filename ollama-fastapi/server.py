from dns import message
from fastapi import FastAPI,Body
from ollama import Client 


app = FastAPI()
# connect to ollama
client = Client(host="http://localhost:11434")


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/contact-us")
def read_contact_us():
    return {"email": "world@example.com"}

@app.post("/chat")
def chat(message: str = Body(...,description="The Message")):
    response = client.chat(model = "gemma:2b",messages=[
    {"role":"user" , "content": message}
])
    # the above is basically an api call 
    return {"response": response.message.content}


# we made an internal API server which uses ollama API to interact with our model



