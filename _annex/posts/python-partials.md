title: Python's Partials
date: 2014-08-19 12:00:00
has_mathjax: 1
has_pygments: 1

I've been abstaining myself from reddit for a while to get some other things
done and I recently decided to catch up on the [programming subreddit][1] news
en masse.

One of the interesting posts I came across was ["The Great White Space
Debate"][2]. It was an eloquent post on a dry programming topic; however, the
python script the author posted in the article piqued my attention. The script
locates the Java source files within a root project directory and then
identifies, counts, and summarizes the various for loop styles used within
them.  

Here is the script taken from the blog post:

    #!python
    import os
    import re
    from functools import partial
    
    def get_java_src_files(java_root):
        for root, _, files in os.walk(java_root):
            yield from (os.path.join(root, f) for f in files
                        if f.endswith('.java'))
    
    def read_files(filenames):
        for filename in filenames:
            with open(filename, 'r', encoding='utf-8') as f:
                yield from f.readlines()
    
    def extract_forloops(lines):
        yield from (
            line.strip() for line in lines
            if 'for (' in line
            # One of those god forsaken 'enhanced' for loops. Ignore
            and ':' not in line
        )
    
    if __name__ == '__main__':
        spaced_apart = partial(re.search, '[a-zA-Z]\s\=')
        grouped_together = partial(re.search, '[a-zA-Z]\=')
    
        java_src_path = r'C:\Program Files\Java\jdk1.8.0_20\src'
    
        forloops = extract_forloops(read_files(get_java_src_files(java_src_path)))
    
        counts = ('spaced': 0, 'nonspaced' : 0)
        for loop in forloops:
            if grouped_together(loop):
                counts['nonspaced'] += 1
            elif spaced_apart(loop):
                counts['spaced'] += 1
        print(counts)

I was interested in how this script was written.  The script is liberally
using two aspects of python's functional features: _generators_ and
_[partials][4]_.

Partials
--------

The `f(args)` operator is used to make a function call on function `f`.
Each argument to a function is an expression.  Before the function get
executed, all of the argument expressions are evaluated from left to
right.  This is known as _application order evaluation_.

It is possible to partially evaluate function arguments using the
`partial()` function from the `functools` module.  For example:

    :::python
    def foo(x, y, z):
        return x + y + z

    from functools import partial
    fn = partial(foo, 1, 2)  # supply values to foo's x and y arguments 
    fn(3)                    # calls foo(1,2,3), result is 6

The `partial()` function preemptively evaluates some of the arguments to
a function, and returns an object that you can call to supply the
remaining arguments at a later point. 

In the above example, the variable `fn` represents a partially evaluated
function where the first two arguments, `x` and `y` are already supplied and
evaluated.  The third argument, `z`, is given later on the next line. The
function is then complete and executed, yielding a result of 6.

Partial evaluation of function arguments is closely related to
_[currying][3]_, a functional programming technique where a function
taking multiple arguments is decomposed into a series of functions each
taking only one argument. For example, given a function `f(x,y)`, you
partially evaluate `f` by fixing `x` to get a new function to which you
give values of `y` to produce a result.  

[1]: http://www.reddit.com/r/programming 
[2]: https://medium.com/@thechriskiehl/the-great-white-space-debate-3633cba8b5c1
[3]: http://en.wikipedia.org/wiki/Currying
[4]: https://docs.python.org/2/library/functools.html#functools.partial
