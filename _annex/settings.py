import os

def parent_dir(path):
    return os.path.abspath(os.path.join(path, os.pardir))

BLOG_TITLE = "Indraniel's Notebook" 

REPO_NAME = ''
DEBUG = True

# Assume that the Flask app is located in the same directory
# as this settings.py file
APP_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = parent_dir(APP_DIR)

# Where we're going to dump the static blog pages to
FREEZER_DESTINATION = PROJECT_ROOT

FREEZER_BASE_URL = 'http://localhost/%s' % (REPO_NAME)

# Don't remove the Flask code when we run the freezer!
FREEZER_REMOVE_EXTRA_FILES = False

FLATPAGES_MARKDOWN_EXTENSIONS = ['codehilite']

# Location of the raw blog texts
FLATPAGES_ROOT = os.path.join(APP_DIR, 'posts')
FLATPAGES_EXTENSION = '.md'
