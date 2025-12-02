message = input("Say something! ").lower().strip()

while message != "exit":

    if message == "hello!":
        message = input("Hi, there! ").lower().strip()

    if message == "how are you?":
        message = input("I'm a program, but thanks for asking! ").lower().strip()

    elif message == "what are you doing?":
        message = input("I'm speaking to you. And you? ").lower().strip()

    else:
        message = input("Good. ")
