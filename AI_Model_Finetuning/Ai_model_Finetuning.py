from openai import OpenAI
client = OpenAI(api_key="YOUR_API KEY")
import csv
import json

#The following script reads a CSV file from the specified path, extracts the 'Support Query' and 'Category Description' columns, and then creates a JSONL file with the data formatted appropriately for training our model.

with open('PATH_TO_YOUR_CSV', mode='r', newline='') as csv_file , open('conversation.jsonl', mode='w') as jsonl_file:
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

# This chunk of code is to open our Jsonl file for finetuning
training_file=client.files.create(
  file=open("conversation.jsonl", "rb"),
  purpose="fine-tune"
)

# This block of code is to train our AI model 
print(training_file.id)
response=client.fine_tuning.jobs.create(
  training_file=training_file.id, 
  model="gpt-3.5-turbo",
  suffix="convotune"
  
)

# This line of code allows you to check the current status of our training model, showing whether it is still in the training process or has completed training.

print(client.fine_tuning.jobs.list(limit=1))


# Testing FineTuned Model

response = client.chat.completions.create(
  model=client.fine_tuning.jobs.list(limit=1).data[0].fine_tuned_model,
  messages=[
    {"role": "user", "content": "can i get a fee waiver for mortage loan online"} # Example Question
  ]
)

print(response.choices[0].message.content)
