# Connect to Web3 app with your Metamask wallet using Python Selenium

This Python script automates the process of setting up and connecting Metamask to Web3 applications. It uses Selenium to interact with the Firefox browser, opens Firefox with the Metamask extension installed, imports an existing wallet, and connects to a Web3 application (in this case, Uniswap).

## Prerequisites

- Python 3.x
- Selenium library (install via `pip install selenium`)
- GeckoDriver for Firefox (download from [here](https://github.com/mozilla/geckodriver/releases))


## Usage

1. Install Firefox if not already installed.
2. Update the `extension` variable in `main.py` with the link to the Metamask extension.
3. Make sure you have a passphrase saved in a file named `passphrase.txt`.
4. Run the script using Python.

```bash
python main.py

## How it Works

The script performs the following steps:

Opens Firefox with the Metamask extension.
Install Metamask to web browser.
Connects to Metamask and imports the wallet using the passphrase from passphrase.txt.
Connects to a Web3 application (in this case, Uniswap).

## License

This project is licensed under the [MIT License](LICENSE).


## Adjustments and Contributions

Feel free to make adjustments or contribute to this project. If you have any suggestions or find any issues, please open an issue or a pull request.

If you find this project helpful or useful in any way, consider giving it a star. It's a great way to show appreciation and support!

Thanks for checking out this project!
