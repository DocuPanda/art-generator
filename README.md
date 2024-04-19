# artpanda

A simple python script to rapidly generate a selection of images for website assets. 

## Prerequisites
This repo makes openai calls. Sign up for their API access at https://platform.openai.com/signup, and obtain your API key.

## Installation

Install your virtual environment and dependencies:

```bash
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

Create a .env file and populate it with your openAI api key:
touch .env
echo "OPENAI_API_KEY=your_api_key" > .env


## Usage

Run the following line:
```bash
python scripts/art.py
```

This will prompt you to enter a short subject for the image you would like to generate. For example try:

"A goofy greedy panda stealing sacks of gold"

The script will then generate a selection of images based on your input in various styles. Run python scripts/art.py --help to see the available styles, and generate more examples of your favorite style by e.g. running

python scripts/art.py --style="pop-art" --n 3 --subject "A goofy greedy panda stealing sacks of gold"
