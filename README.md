# Demo Intro to Flask

This is a demo of Flask for a standalone lecture in an intro to web dev class.

----
# Notes

* We've seen PHP, but there's many other languages/frameworks for web apps out there.
  * PHP is widely used by Facebook.

# What is [Flask](http://flask.pocoo.org/)?

"Flask - a microframework for Python based on Werkzeug, Jinja 2 and good intentions."

# Who Uses it?

* Pinterest - Social media site
  * Uses for apis - over 12 billion requests per day
* Twillio uses for apis - Text messaging, VOIP, etc in the cloud
* LinkedIn uses internally

# Why use it?

* Speed and ease of development
* "Fast enough" performance

# Demo
## Setup

1. Install some needed packages

```sh
sudo apt-get update
sudo apt-get install python-dev python-pip virtualenvwrapper git
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
git clone https://github.com/Graham42/flask-tutorial flask-intro
cd flask-intro/
git checkout 1.0-Hello-World
```

3. Setup for this project: create virtual python environment, install Flask

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
a terminal window.

```sh
workon flask-demo
python server.py
```

You should be able to view this webpage at [http://localhost:3000](http://localhost:3000)

Tag: 1.0 - Hello World

## Building our HTML

[The Jinja documentation](http://jinja.pocoo.org/docs/dev/templates/) has an example of what Jinja
looks like. This is what we'll be using in our HTML files.

Tag: 1.1 - If demo
Tag: 1.2 - Loop demo

## Routing

Unlike PHP our pages don't need to end in `.php`. Let's add another page. First, in our
`demo_app/__init__.py`

```python
@app.route('/other_page/')
def other():
    return render_template('other_page.html')
```

Then add the html file. Can see this other page when we go to
[/other_page](http://localhost:3000/other_page).

About this html file, we now have a bunch of shared code between our main page and this other one.
Jinja let's us create a base page and extend it. Good programmers look for abstractions,
opportunity to remove code duplication!

Tag: 1.3 - Other page demo
Tag: 1.4 - Template inheritance

### Variables in URLs

Cool thing that is hard to do in PHP.

Tag: 1.5 - News

### Error pages

[More about error pages](http://flask.pocoo.org/docs/0.10/patterns/errorpages/)

Might have broken links, or maybe someone tries to go to a page that doesn't exist.

Tag: 1.6 - Error handling

# Out of Time Thoguhts

Can do GET, POST, etc easily. Flask is well documented.

Many python libraries available to access whatever database you want, MySQL, PostgreSQL, etc

If I've peaked your interest, should definitely check out the [Flask Mega
Tutorial](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)

