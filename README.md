# QTF

A simple CLI tool for making HTTP GET and POST requests with Python.

## Features

- **GET requests** - Fetch JSON data from authorized web apps
- **POST requests** - Send JSON data to authorized web apps
- **Interactive CLI** - Simple command-based interface
- **Colorful output** - Powered by `termcolor`

## Installation

1. Clone the repository:

```bash
git clone https://github.com/<your-username>/QTF.git
cd QTF
```

2. Create and activate a virtual environment (not required):

```bash
python -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the tool:

```bash
python main.py
```

### Commands

| Command   | Description                                      |
|-----------|--------------------------------------------------|
| `get`     | Send a GET request and retrieve JSON data        |
| `post`    | Send a POST request with JSON data               |
| `clear`   | Clear the terminal and redraw the logo           |
| `help`    | Display available commands                       |
| `quit`    | Exit the tool                                    |

## Project Structure

```
QTF/
├── main.py              # Main entry point and CLI loop
├── modules/
│   ├── req.py           # GET request handler
│   ├── post.py          # POST request handler
│   ├── help.py          # Help command
│   └── logo.py          # ASCII logo display
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

## Dependencies

- `requests` - HTTP library
- `termcolor` - Terminal text coloring

## Author

Made by Skyrix
