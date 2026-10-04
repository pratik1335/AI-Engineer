import os 
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API Key is not available")

client = Groq(api_key = my_api_key)

model = "openai/gpt-oss-20b"
role = "user"
# prompt = "I want to connect with you regarding this bug"
# prompt = "I love you baby!!"
prompt = "Suggest name for my cloth company"

message_system = {
    "role" : "system",
    # "content" : "You are my strict office collegue who is also my manager and is very professional"
    "content" : "You are a brand manager who suggests name for my cloth company. name should be in one word. and suggest only one name"
}

message = {
    "role" : role,
    "content" : prompt
}

messages = [message_system, message]

# Temperature is 0 by default which means safe
# response = client.chat.completions.create(model=model, messages=messages)
# response = client.chat.completions.create(model=model, messages=messages, temperature=1)
response = client.chat.completions.create(model=model, messages=messages, temperature=2)

# print(response)

print("##################################")

answer = response.choices[0].message.content

print(answer)