import os
import requests

api_key = os.getenv("API_KEY")
url = os.getenv("URL")

headers = {
  "api-key" : api_key
}

def send_message(user_message, thread_id):

  body = {
    "message" : user_message
  }
  if thread_id != None:
    body["threadId"] = thread_id
  response = requests.post(url, headers=headers, json=body)
  response_data = response.json()

  return response_data

print("Welcome! Type your message and press Enter to send.")
print("Type 'exit' to end the program")
print("Type 'new' to switch conversation thread.")
print("Starting a new conversation for you.\n")

threads = []

while True:
  user_message = input("You: ")
  if user_message.lower() == "exit":
    break
  elif user_message.lower() == "new":
    current_thread_id = None
    print("Starting new conversation")
    continue
  

  current_thread_id = None
  response_data = send_message(user_message, current_thread_id)
  latest_message = response_data.get("response")
  current_thread_id = response_data.get("threadId")
  print(f"GPT: {latest_message}")
  threads.append(current_thread_id)
  
