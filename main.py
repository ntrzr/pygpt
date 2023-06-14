import openai
openai.api_key = 'YOUR_API_KEY'

def generate_response(prompt):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.7
    )
    return response.choices[0].text.strip()

while True:
    user_input = input('You: ')
    if user_input.lower() in ['exit', 'quit']:
        break

    response = generate_response(user_input)
    print('ChatGPT:', response)
