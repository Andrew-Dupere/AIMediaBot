# This code is for v1 of the openai package: pypi.org/project/openai
import os
import openai
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')



# client = OpenAI()

# response = client.chat.completions.create(
#   model="gpt-4",
#   messages=[],
#   temperature=0,
#   max_tokens=1024
# )

def gptCompletions(role, prompt):

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": role},
            {"role": "user", "content": prompt},
        ]
    )
    return(response.choices[0].message.content)

# print(gptCompletions('you are writing a twitter post','make a joke about joseph stalin'))


