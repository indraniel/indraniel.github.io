clean:
	find . -path ./venv -prune -o -name "*.pyc" -print -exec rm -rf {} \;
