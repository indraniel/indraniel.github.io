title: Python's Functional Features - Partials & Generators
date: 2014-08-19 12:00:00
has_mathjax: 1
has_pygments: 1

I've been abstaining myself from reddit for a while to get some other things
done and I recently decided to catch up on the [programming subreddit][1] news
en masse.

One of the interesting posts I came across was ["The Great White Space
Debate"][2]. It's an eloquent post on a dry programming topic; however, the
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

Being a python neophyte, I was interested in how this script was written.  The
script is liberally using two aspects of python's functional features:
 _[partials][4]_ and _[generators][5]_.

Partials
--------

### Theory

The `f(args)` operator is used to make a function call on function `f`.
Each argument to a function is an expression.  Before the function gets
executed, all of its argument expressions are evaluated from left to
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

### Practice

In the Java for loop identifying code the author creates partially evaluated functions on lines 24-25:

    :::python
    spaced_apart = partial(re.search, '[a-zA-Z]\s\=')
    grouped_together = partial(re.search, '[a-zA-Z]\=')

and invokes them on the `if` statements on lines 33 and 35:

    :::python
    if grouped_together(loop):
        counts['nonspaced'] += 1
    elif spaced_apart(loop):
        counts['spaced'] += 1

The author is using the partials as a way to "label" his regular expression through descriptive and readable function variable names.  An interesting approach!

Generators
----------

### Theory

Whenever a function uses the `yield` keyword, it defines a _generator_ object.  A generator is a function that produces a sequence of values for use in iteration.  For example,

    :::!#python
    def countdown(n):
        print("Counting down from {}".format(n))
        while n > 0:
            yield n
            n -= 1
        return

If you define the above function in a REPL and execute it, like so:

    >>> c = countdown(5)

you'll notice that none of the code gets executed.  Instead `countdown` returns a generator object which is assigned to variable `c`.  The generator object will begin to execute the function only when the `next()` method is applied to it like so:

    >>> c.next()  # "it's c.__next__ in Python 3.x"
    Counting down from 5
    5

On the first call to `next()`, the generator function executes statements until it reaches a `yield` statement.  The `yield` statement produces a result at which point execution of the function stops until `next()` is invoked again.  Subsequent `next()` calls resumes executing the function starting with the statement following `yield`. Continuing with our running example, a second call to `next()` will behave like:


    >>> c.next()
    4

In python, you don't normally call `next()` directly; rather, it's called indirectly via a `for`, or some other operation that works on a sequence.

A generator function signals its completion by returning or raising a `StopIteration` exception.  Afterwards, continued `next()` calls should always return `None`.

#### Warning

A subtle problem with generators happens when a generator is partially consumed.  An example scenario is:

    for n in countdown(5):
        if n == 2: break
        # otherwise, do more stuff...

Here, the `for` loop aborts when "n" becomes equal to 2, however, the associated generator never fully completes.  When a generator is no longer used, or gets deleted once out of scope, a generator method named `close()` is invoked.  Normally it's not necessary to call `close()` directly, but you can call it manually like so:

    >>> c = countdown(5)
    >>> c.next()
    Counting down from 5
    5
    >>> c.next()
    4
    >>> c.close()
    >>> c.next()
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    StopIteration

A much more through description of python's generator feature is described [here][6].

### Practice

Generators are a powerful way to write pythonic programs that are based on processing data streams of unknown size and limit.

In the Java code parsing example, the `yield` statement is called in all three of the functions defined in the script.  This approach is useful because we have an unknown data stream --  for any given Java project one doesn't know how many Java source files there are, and how many lines are in each source file.  Rather than loading everything up initially, we can lazily load up the source files and its line contents as needed.

[1]: http://www.reddit.com/r/programming 
[2]: https://medium.com/@thechriskiehl/the-great-white-space-debate-3633cba8b5c1
[3]: http://en.wikipedia.org/wiki/Currying
[4]: https://docs.python.org/2/library/functools.html#functools.partial
[5]: https://docs.python.org/2/howto/functional.html#generators
[6]: https://www.jeffknupp.com/blog/2013/04/07/improve-your-python-yield-and-generators-explained/
