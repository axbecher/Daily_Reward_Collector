# What is this?

A Python script for collecting daily bonuses in the video game "Don't Starve Together" on the Steam gaming platform. This script also includes a GUI for easier use by those who do not have extensive technical knowledge.

# Requirements

VS Code with Python Interpreter

To test if your PC can handle Python Scripts

Make a new file and name it test.py

There write:
```
print("Hello World")
```

And save it, VS Code should warn you that you need to install python extension, install it.
After that when you try to run it from VS Code, you will need to install Python Interpreter from Microsoft Store.

## Installation

Automation Script for Daily Gift requires [Python 3.10](https://apps.microsoft.com/store/detail/python-310/9PJPW5LDXLZ5?hl=de-at&gl=at) to run.

Install the dependencies and first setup.

```sh
cd DontStarveTogether
pip install -r requirements.txt
python .\executable.py
```

If "Custom URL" prompt appears insert url that you want to open after each time run has been compiled will open, empty means default => ( axbecher.com )

![Custom URL](https://i.imgur.com/wtFj89x.png)

You should have in taskbar the running script.

Press **1. START** and find location for steam.exe

![Main Menu](https://i.imgur.com/D4ELMl2.png)

After that, Steam should run automatically and should launch the game.

## Resources

| Resources | README |
| ------ | ------ |
| psutil | [psutil docs](https://psutil.readthedocs.io/en/latest/) |
| PyAutoGUI | [PyAutoGUI docs](https://pyautogui.readthedocs.io/en/latest/) |
| tldextract | [tldextract docs](https://pypi.org/project/tldextract/) |
| win10toast | [win10toast docs](https://pypi.org/project/win10toast/) |
| WMI | [WMI docs](https://pypi.org/project/WMI/) |
| VS Code | [VS Code Docs](https://code.visualstudio.com/docs) |
|
| Python 3.10 | [Microsoft Store](https://apps.microsoft.com/store/detail/python-310/9PJPW5LDXLZ5?hl=de-at&gl=at) |
| Axbecher .com | [Pesonal Website](https://axbecher.com) |
| 


## Development

Want to contribute? Great!

In folder "development" you can find scripts that I used to debug this project.
**If you have any ideas try to implement or even raise an issue and we can discuss.**

# Project Status

| Status | Name | Description |
| ------- |  --- | --- |
| ~~DONE~~ | ~~Preview GIF~~ | ~~Preview gifs for this project~~ |
| TODO | .exe | Create .exe instead of .py |
| TODO | Change click times | Change times for mouse clicks from GUI |
| TODO | inStartup docs | Docs related to inStartup feature |

# Logs

Want to see logs?

- Click on **"4. LOGS"** button from main menu.
or
- Just go in DontStarveTogether/logs

# License

MIT

**Free Software, Hell Yeah!**

