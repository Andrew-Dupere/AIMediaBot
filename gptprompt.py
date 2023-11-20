# This code is for v1 of the openai package: pypi.org/project/openai
import os
import openai
from openai import OpenAI
 
from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
openai.api_key = OPENAI_API_KEY




client = OpenAI(
    api_key=os.environ['OPENAI_API_KEY']
)

#this is the function used by the main script
def gptClientCompletions(role, prompt):
    response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {
            "role": role,
            "content": prompt,
        },
    ],

)
    return response.choices[0].message.content


def gptCompletions(role, prompt):

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": role},
            {"role": "user", "content": prompt},
        ]
    )
    return(response.choices[0].message.content)




print(gptClientCompletions('user','what was the biggest city in china in the year 1000?'))
