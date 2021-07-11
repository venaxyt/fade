# Module made by @venaxyt on Github
from random import randint
from os import system

def blackwhite(text):
    system(""); faded = ""
    red = 0; green = 0; blue = 0
    for line in text.splitlines():
        faded += (f"\033[38;2;{red};{green};{blue}m{line}\033[0m\n")
        if not red == 255 and not green == 255 and not blue == 255:
            red += 20; green += 20; blue += 20
            if red > 255 and green > 255 and blue > 255:
                red = 255; green = 255; blue = 255
    return faded

def purplepink(text):
    system(""); faded = ""
    red = 40
    for line in text.splitlines():
        faded += (f"\033[38;2;{red};0;220m{line}\033[0m\n")
        if not red == 255:
            red += 15
            if red > 255:
                red = 255
    return faded

def greenblue(text):
    system(""); faded = ""
    blue = 100
    for line in text.splitlines():
        faded += (f"\033[38;2;0;255;{blue}m{line}\033[0m\n")
        if not blue == 255:
            blue += 15
            if blue > 255:
                blue = 255
    return faded

def pinkred(text):
    system(""); faded = ""
    blue = 255
    for line in text.splitlines():
        faded += (f"\033[38;2;255;0;{blue}m{line}\033[0m\n")
        if not blue == 0:
            blue -= 20
            if blue < 0:
                blue = 0
    return faded

def purpleblue(text):
    system(""); faded = ""
    red = 110
    for line in text.splitlines():
        faded += (f"\033[38;2;{red};0;255m{line}\033[0m\n")
        if not red == 0:
            red -= 15
            if red < 0:
                red = 0
    return faded

def water(text):
    system(""); faded = ""
    green = 10
    for line in text.splitlines():
        faded += (f"\033[38;2;0;{green};255m{line}\033[0m\n")
        if not green == 255:
            green += 15
            if green > 255:
                green = 255
    return faded

def fire(text):
    system(""); faded = ""
    green = 250
    for line in text.splitlines():
        faded += (f"\033[38;2;255;{green};0m{line}\033[0m\n")
        if not green == 0:
            green -= 25
            if green < 0:
                green = 0
    return faded

def brazil(text):
    system(""); faded = ""
    red = 0
    for line in text.splitlines():
        faded += (f"\033[38;2;{red};255;0m{line}\033[0m\n")
        if not red > 200:
            red += 30
    return faded

def random(text):
    system(""); faded = ""
    for line in text.splitlines():
        for character in line:
            faded += (f"\033[38;2;{randint(0,255)};{randint(0,255)};{randint(0,255)}m{character}\033[0m")
        faded += "\n"
    return faded
