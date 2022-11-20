#!/usr/bin/env python3


def decode_word(word):
    """
    Given a string nammed word,
    split the string into a list of integers,
    every integer is a 2 digit number if is greater than 96 and less than 100
    else is a 3 digit number.
    Return the list of integers.
    Example:
    input: "11610497110107115"
    output: [116, 104, 97, 110, 107, 115]
    """
    result = []
    while word != "":
        if int(word[:2]) >= 13 and int(word[:2]) < 100:
            result += [int(word[:2])]
            word = word[2:]
        else:
            result += [int(word[:3])]
            word = word[3:]
    print(result)
    return result


def decode_message(message):
    """
    Given a message, split it by spaces and decode each word
    Return the decoded message
    Example:
    input: "11610497110107115 102111114"
    output: "thanks for"
    """
    result = ""
    for word in message.split():
        for i in decode_word(word):
            result += chr(i)
        result += " "
    return result


def read_file(filename):
    """
    Read a file and return the content
    """
    with open(filename, "r") as f:
        return f.read().strip()


def main():
    """
    Main function
    Read the file and decode the message
    """
    input = read_file("encrypted.txt")
    decoded_message = decode_message(input)
    print(f"{decoded_message}")


if __name__ == "__main__":
    main()
