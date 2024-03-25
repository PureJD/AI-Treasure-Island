import os
from openai import OpenAI

def open_ai_chat(question, context):
    # Retrieve the API key securely from an environment variable
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise ValueError("No API key found. Please set the OPENAI_API_KEY environment variable.")

    client = OpenAI(api_key=api_key)

    # Append the new question to the context
    context.append({"role": "user", "content": question})

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=context + [
                {"role": "system", "content": "Make a new line every 12 words to ensure it fits on screen. This is a choose your own adventure game called Treasure Island. You are setting the adventure for the user who will provide answers and it is your job to continue the adventure. Start every question with a themed drawing in ASCII art using monospaced font. Only use standard characters to ensure the drawing is displayed correctly."}
            ]
        )

        # Assuming there's at least one choice in the response and you want the message content
        if response.choices:
            generated_message_content = response.choices[0].message.content
            # Update the context with the AI's response
            context.append({"role": "system", "content": generated_message_content})
            print(generated_message_content)
        else:
            print("No choices were returned.")
            generated_message_content = ""

    except UnicodeEncodeError as e:
        print(f"Unicode encoding error: {e}")
        generated_message_content = ""
    except Exception as e:
        print(f"An error occurred: {e}")
        generated_message_content = ""

    return generated_message_content, context  # Return the updated context along with the response

# Initialize an empty context at the beginning of your game or conversation
context = []
