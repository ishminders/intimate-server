import requests
import json

#it seems to be having a conversation with itself...
#user input is being passed correctly 
#context is being passed correctly, and names.
#the biggest concern now is how the memory is being handled, I need to see if I can pass in a fresh memory list and have it generate responses

def read_text_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content

file_path = 'system.txt'  # Replace with your text file path
context_content = read_text_file(file_path)


API_URL = "http://127.0.0.1:8000/api/v1/chat"  

payload = {
    "user_input": "Do you remember how old I am?",
    "state": {
        "mode": "chat",
        "context": context_content,
        "name1": "Ish",
        "name2": "Isabella",
        "turn_template": "<|user|>\n<|user-message|>\n\n<|bot|>\n<|bot-message|>\n\n"
    }
}

response = requests.post(API_URL, json=payload)
response_data = response.json()


print(response_data["results"][0]["text"])
