from flask import render_template, url_for, Response
from flask_flatpages import pygments_style_defs
from app import app, pages

def sorted_posts():
    posts = [page for page in pages if 'date' in page.meta]
    sorted_posts = sorted(posts, reverse=True,
                                 key=lambda page: page.meta['date'] )
    return sorted_posts

@app.route('/')
def home():
    posts = sorted_posts()
    return render_template('index.html', pages=posts)

@app.route('/<path:path>/')
def page(path):
    print 'Generating post: %s' % path
    page = pages.get_or_404(path)
    return render_template('page.html', page=page)

@app.route('/pages/about/')
def about():
    page = pages.get_or_404('pages/about')
    return render_template('page.html', page=page)

@app.route('/pygments.css')
def pygments_css():
    return pygments_style_defs('pastie'), 200, {'Content-Type': 'text/css'}

@app.route('/all.rss.xml')
def rss_feed():
    posts = sorted_posts()
    feed = render_template('feed.xml', posts=posts)
    return Response(feed, mimetype='application/xml')
