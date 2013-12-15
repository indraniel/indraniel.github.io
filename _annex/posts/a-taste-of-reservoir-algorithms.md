title: A Taste of Reservoir Algorithms
date: 2010-08-10 12:00:00
has_mathjax: 1

<center>
<img alt="A Chocolate Sampling" src="http://farm1.static.flickr.com/15/68153223_665dbdf47d_m.jpg">
</center>

Imagine that you are the Chief Chocolate Inspector of a chocolate factory. Your
job is to ensure that the days production of chocolate by the factory is of
good quality. Only upon your recommendation will the factory be shipping out
its days worth of chocolate production to its distribution points.

The chocolate factory consists of three adjacent rooms connected together by a
conveyor belt/assembly line.

The first room is where the chocolate pieces are produced and initially placed
onto the conveyor belt. The factory produces a variety of decadent chocolate
types simultaneously and randomly places each type onto the conveyor belt.

The second adjoining room is where each of the individual chocolate pieces get
wrapped up. Afterwards, you are given a choice whether to choose that
particular piece for taste inspection, or ignore it and wait for the next one.

The final adjoining room is where the chocolate pieces get packaged together in
boxes and loaded onto the delivery trucks. The trucks only move upon your
decision at the end of the day.

Your goal, as the Chief Inspector, is to notify the truck drivers if the
packages are suitable for shipping in as efficient manner as possible. Armed
with a special selection bin to hold $n$ pieces of chocolate, you decide to
choose $n$ uniformly random pieces of chocolate out the $N$ total pieces of
chocolate produced by the factory throughout the day, where $n<<N$. Afterwards,
you base your taste decision on this random subset.

Unfortunately, you have no idea as to how many chocolate entities will be
passing by on any given day. Some days, the amount of chocolate produced by the
factory is very high, on others it is pretty low. In other words, you do not
know what $N$ is beforehand.

While you could wait to make the sampling after the days production is done;
you don’t want to hold up the assembly line making these quality control
choices. "[I Love Lucy][1]" has shown what kind of hijinks can happen if this
process goes awry.

<span class='embed-youtube' style='text-align:center; display: block;'>
<iframe class='youtube-player' type='text/html' width='520' height='323' src='http://www.youtube.com/embed/8NPzLBSBzPI?version=3&#038;rel=1&#038;fs=1&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;wmode=transparent' frameborder='0'></iframe>


What to do?
-----------

One solution to this problem might be to roll a die as each chocolate piece
passes you. If the die rolls even, hold the chocolate for inspection in the
selection bin. Otherwise, let the chocolate pass through. If the selection bin
is full when choosing a chocolate piece, simply replace the oldest chocolate
piece in the bin with the new one.

In this naïve approach, one is biased against keeping the earliest chocolate
samples with the ones selected later in the day. To resolve this issue, you can
use a loaded die or get more "[Dungeons & Dragons][2]"-esque by using more
sophisticated dice and rules as the day progresses.

<center>
<img alt="Multifaced dice" src="/static/images/multifaced-dice.jpg">
</center>

Then with some luck, you could get a uniform sampling of the days production of
chocolate.

But there is a better way...

A Smarter Way
-------------

Suppose you could assign a uniform random \([i.i.d][3] of course!\) number from
$\[0,1\)$ to each piece of chocolate you encounter on the assembly line.

Now, to obtain a sampling of the days production of chocolate, simply choose
the chocolates corresponding to the $n$ lowest random numbers linked with them.
Each chocolate piece has an equal chance of being in the lowest $n$ choices, so
the sampling is uniform.

With the ubiquitous computing power available these days, you could substitute
using dice with a [iPhone][4] or [Android][5] app to help out. Each time you see a new
chocolate piece, generate a random number with your app. Hold onto the
chocolate pieces that correspond to the $n$ lowest random numbers. If you
encounter a new chocolate piece that is linked with a random number that is
lower than the largest random number associated chocolate already in your
selection bin, simply replace the old one with the new one.

By the end of the process you now have $n$ uniform samples of the entire days
chocolate production, and you never needed to hold onto more than those $n$
items. Pretty clever, eh!

This approach could be optimized even further. For example, you could
preemptively generate a large list of random numbers; identify the lowest ones;
and afterwards directly choose those chocolate pieces as they appear off the
production line and bypass the rest.

Amazingly, you could sample the entire days production of chocolates, $N$, in
less than $O\(N\)$ time. According to this [fellow][6], you can make the
process $O\(n\(1+log\(N/n\)\)\)$ efficient.

These techniques of sampling a set of unknown size through one pass are called
_[reservoir algorithms][7]_.

The "Real" World
----------------

While most of us are not chocolate inspectors, we are all nowadays swamped in a
"sea of data", from [science][8] and [business][9] to [personal tracking][10].
Often times these raw data sets come in large chunks. One data-mining technique
to get a better handle of the data is sampling it. Sometimes less is more. Now
chocolate pieces become record sets and the assembly line becomes a large file.

Reservoir algorithms can be a useful tool in one’s data [science &
engineering][11] endeavors.



[1]: http://en.wikipedia.org/wiki/I_Love_Lucy
[2]: http://en.wikipedia.org/wiki/Dungeons_%26_Dragons
[3]: http://http://en.wikipedia.org/wiki/Independent_and_identically_distributed_random_variables
[4]: http://www.apple.com/iphone/apps-for-iphone/
[5]: http://www.android.com/market/
[6]: http://www.cs.umd.edu/~samir/498/vitter.pdf
[7]: http://en.wikipedia.org/wiki/Reservoir_sampling
[8]: http://www.nytimes.com/2009/12/15/science/15books.html
[9]: http://bits.blogs.nytimes.com/2010/07/26/bringing-data-mining-into-the-mainstream/
[10]: http://online.wsj.com/article/NA_WSJ_PUB:SB122852285532784401.html
[11]: http://radar.oreilly.com/2010/06/what-is-data-science.html
