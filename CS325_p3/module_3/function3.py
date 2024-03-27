# this is the OpenAI querying/summarization module (function3.py)

import os
from dotenv import load_dotenv # for loading environment variables from .env file
import openai # for GPT-3.5 API
# function that returns the summary of the sanitized data given the sanitized data and the filename
# input: filename (string) - name of the file containing the sanitized data
# output: summary (string) - the summary of the sanitized data

def get_summary(filename) -> str:
    load_dotenv() # load the environment variables from the .env file
    openai_api_key = os.getenv('OPENAI_API_KEY') # get the value of the OPENAI_API_KEY environment variable

    # open the sanitized file
    with open(filename, 'r', encoding='utf-8') as file:
        sanitized = file.read()

    # the completion code is to create a 50-word summary of the sanitized data
    completion = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a writer who excels in summarizing articles in a concise and informative manner."},
            {"role": "user", "content": f"Summarize the article in 50 words, with proper grammar: {sanitized}"}
        ],
        temperature=0 # forces the model to be deterministic in following the prompt
    )

    summary = completion.choices[0].message.content # get the summary from the completion

    return summary