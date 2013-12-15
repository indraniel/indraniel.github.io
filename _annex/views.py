from flask import render_template, url_for, redirect, request
from app import app, pages
from werkzeug.contrib.atom import AtomFeed

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
    feed = AtomFeed('Articles', feed_url=request.url, url=request.url_root)
    pages = sorted_posts()
    for page in pages:
        feed.add(
            page.meta['title'],
            page,
            content_type='html',
            author=page.meta.get('author', 'indraniel'),
            url='/'.join([app.config['FREEZER_BASE_URL'], page.path]),
            updated=page.meta['date'],
        )
    return feed.get_response()
