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

@app.route('/news/')
def news():
    with open('demo_app/headlines.txt') as f:
        headlines = [line.strip('\n') for line in f.readlines()]

    return render_template('news.html', headlines=headlines)

@app.route('/news/<headline>')
def news_post(headline):
    return render_template('news_post.html',
        title='Breaking News!',
        subtitle=headline)

# error pages
@app.errorhandler(404)
def page_not_found(e):
    return  render_template('404.html'), 404
