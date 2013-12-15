from flask import render_template, url_for, Response
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
    print 'Path is: %s' % path
    page = pages.get_or_404(path)
    print 'Page is: %s' % page
    return render_template('page.html', page=page)

@app.route('/pages/about/')
def about():
    page = pages.get_or_404('pages/about')
    return render_template('page.html', page=page)

@app.route('/all.rss.xml')
def rss_feed():
    posts = sorted_posts()
    feed = render_template('feed.xml', posts=posts)
    return Response(feed, mimetype='application/xml')
