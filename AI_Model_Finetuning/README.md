# Fine-Tuning a GPT-3.5 Turbo Model

This repository provides an overview of the process to fine-tune a GPT-3.5 Turbo model using OpenAI's API. Fine-tuning allows you to adapt a pre-trained language model to perform specific tasks or generate specialized content. In this README, we'll guide you through the steps required to fine-tune the model, from data preparation to testing the fine-tuned model.

## Prerequisites

Before you start fine-tuning the model, ensure that you have the following prerequisites:

1. **OpenAI API Key**: You need an API key from OpenAI to access their models and services. Replace `"YOUR_API_KEY"` in the code with your actual API key.

## Getting Started

Follow these steps to get started with fine-tuning the GPT-3.5 Turbo model:

1. **Clone the Repository**: Clone this repository to your local machine using the provided GitHub repository URL.

2. **Install Dependencies**: Install the required Python packages if you haven't already. The primary dependency is the `openai` package, which is used to interact with the OpenAI API.

3. **Prepare Your Dataset**: Your dataset should be in CSV format and the we are using two columns from the given dataset as input and output to train our model:
   - `Support Query`: This column should contain user queries or prompts.
   - `Category Description`: This column should contain the desired model responses or answers.

4. **Modify the Code**: Open the provided Python script and replace `"PATH_TO_YOUR_CSV"` with the actual path to your CSV file. This script will convert your CSV data into JSONL format, which is suitable for fine-tuning.

5. **Convert CSV to JSONL**: Run the Python script to convert your CSV data into JSONL format. The script reads the CSV file, extracts the necessary columns, and creates a JSONL file that is ready for fine-tuning.

6. **Fine-Tuning the Model**: The code will upload the JSONL file to OpenAI for fine-tuning. The model used for fine-tuning is `"gpt-3.5-turbo"`. You can monitor the console for progress updates on the fine-tuning process. The fine-tuning process typically takes some time, so be patient.

## Testing the Fine-Tuned Model

After the fine-tuning process is completed, you can test your fine-tuned model with user queries or prompts. Here's an example of how to make queries to the model using Python:

```python
response = client.chat.completions.create(
    model=client.fine_tuning.jobs.list(limit=1).data[0].fine_tuned_model,
    messages=[
        {"role": "user", "content": "Can I get a fee waiver for mortgage loan online?"}
    ]
)

print(response.choices[0].message.content)

