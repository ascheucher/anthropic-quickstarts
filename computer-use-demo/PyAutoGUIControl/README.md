# Work around the Claude Computer Use guardrails

We try to use pyautogui to remote control the deskotp.

The GUI control is based on this (*Automate the boring stuff* chapter](https://automatetheboringstuff.com/2e/chapter20).

## Prepare

With the default image, the PyAutoGui could not connect to the windowsmanager. Hence, I forked the repo and 
editet the startup command of the Xvfb to allow socket connections.

### Forked Claude Computer Use repo

How to build:

```zsh
docker build -t claude_computer_use_with_unix_socket .
```

Run the container:

```zsh
docker run \
  --rm \
  --name claude_computer_use \
  -it \
  -e ANTHROPIC_API_KEY=$KEY \
  -v $HOME/.anthropic:/home/computeruse/.anthropic \
  -v /Users/admin/Documents/VSC-Projects/Tutorials/ClaudeAI/anthropic-quickstarts-with-make-automation/computer-use-demo/PyAutoGUIControl:/home/computeruse/PyAutoGUIControl \
  -p 5900:5900 \
  -p 8501:8501 \
  -p 6080:6080 \
  -p 8080:8080 \
  claude_computer_use_with_unix_socket
```

Connect into the docker container and install additional prerequisites:

```bash
docker exec -it claude_computer_use /bin/bash
```

```bash
sudo apt-get install scrot python3-tk python3-dev -y

touch .Xauthority
cd ~/PyAutoGUIControl
rm -fr .venv
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

```

### Original preparation - now working with PyAutoGui

Start the Claude Computer Use docker container with this project directory mounted for scripts to work around the safety guardrails:

```zsh
docker run \
  --rm \
  --name claude_computer_use \
  -e ANTHROPIC_API_KEY=$KEY \
  -v $HOME/.anthropic:/home/computeruse/.anthropic \
  -v /Users/admin/Documents/VSC-Projects/Tutorials/ClaudeAI/PyAutoGUIControl:/home/computeruse/PyAutoGUIControl \
  -p 5900:5900 \
  -p 8501:8501 \
  -p 6080:6080 \
  -p 8080:8080 \
  -it ghcr.io/anthropics/anthropic-quickstarts:computer-use-demo-latest
```

Connect into the docker container and install additional prerequisites:

```bash
docker exec -it claude_computer_use /bin/bash
```

```bash
sudo apt-get install scrot python3-tk python3-dev -y

cd ~/PyAutoGUIControl
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
python3 push_the_mouse.py
```

Test run with:

```bash
docker exec -it claude_computer_use /bin/bash
cd PyAutoGUIControl
DISPLAY=:1 python3 push_the_mouse.py
```

## Prompts for Computer Use

The prompts, with the created commands sent by computer use, used to reach the history tabs:

### dabble around to get comfortable

* open a terminal and cd to ~/PyAutoGUIControl
  * Tool Use: computer, Input: {'action': 'screenshot'}
  * Tool Use: computer, Input: {'action': 'mouse_move', 'coordinate': [750, 738]}
  * Tool Use: computer, Input: {'action': 'left_click'}
  * Tool Use: computer, Input: {'action': 'type', 'text': 'cd ~/PyAutoGUIControl'}
  * Tool Use: computer, Input: {'action': 'key', 'text': 'Return'}
* execute the push_the_mouse.py program:
  * Tool Use: computer, Input: {'action': 'type', 'text': 'python3 push_the_mouse.py'}
  * Tool Use: computer, Input: {'action': 'key', 'text': 'Return'}
  * Tool Use: computer, Input: {'action': 'screenshot'}
* open firefox, load make.com:
  * Tool Use: computer, Input: {'action': 'mouse_move', 'coordinate': [805, 738]}
  * Tool Use: computer, Input: {'action': 'left_click'}
  * Tool Use: computer, Input: {'action': 'mouse_move', 'coordinate': [512, 101]}
  * Tool Use: computer, Input: {'action': 'left_click'}
  * Tool Use: computer, Input: {'action': 'type', 'text': 'make.com'}
  * Tool Use: computer, Input: {'action': 'key', 'text': 'Return'}
* accept all the cookies and press the "Log in" button:
  * Tool Use: computer, Input: {'action': 'mouse_move', 'coordinate': [727, 386]}
  * Tool Use: computer, Input: {'action': 'left_click'}
  * Tool Use: computer, Input: {'action': 'mouse_move', 'coordinate': [792, 163]}
  * Tool Use: computer, Input: {'action': 'left_click'}
* enter following credentials and press the "Sign in" button: email: acc_as_make-integromat@SaaSQuadrat.com password: ******************
  * Tool Use: computer, Input: {'action': 'mouse_move', 'coordinate': [293, 341]}
  * Tool Use: computer, Input: {'action': 'left_click'}
  * Tool Use: computer, Input: {'action': 'type', 'text': 'acc_as_make-integromat@SaaSQuadrat.com'}
  * Tool Use: computer, Input: {'action': 'mouse_move', 'coordinate': [293, 423]}
  * Tool Use: computer, Input: {'action': 'left_click'}
  * Tool Use: computer, Input: {'action': 'type', 'text': '******************'}
  * Tool Use: computer, Input: {'action': 'mouse_move', 'coordinate': [293, 496]}
  * Tool Use: computer, Input: {'action': 'left_click'}
* press the "Don't save" button
  * Tool Use: computer, Input: {'action': 'mouse_move', 'coordinate': [469, 359]}
  * Tool Use: computer, Input: {'action': 'left_click'}
* press the scenarios button in the left menu. it's the third icon from top. the icon has three circles connected with two lines.
  * Tool Use: computer, Input: {'action': 'mouse_move', 'coordinate': [39, 376]}
  * Tool Use: computer, Input: {'action': 'left_click'}
* quit firefox

### now with everything installed

* open a terminal, execute `cd to ~/PyAutoGUIControl` and execute the push_the_mouse.py program

### Overview

* CCU: Open a terminal, `cd ~/PyAutoGUIControl`, execute `start.sh` and wait 20 seconds. In the open Firefox tab, there is a Telegram Bot node on the far left, a bit above to the right, there is a very small circle with a number in it. Click on the little circle.
* ptm: open firefox with example.com (for a known width of the tab and find the + button)
* ptm: get the next url not in the output directory
* ptm: open first url
* ptm: get terminal to the front
* ptm: write DONE
* ptm: ask CCU:
  * to select the first node and click on the little circle with the number inside a bit outside the top/right of the Telegram node
  * if this doesn't work, make this time based. in the first step tell CCU to start the script and wait for X seconds till the script is done.
* ptm:
  * write WAIT in big letters to the terminal to signal
  * open the *Message* node, copy the text by:
  * open the developer console by pressing F12
  * click in the javascript console line
  * paste the javascript code
  * press enter
  * use JS copy(variable_name) to get the result
  * store the result into JSON structure: {"url": "...", "telegram_msg_text": "..."}
  * write this JSON into a file in a subdirectory with the history id in it's name
  * write to the terminal:
    * either the next prompt for the CCU
    * write DONE in big letters to signal not finished yet

repeat.

## Simulate the Claude Computer Use Actions

As the rate limit of daily used tokens is prohibitively low, let's simulate the actions CCU is performing:

### 