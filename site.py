from _annex import main

@main.manager.command
def freeze():
    main.freezer.freeze()

if __name__ == '__main__':
    main.manager.run()
