import sys as commandLine
import time

private_key = "MAGARAMCH"

def displayLoading(showTime):
    while showTime > 0:
        time.sleep(0.5)
        print("\n\n\n . . . . . . Loading . . . . . . ")
        showTime -= 1

def getReduced(str):
    return [ ord(str[index]) - 65 for index in range(len(str)) ]

def getIndexOfPrivateKey(index):
    return (index % len(private_key))

def getMessage(asciiList):
    privateList = getReduced(private_key)
    finalMessage = [ ((asciiList[index] - privateList[getIndexOfPrivateKey(index)]) % 26) for index in range(len(asciiList))]
    return finalMessage

def encryptFunction(message):
    message_upper = message.upper()
    original = getReduced(message_upper)
    decrypt = getMessage(original)
    answer = ""
    for character in decrypt:
        answer += chr(character + 65)
    return answer

def getStrings(first_arg):
    print("Working on the code")
    displayLoading(4)
    answer = []
    for text in first_arg:
        if not(text.isalpha()):
            print("Please check the input")
        else:
            answer.append(encryptFunction(text.strip()))
    print("\n\n\n{}\n".format(answer))


if __name__ == "__main__":
    first_arg = ""
    if len(commandLine.argv) > 1:
        time.sleep(1)
        getStrings(commandLine.argv[1:])
    else:
        print("You forgot to add encrypted message")
