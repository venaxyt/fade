# Module made by @venaxyt on Github
import os

def purple(text):
    os.system("")
    number = 40
    faded = ""
    for line in text.splitlines():
        faded += (f"\033[38;2;{number};0;220m {line}\n")
        number += 15
    return faded
