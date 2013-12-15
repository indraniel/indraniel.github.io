from _annex import main

@main.manager.command
def freeze():
    "Render the posts to static html files"
    main.freezer.freeze()

if __name__ == '__main__':
    main.manager.run()
