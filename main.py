import os
import openai
import config

openai.api_key = config.key
response = openai.Image.create(prompt="a cricket match", n=1, size="1024x1024")
image_url = response['data'][0]['url']
print(image_url)
