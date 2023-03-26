"""
response.py
-----------------
Answers users question in the chat
"""

import openai
import os
openai.api_key = ""

# In this function, you will accept a question from the user and generate a response using GPT
def answer_question(user_question):
    """
    Answer to questions in the chatbox
    :param user_question: Question of user in the chat
    """
    prompt = f"Pretend you're zoomer, Generate me a humour meme of {user_question} using these fields, Image Description: Caption:  no line breaks between, don't give any extra comments"
    print(prompt)
    chatgpt_response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.55,
        max_tokens=500,
        top_p=0.95)
    # TODO: generate response based on user_question and return as a single string
    print(chatgpt_response['choices'][0]['message']['content'].strip())

    return chatgpt_response['choices'][0]['message']['content'].strip()

# In this function, you will generate an image based on the user prompt
def generate_image(user_prompt):
    try:
        # TODO: generate one image which relates to prompt, and return the url of the image as a string
            image_object = openai.Image.create(
            prompt=user_prompt,
            n=1,
            size="512x512")
            print(image_object['data'][0]['url'])
            return image_object['data'][0]['url']
    
    except:
        # DO NOT DELETE!
        return ""