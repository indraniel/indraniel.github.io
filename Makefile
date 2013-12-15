POSTS=$(shell find _annex/posts -maxdepth 1 type -f -name "*.md")
POST_DIRS=$(shell find _annex/posts -maxdepth 1 -name "*.md" -exec basename -s .md -a {} \;)

posts: $(POSTS)
	. venv/bin/activate
	python site.py freeze

clean:
	find . -path ./venv -prune -o -name "*.pyc" -print -exec rm -rf {} \;

cleanall:
	find . -path ./venv -prune -o -name "*.pyc" -print -exec rm -rf {} \;
	rm -rf $(POST_DIRS) pages static index.html all.rss.xml
