from openai import OpenAI
import json

## LLM Details ##
client = OpenAI(
    base_url="http://localhost:1234/v1", 
    api_key="not-needed"
    )
temp = 0.7
usedmodel="local model"

## Read prompt file function ##
def readfile(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        content = [line.strip().rstrip(',') for line in lines if line.strip().rstrip(',')]  # Remove trailing comma
    return content

## Main function ##
def main(file):
    msgs = readfile(file)  # Read the file content
    formatted_msgs = []
    for msg in msgs:
        msg_dict = json.loads(msg)
        formatted_msgs.append({"role": msg_dict["role"], "content": msg_dict["content"]})

    # Call the LLM
    completion = client.chat.completions.create(
        model=usedmodel,
        messages=formatted_msgs,  # Pass the formatted messages
        temperature=temp,
    )
    return completion.choices[0].message

## Write response to file ##
def writefile(filename, completion_message):
    with open(filename, 'w') as f:
        f.write(completion_message.content)

response = main("testing.txt")
writefile("response.txt", response)

