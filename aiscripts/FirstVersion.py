import openai
import sys

openai.api_key = "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"

promt = sys.argv[1]

response = openai.Completion.create(engine="text-davinci-001", promt = promt, max_tokens=10)
print(response.choices[0].text)