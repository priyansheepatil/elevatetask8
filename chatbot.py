print("Bot: Hello! I'm your virtual assistant. Type 'Bye' exit.\n")

while True:
    user_ip = input("You: ").lower()

    if user_ip in ["hi", "hello", "hey"]:
        print("Bot: Hello there, how are you today?\n")
    elif "how are you" in user_ip:
        print("Bot: I'm just a bot, but I'm doing great. What about you?\n")
    elif "your name" in user_ip:
        print("Bot: My name is Bot11, created by Priyanshee Patil.\n")
    elif "weather" in user_ip:
        print("Bot: I can't check the live weather yet, but it is Winter Season.\n")
    elif "help" in user_ip:
        print("Bot: I can chat with you, tell my name, or discuss simple topics!\n")
    elif "bye" in user_ip:
        print("Bot: Bye bye! Have a nice day.\n")
        break
    
    else:
        print("Bot: I'm not sure how to respond to that. Can you rephrase it?\n")
     
print("Chat ended.")