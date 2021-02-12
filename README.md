<div align="center">

# flag-bot

<a href="https://www.python.org">
    <img alt="Python" src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54"></a>
<br>
<br>

This is a python bot that can solve the flag quiz on [geo-quiz.net](https://www.geo-quiz.net/de/flaggenquiz.html) faster than a human by automatically detecting the color of the top left pixel of the flag and clicking on the correct answer on the screen.

</div>

<details>
<summary>Table of Contents</summary>

- [Installation](#installation)
- [Usage](#usage)
- [How it Works](#how-it-works)
- [Limitations](#limitations)
- [Contributing](#contributing)
- [License](#license)
</details>

## Installation

The bot is running on Windows only as the win32api is used for clicking. To run it on Linux/macOS you need to modify the click function first.

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

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT). You are free to use, modify, and distribute this software for both personal and commercial purposes as long as you give attribution to the original author. For more information about the license, please see the `LICENSE` file.
