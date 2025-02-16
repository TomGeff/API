import openai

openai.api_key = "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"
openai.api_base = "https://openrouter.ai/api/v1"

def open_ia_response(prompt):
    response = openai.ChatCompletion.create(
        model="openai/gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]