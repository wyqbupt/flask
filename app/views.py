from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
<<<<<<< HEAD
    user = { 'nickname': 'Miguel' } # fake user
=======
    user = { 'nickname': 'WWW' } # fake user
>>>>>>> 5220773baf4aea2b663c4b3c2abe63cd8b6da05e
    posts = [ # fake array of posts
        {
            'author': { 'nickname': 'John' },
            'body': 'Beautiful day in Portland!'
        },
        {
<<<<<<< HEAD
            'author': { 'nickname': 'Susan' },                                              'body': 'The Avengers movie was so cool!'
                                                                                        }
    ]
    return render_template("index.html",                                                    title = 'Home',
            user = user,
=======
            'author': { 'nickname': 'Susan' },
            'body': 'The Avengers movie was so cool!'                               }
    ]
    return  render_template("index.html",
            title = 'Home',
            user = user ,
>>>>>>> 5220773baf4aea2b663c4b3c2abe63cd8b6da05e
            posts = posts)

