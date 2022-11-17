import os
import openai

openai.api_key = "<apikey>"

user_input = input("Write your query here: ")
response = response = openai.Completion.create(
  model="text-davinci-002",
  prompt=f"{user_input}",
  temperature=0.5,
  max_tokens=150,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)
#print(response)
answer = response['choices'][0]
#print(answer)
for key,value in answer.items():
    if key == 'text':
        value = value.strip('\n')
        print(value)
