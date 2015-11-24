from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    my_stuff = [
        ('friend', 'Bob'),
        ('dog', 'Tess'),
        ('cat', 'Tiger')
    ]
    return render_template('home.html',
        things=my_stuff,
        show_flask_logo=True
    )
