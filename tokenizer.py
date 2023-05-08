import openai
from transformers import GPT2TokenizerFast
import sys

input_file = sys.argv[1]

tokenizer = GPT2TokenizerFast.from_pretrained("gpt2")
with open(input_file, "r", encoding='utf-8') as f:
    s = f.read()
encoded = tokenizer.encode(s)
numberOfTokens = len(encoded)
print('File\'s total Tokens: ', numberOfTokens)
