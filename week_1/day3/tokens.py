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

prompt1 = "Hi!"
prompt2 = "Explain time travel in Detail"
prompt3 = "Write a 1000 word essay on Machine learning"

prompts = [prompt1, prompt2, prompt3]
for prompt in prompts:
    message = {
    "role" : role,
    "content" : prompt
    }
    messages = [message]
    # response = client.chat.completions.create(model=model, messages=messages)
    # usage = response.usage
    # print(f"Prompt : {prompt} --> your tokens: {usage.prompt_tokens} completeion_tokens: {usage.completion_tokens} total tokens: {usage.total_tokens}")
    response = client.chat.completions.create(model=model, messages=messages, max_tokens=1000)
    usage = response.usage
    print(f"Prompt : {prompt} --> your tokens: {usage.prompt_tokens} completeion_tokens: {usage.completion_tokens} total tokens: {usage.total_tokens} Finish Reason: {response.choices[0].finish_reason}")



# prompt = "Do you know CDAC?"
# message = {
#     "role" : role,
#     "content" : prompt
# }

# messages = [message]
# response = client.chat.completions.create(model=model, messages=messages)
# print(response)
# print("##################################")
# answer = response.choices[0].message.content
# print(answer)