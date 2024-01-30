from openai import OpenAI
client = OpenAI(api_key="Your_Openai_Key")
import csv
import json

# from a csv to jsonl

with open('csv_path', mode='r', newline='') as csv_file , open('conversation.jsonl', mode='w') as jsonl_file:
    csv_reader = csv.DictReader(csv_file)
     
    csv_reader = csv.DictReader(csv_file)
    
    # Iterate through each row in the CSV file
    for row in csv_reader:
        # Create a dictionary with the role and content for each message
        messages = [
            {"role": "user", "content": row["Support Query"]},
            {"role": "assistant", "content": row["Category Description"]}
        ]
        
        # Append the messages dictionary to the conversation data
        json_data = json.dumps({"messages": messages})
        
        # Write the JSON string to the JSONL file followed by a newline
        jsonl_file.write(json_data + '\n')


training_file=client.files.create(
  file=open("conversation.jsonl", "rb"),
  purpose="fine-tune"
)

print(training_file.id)
response=client.fine_tuning.jobs.create(
  training_file=training_file.id, 
  model="gpt-3.5-turbo",
  suffix="convotune"
  
)
print(response)
print(client.fine_tuning.jobs.list(limit=1))


response=client.chat.completions.create(
  model="gpt-3.5-turbo-16k",
  messages=[
    {"role": "user", "content": "How can lookup multiple criteria into one cell? It only brought back only the first value when I did the Vlookup. I need look up the material id and region and pull back the CWID in the cell."}
  ]
)

response = client.chat.completions.create(
  model="ft:gpt-3.5-turbo-0613:personal:convotune:8mhoS3ZF",
  messages=[
    {"role": "user", "content": "can i get a fee waiver for mortage loan online"}
  ]
)

print(response.choices[0].message.content)
