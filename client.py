from openai import OpenAI
client = OpenAI(
    api_key = "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"
)
completion = client.chat.completions.create(
    model="gpt-5-mini",
    messages = [
    {"role": "system", "content": "You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Assistant."},
    {"role": "user", "content": "What is coding?"}
]
)
print(completion.choices[0].message)
