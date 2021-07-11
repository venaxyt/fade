# Module made by @venaxyt on Github
from random import randint
from os import system

def purplepink(text):
    system("")
    number = 40
    faded = ""
    for line in text.splitlines():
        faded += (f"\033[38;2;{number};0;220m{line}\033[0m\n")
        if not number == 255:
            number += 15
            if number > 255:
                number = 255
    return faded

def greenblue(text):
    system("")
    number = 100
    faded = ""
    for line in text.splitlines():
        faded += (f"\033[38;2;0;255;{number}m{line}\033[0m\n")
        if not number == 255:
            number += 15
            if number > 255:
                number = 255
    return faded

def pinkred(text):
    system("")
    number = 255
    faded = ""
    for line in text.splitlines():
        faded += (f"\033[38;2;255;0;{number}m{line}\033[0m\n")
        if not number == 0:
            number -= 20
            if number < 0:
                number = 0
    return faded

def purpleblue(text):
    system("")
    number = 110
    faded = ""
    for line in text.splitlines():
        faded += (f"\033[38;2;{number};0;255m{line}\033[0m\n")
        if not number == 0:
            number -= 15
            if number < 0:
                number = 0
    return faded

def water(text):
    system("")
    number = 10
    faded = ""
    for line in text.splitlines():
        faded += (f"\033[38;2;0;{number};255m{line}\033[0m\n")
        if not number == 255:
            number += 15
            if number > 255:
                number = 255
    return faded

def fire(text):
    system("")
    number = 250
    faded = ""
    for line in text.splitlines():
        faded += (f"\033[38;2;255;{number};0m{line}\033[0m\n")
        if not number == 0:
            number -= 20
            if number < 0:
                number = 0
    return faded

def brazil(text):
    system("")
    number = 0
    faded = ""
    for line in text.splitlines():
        faded += (f"\033[38;2;{number};255;0m{line}\033[0m\n")
        if not number > 200:
            number += 30
    return faded

def random(text):
    system("")
    faded = ""
    for line in text.splitlines():
        for character in line:
            faded += (f"\033[38;2;{randint(0,255)};{randint(0,255)};{randint(0,255)}m{character}\033[0m")
        faded += "\n"
    return faded
