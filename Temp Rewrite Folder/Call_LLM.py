from openai import OpenAI
import Commands

## LLM Details ##
client = OpenAI(
    base_url="http://localhost:1234/v1", 
    api_key="not-needed"
    )
temp = 0.7
usedmodel="local model"
# Results depend on model and other settings.
# Additionally, if the LLM is being wierd, you can look at the prompt + change however you want.


## Call Function ##
def main(msgs):
    completion = client.chat.completions.create(
        model=usedmodel,
        messages=msgs,
        temperature=temp,
    )
    return completion.choices[0].message

## Run by itself ##
if __name__ == "__main__":
    response = main([
        {"role": "user", "content": "this is a test. talk about rocks or something."},
        {"role": "system", "content": "for instance, you could say rocks are cool."}
        ])
    # save stuff as txt file
    Commands.save("response.txt", response)