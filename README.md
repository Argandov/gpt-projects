# 1. GPT-Chatter

GPT-Chatter is a Python program that uses the OpenAI GPT-3 API to provide chatbot functionality. This program allows users to engage in natural language conversations with an AI chatbot powered by GPT-3.

## Requirements

To run this program, you will need an OpenAI API key and a valid GPT-3 model. Set these values in a `.env` file as `OPENAI_API_KEY` and `OPENAI_MODEL`.

You will also need to install the following Python packages:
- `openai`
- `dotenv`

## Usage

To start a conversation with the GPT-3 chatbot, simply run the `gpt-chatter.py` script and enter a message when prompted.

You can optionally provide a JSON or plain text file to the chatbot by using the `/file:` 
command followed by the file path. For example, `/file:path/to/file.json`.
