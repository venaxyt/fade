> # FADE TEXT

![image](https://user-images.githubusercontent.com/81310818/125177956-7e21cb80-e1e0-11eb-86c3-91a201965b33.png)

```
# Module made by @venaxyt on Github
import fade

text = """
      ▒▓     █ ▓█████ ░███▄    █  ▄▄▄      ▒██   ██▒ ▓█   ██  ███▄ ▄███▓
       ▓█░   █▒▓█   ▀ ▒██ ▀█  ░█ ▒████▄    ▒▒ █ █ ▒░ ██  ░██▒▓██▒▀█▀ ██▒
       ▓██  ██░▒███   ▓██  ▀█ ██▒▒██  ▀█▄  ░░  █   ░▒██  ▒██░▓██    ▓██░
        ▒██ █░░▒██  ▄ ▓██▒  ▐▌██▒░██▄▄▄▄██  ░ █ █ ▒ ▓██  ▓██░▒██    ▒██
         ▒▀█░  ░▓████▒▒██░   ▓██░ ▓█   ▓██▒▒██▒ ▒██▒▒▓█████▓ ▒██▒   ░██▒
         ░  ░  ░░ ▒░ ░░ ▒░   ▒ ▒  ▒▒   ▓▒█░▒▒ ░ ░▓ ░░▒▓▒ ▒ ▒ ░ ▒░   ░  ░
         ░ ░    ░ ░  ░░ ░░   ░     ▒   ▒▒ ░░░   ░▒ ░ ░▒░ ░   ░  ░      ░
                    ░   ░  ░    ░    ░   ▒    ░    ░    ░░ ░    ░ v e n a x ░
"""
# Fading a ascii art text (pink-purple)
faded_text = fade.purple(text)
print(faded_text)
>>> Output :
```
> ![](https://github.com/venaxyt/fade/blob/main/images/purple-pink.PNG)
```
# Fading a ascii art text (green-blue)
faded_text = fade.blue(text)
print(faded_text)
>>> Output :
```
> ![](https://github.com/venaxyt/fade/blob/main/images/blue-green.PNG)

> ### **Download** : ``pip install fade``<br>
> ### **PyPi : https://pypi.org/project/fade**
