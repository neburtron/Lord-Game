from openai import OpenAI

## LLM Details ##
client = OpenAI(
    base_url="http://localhost:1234/v1", 
    # If you're actually paying OpenAI for their models, you either need to comment this out or figure out what URL to put here instead.
    api_key="not-needed"
    # Probably a good idea to get this from somewhere private for people that pay for OpenAI's stuff
    )
temp = 0.7
usedmodel="local model"
# Results depend on model and other settings.
# Additionally, if the LLM is being weird, you can look at the prompt + change however you want.


## Call Function ##
def main(msgs):
    try:
        completion = client.chat.completions.create(
            model=usedmodel,
            messages=msgs,
            temperature=temp,
        )
        return completion.choices[0].message
    except Exception as e:
        print()
        print(f"Error during LLM interaction: {e}")
        print()
        return None