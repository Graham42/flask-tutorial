# Demo Intro to Flask

This is a demo of Flask for a standalone lecture in an intro to web dev class.

----
# Notes

* We've seen PHP, but there's many other languages/frameworks for web apps out there.
* PHP widely used by Facebook.


# Flask

"Flask - a microframework for Python based on Werkzeug, Jinja 2 and good intentions."


# Who Uses it?

* Pinterest - Social media site
  * Uses for apis - over 12 billion requests per day
* Twillio uses for apis - Text messaging, VOIP, etc in the cloud
* LinkedIn uses internally


# Why use it?

* Speed and ease of prototyping and development
* "Fast enough" performance


# Demo
## Setup

1. Install some needed packages

```sh
sudo apt-get update
sudo apt-get install python-dev python-pip virtualenvwrapper
cat >> ~/.bashrc << EOF
  export WORKON_HOME=$HOME/.virtualenvs
  export PROJECT_HOME=$HOME/dev
  source /usr/share/virtualenvwrapper/virtualenvwrapper.sh
EOF
source ~/.bashrc
```

2. Download the starting source code

```sh
mkdir -p ~/dev/
cd ~/dev/
wget BLAH_TODO_THING/flask-intro.tar.gz
tar -xzf BLAH_TODO_THING/flask-intro.tar.gz
cd flask-intro/
```

3. Setup for this project, create virtual python environment, install Flask

```sh
mkvirtualenv flask-demo
cd ~/dev/flask-intro
setvirtualenvproject
pip install Flask
deactivate
```

4. Any time you want to work on this project just run `workon flask-demo` to activate the virtual
   python environment we created for this project, which now has Flask installed


## Hello world

The starting code you've downloaded is a basic Hello World web app. To run this web app, let's open
a separate terminal window.

```sh
workon flask-demo
python server.py
```

