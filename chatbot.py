#imports library/module to use openai
import openai
import json
openai.api_key = "can hardcode API key here"

#function that creates message that will contain past conversations
def messageBuilding(user_message, past_messages):
    past_messages.append({"role": "user", "content": user_message})
    return past_messages

#function that sends API request
def apiCall(past_messages):
    completion = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=past_messages
    )
    return completion

#main function
def main():
    past_messages = [{"role": "system", "content": "You are an assistant"}]

    user_input = ""
    #chatbot continues to hold conversation with user until they enter "Quit"
    while user_input != "Quit":
        if user_input == "Quit":
            break
        user_input = input()
        past_messages = messageBuilding(user_input, past_messages)
        completion = apiCall(past_messages)
        print(completion.choices[0].message.content)

if __name__ == "__main__":
    main()
