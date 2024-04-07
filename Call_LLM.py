from openai import OpenAI
import json

## LLM Details ##
client = OpenAI(
    base_url="http://localhost:1234/v1", 
    api_key="not-needed"
    )
temp = 0.7
usedmodel="local model"
# Results depend on model and other settings.'
# Additionally, if the LLM is being wierd, you can look at the prompt + change however you want.


## Main function ##
def main(msgs):
    # Call the LLM
    completion = client.chat.completions.create(
        model=usedmodel,
        messages=msgs,
        temperature=temp,
    )
    return completion.choices[0].message


## Write response to file ##
def writefile(filename, completion_message):
    with open(filename, 'w') as f:
        f.write(completion_message.content)


if __name__ == "__main__":
    response = main([
        {"role": "system", "content": "this is a test. talk about rocks or something."},
        {"role": "user", "content": "for instance, you could say rocks are cool."}
        ])
    writefile("response.txt", response)

    