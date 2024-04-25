# Art Panda

A minimalistic python repo script to rapidly generate a selection of images for website assets. Built by [docupanda.io](wwww.docupanda.io) team to scratch an itch. PRs welcome.  

## Prerequisites
This repo makes openai calls. Sign up for their API access at https://platform.openai.com/signup, and obtain your API key.

## Installation

Install your virtual environment and dependencies:

```bash
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -e .
```

Create a .env file and populate it with your openAI api key:
```bash
touch .env
echo "OPENAI_API_KEY=<YOUR_API_KEY>>" > .env
```


## Usage

Run the following line:
```bash
python scripts/art.py
```

This will start an interactive session which will prompt you to enter a short subject for the image you would like to generate. For example try:

`"A goofy greedy panda stealing sacks of gold"`

The script will then generate a selection of images based on your input in various styles under /output. Run python scripts/art.py --help to see the available styles, and generate more examples of your favorite style by e.g. running

```bash
python scripts/art.py --style="pop-art" --n 3 --subject "A goofy greedy panda stealing sacks of gold"
```
