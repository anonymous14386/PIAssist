from ollama import chat
from ollama import ChatResponse

response: ChatResponse = chat(model='gemma2:2b', messages=[
	{
		'role': 'user',
		'content': 'Why is the sky blue?',
	},
])
print(response['message']['content'])
#or access fields directly
print(response.message.content)
