from transformers import AutoModelForCausalLM, AutoTokenizer
import speech_recognition as sr
import pyaudio
import torch
import random

tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium", padding_side = "left")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")


# exiting responses
exit_response = ["take care", "Thank you for your time", "it was nice talking to you", "you are one such fucker"]
# Let's chat until user decides to stop
while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak something...")
        audio = r.listen(source)

    try:
        user_input = r.recognize_google(audio)
    except sr.UnknownValueError:
        print("Wtf did you just said")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    # Check if the user wants to stop the conversation
    if user_input.lower() in ['stop', 'quit', 'exit', 'bye', 'sayonara']:

        print(random.choice(exit_response))
        break

    # Encode the new user input, add the eos_token, and return a tensor in PyTorch
    new_user_input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors='pt')

    # Append the new user input tokens to the chat history
    bot_input_ids = torch.cat([chat_history_ids, new_user_input_ids], dim=-1) if 'chat_history_ids' in locals() else new_user_input_ids

    # Generate a response while limiting the total chat history to 1000 tokens
    chat_history_ids = model.generate(bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)

    # Pretty print the last output tokens from the bot
    print("Naukar: {}".format(tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)))
