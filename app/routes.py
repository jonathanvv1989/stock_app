from flask import render_template
from app import app


@app.route("/")
@app.route("/index")
def index():
    user = {'username': 'Jonathan'}
    tips = [
        {
            'author': 'Warren Buffet',
            'body': 'I will tell you how to become rich. Close the doors. \
                     Be fearful when others are greedy. Be greedy when others \
                     are fearful.'
        },
        {
            'author': 'Peter Lynch',
            'body': 'Know what you own, and know why you own it.'
        }
    ]
    return render_template(
        'index.html', title='Home', user=user, tips=tips
    )
