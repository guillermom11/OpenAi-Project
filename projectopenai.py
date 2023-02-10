import openai

openai.api_key = "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"
model_engine = "text-davinci-003"
prompt = str(input())
completion = openai.Completion.create(
    engine = model_engine,
    prompt = prompt,
    max_tokens=1024,
    n=1,
    stop = None,
    temperature = 0.5 #how risky is the model
)
response = completion.choices[0].text
print(response)