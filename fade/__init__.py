# Module made by @venaxyt on Github
import os

def purplepink(text):
    os.system("")
    number = 40
    faded = ""
    for line in text.splitlines():
        faded += (f"\033[38;2;{number};0;220m {line}\033[0m\n")
        number += 15
    return faded

def greenblue(text):
    os.system("")
    number = 100
    faded = ""
    for line in text.splitlines():
        faded += (f"\033[38;2;0;255;{number}m {line}\033[0m\n")
        number += 15
    return faded

def pinkred(text):
    os.system("")
    number = 255
    faded = ""
    for line in text.splitlines():
        faded += (f"\033[38;2;255;0;{number}m {line}\033[0m\n")
        number -= 20
    return faded

def water(text):
    os.system("")
    number = 10
    faded = ""
    for line in text.splitlines():
        faded += (f"\033[38;2;0;{number};255m {line}\033[0m\n")
        number += 15
    return faded

def fire(text):
    os.system("")
    number = 150
    number2 = 0
    faded = ""
    for line in text.splitlines():
        faded += (f"\033[38;2;255;{number};{number2}m {line}\n")
        if not number < 0:
            number -= 23
        else:
            number2 += 23
    return faded
