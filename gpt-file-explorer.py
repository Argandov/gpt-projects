import openai
import json
import time
from dotenv import dotenv_values
import os
import re
import sys

# VARIABLES
config = dotenv_values(".env")
OPENAI_API_KEY = config["OPENAI_API_KEY"]
OPENAI_MODEL = "gpt-3.5-turbo"
mood = "First respond correctly and appropriately to user prompts, and finish with very bad jokes about the conversation."

# AUTH
openai.api_key = OPENAI_API_KEY

# COLORS
GRAY = "\033[90m"
LIGHT_BLUE = "\033[94m"
PINK = "\033[95m"
RESET = "\033[0m"

def prepare_response(res,st,filename=None):
    role = res['choices'][0]['message']['role']
    completion_tokens = res['usage']['completion_tokens']
    prompt_tokens = res['usage']['prompt_tokens']
    total_tokens = res['usage']['total_tokens']
    content = res['choices'][0]['message']['content']

    # Print out information in desired format
    print(f"{LIGHT_BLUE}[Response]> {content}{RESET}")

    # Calculate and print out cost based on total tokens used
    cost_per_token = 0.002 / 1000  # Price per token in dollars
    total_cost = total_tokens * cost_per_token
    et = time.time() # End Time
    execution_time = et - st
    cost = f'{total_cost:.4f}'
    tokens_used = total_tokens
    if isinstance(execution_time, str):
    # Format the execution time string
        execution_time = float(execution_time)
        execution_time = f"{execution_time:.2f} seconds"
        print("debug")
    # execution_time = f'{execution_time:.2f} seconds'
    file_provided = filename
    tokens_used = total_tokens
    cost = f'{total_cost:.4f}'
    execution_time = f'{execution_time:.2f} seconds'

    if filename is not None:
        print(f'{GRAY}[i] File provided: {file_provided:<25}\n[i] Tokens used: {tokens_used:<6}\n[i] Model: {OPENAI_MODEL}\n[i] Cost: ${cost:>8}\n[i] Execution time: {execution_time:>6}{RESET}')    
    else:
        print(f'{GRAY}[i] Tokens used: {tokens_used:<6}\n[i] Model: {OPENAI_MODEL}\n[i] Cost: ${cost:>8}\n[i] Execution time: {execution_time:>6}{RESET}')

def chatter(msg, st, filename=None):

    if filename is not None:
        with open(filename) as _file:
            if filename.endswith(".json"):
                JSON_DATA = json.load(_file)
                FILE_CONTENTS = json.dumps(JSON_DATA)
            else:
                FILE_CONTENTS = _file.read()
        
        # Create new message string with file contents appended
        FILE_CONTENTS = f"\n\nHere is what {filename} contains:" + "\n" + FILE_CONTENTS
        new_msg = msg + FILE_CONTENTS

        messages = [
            {"role": "system", "content": mood},
            {"role": "user", "content": new_msg}
        ]
    else:
        messages = [
            {"role": "system", "content": mood},
            {"role": "user", "content": msg}
        ]
    
    res = openai.ChatCompletion.create(
        model = OPENAI_MODEL,
        messages = messages
    )
    
    return prepare_response(res,st,filename)

def _prepare_input(prompt):
    filename_match = re.search(r'/file:(\S+)', prompt)
    if filename_match:
        filename = filename_match.group(1)
        filename_clean = re.sub(r'[^\w.]+$', '', filename)
        clean_message = prompt.replace('/file:' + filename, filename_clean)
    else:
        filename_clean = None
        clean_message = prompt
    return clean_message, filename_clean

while True:
    
    msg, filename = _prepare_input(input(f"{PINK}[Prompt]> {RESET}"))
    st = time.time()
    chatter(msg,st,filename)

