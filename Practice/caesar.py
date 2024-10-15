key = {
    "a": "x",
    "b": "y",
    "c": "z",
    "d": "a",
    "e": "b",
    "f": "c",
    "g": "d",
    "h": "e",
    "i": "f",
    "j": "g",
    "k": "h",
    "l": "i",
    "m": "j",
    "n": "k",
    "o": "l",
    "p": "m",
    "q": "n",
    "r": "o",
    "s": "p",
    "t": "q",
    "u": "r",
    "v": "s",
    "w": "t",
    "x": "u",
    "y": "v",
    "z": "w"
}

decryt_key = {
    "x": "a",
    "y": "b",
    "z": "c",
    "a": "d",
    "b": "e",
    "c": "f",
    "d": "g",
    "e": "h",
    "f": "i",
    "g": "j",
    "h": "k",
    "i": "l",
    "j": "m",
    "k": "n",
    "l": "o",
    "m": "p",
    "n": "q",
    "o": "r",
    "p": "s",
    "q": "t",
    "r": "u",
    "s": "v",
    "t": "w",
    "u": "x",
    "v": "y",
    "w": "z"
}

def caesar_cipher():
    mode = input("Would you like to encrypt or decrypt? ").lower()
    result = ""
    if mode == "encrypt":
        user_input = input("Enter a message to encrypt: ").lower()
        for letter in user_input:
            if letter in key:
                result += key[letter]
            else:
                result += letter
        return f"The result is: {result}"
    elif mode == "decrypt":
        user_input = input("Enter a message to decrypt: ").lower()
        for letter in user_input:
            if letter in decryt_key:
                result += decryt_key[letter]
            else:
                result += letter
        return f"The result is: {result}"


print(caesar_cipher())