<div align="center">

# flag-bot

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

This is a python bot that can solve the flag quiz on [geo-quiz.net](https://www.geo-quiz.net/de/flaggenquiz.html) faster than a human by automatically detecting the color of the top left pixel of the flag and clicking on the correct answer on the screen.

</div>

## Table of contents

- [Installation](#installation)
- [Usage](#usage)
- [How it Works](#how-it-works)
- [Limitations](#limitations)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone this repository to your local machine.
2. Install the dependencies mentioned below:
- Python 3.x
- PyAutoGUI (`pip install pyautogui`)

## Usage

1. Open the flag quiz on geo-quiz.net using Firefox (not in full screen mode).
2. Do NOT click on start, the bot will start the quiz by it self.
3. Run the script `flag-bot.py` using the command `python flag-bot.py`.
4. The bot will automatically start solving the quiz.

## How it Works

The bot uses PyAutoGUI to automate the clicking process and to capture the screen. The bot detects the color of the top left pixel of the flag. If the top left pixel of two or more flags has the same RGB value, the bot will detect the color of the bottom right pixel too. It then compares the color to a dictionary of flag colors and clicks on the corresponding answer. The process is repeated for every flag until the quiz is completed.

Additionally, to ensure that the bot doesn't get detected as cheating, there are random delays added between each step of the process. These delays can be adjusted in the script.

## Limitations

This bot uses absolute screen coordinates, so it can only be used on a 1920 x 1080 pixel resolution screen using Firefox browser in normal view (not in full screen mode). Alternatively, you can manually adjust the coordinates in the script to match your screen resolution. Additionally, the bot is sometimes too fast for the anti-cheat mechanisms, so you might need to adjust the delays in the script.

## Contributing

If you would like to contribute to this project, please follow these steps:

1. Fork the repository to your own account.
2. Create a new branch with your changes.
3. Submit a pull request with your changes.

## License

</a>This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.
You are free to use, copy, modify, distribute, and display the work, as well as make derivative works based on it, as long as you give attribution to the original author and share any derivative works under the same license. For more information about the license, please see the `LICENSE.md` file.
<div align="center">
<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></div>