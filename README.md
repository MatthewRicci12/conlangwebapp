# !!! This readme is currently in a WIP state!

# Conlang Web App

## Description
This project is a love letter to one of my favourite hobbies: Conlanging, or constructing artificial languages, usually with naturalistic features to so that they feel real. This project was also to work on a weak muscle of mine, that muscle being building web apps with a RESTful protocol. To that end, I created a web app to help me quickly scaffold and iterate on new languages by starting with words first, then retroactively assigning meaning to words, flagging grammar, and constructing the writing system. This is a top-down approach to language; it's far from the only valid approach, but my preferred one. My main conlang I've been working on for most of my life is Vel Droj, and I plan to use this app to scaffold parts of it.

From a learning perspective, this project allowed me to exercise:
- RESTful APIs with Django
- UI Design with Bootstrap
- Docker containerization
- HTMX and AJAX
- SQL and Database Design

Coming from an embedded background, it was great to be able to make a foray into full-stack work.

## Installation Instructions
The project features both a .venv and a docker container, so until it is deployed, it can be used sandboxed and locally. 

### .venv route
Make sure you're in 
pip install -r requirements.txt
npm install
python manage.py startserver

Then just click the URL and conlang away!

### Docker Route


## Usage
Start by uploading texts. This is a conlanging app optimized for top-down conlanging as opposed to a-priori conlanging, so throw a bunch of words at it! You can also upload from a file. A list of stored texts will be maintained.

From here, click the text itself. Click a single word or highlight a string of words and submit it as a vocabulary entry to be looked at later, a grammar note as a quick example of some piece of grammar, or find glyphs to map them to phonology later. From here, it becomes easier to make a vocabulary list and a grammar top-down as well as note your writing system.

## Examples / Demos

## Links to Docs
Link to database diagram (requires lucidchart login): https://lucid.app/lucidchart/57959c10-764d-400c-8314-22905168a14b/edit?viewport_loc=-2701%2C-1404%2C3954%2C2272%2C0_0&invitationId=inv_b9009b8d-4dc6-441f-8724-250e14901b9c

## Potential Features for Future
Deployed online in addition to containerization and usage of PostgreSQL