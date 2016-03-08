title: Counting 101 - Permutations & Combinations
date: 2013-12-26 12:00:00
has_mathjax: 1

<center>
    <img alt="Sesame Street's 'The Count'" src="https://static-secure.guim.co.uk/sys-images/Media/Pix/pictures/2009/11/9/1257758922191/Sesame-Street-the-Count-001.jpg">
</center>

_I always forget the fundementals of counting.  Hopefully this post can serve as useful reminder for me._

If you have three socks, two pairs of pants and four shirts, how many outfits
can you wear? Counting questions like this happen a lot in the everyday world.
*[Combinatorics][2]*, the mathematics of counting, can help in answering these
questions.

Counting can be organized into two cases: _permutations_ and _combinations_.
The difference between the two is the _order_ of things you are counting.  If
the order doesn't matter, it's a **combination**.  If order does matter, it's a
**permutation**.  

Combinations and permutations can be illustrated with these two examples:

* **"I'm having a Bacon-Lettuce-Tomato Sandwich today."**  You don't care what
  order the Bacon, Lettuce and Tomato are placed onto the sandwich, it'll
  still be the same type of sandwich.

* **"The combination to the safe was 496"**.  Here you definitely care about the
  order.  "649" and "694"  wouldn't open the safe; it has to be exactly
  **4-9-6**.
    
    <center>
    <figure>
        <img src="http://ecx.images-amazon.com/images/I/411FE4A25ZL._SY300_.jpg">
        <figcaption>
        Combination Locks should really be called "Permuation Locks"!
        </figcaption>
    </figure>
    </center>

Think of _"**P**ermutation is **P**osition"_ as a useful mnemonic to help you
distinguish between the two cases.

Permutations
------------

Within permutations there are two types: _repetition_ and _no repetition_.

* _Repetition_ happens when items _can_ be counted more than once.  For example, a
  three-digit combination to a safe could be "333".

* _No repetition_ happens when items _cannot_ be counted more than once.  For
  example, the first three people in a sports competition; a person can't be
  ranked both first _and_ second.

### Permutations with Repetition

These are the easiest to count up.  When you have $n$ things to choose from,
you have $n$ choices each time!  When choosing $r$ of them, the permutations
are:

<div class="well">
$$ n * n * ... (r \text{ times}) $$
</div>

In more common english, there are $n$ possibilities for the first choice, then
$n$ possibilities for the second choice, and so on for $r$ times.

> <b>Example:</b>
> 
> For the 3 combination safe, there are 10 numbers to choose from (0-9), and you
> choose 3 of them. So there are:
> 
> $$ 10 * 10 * 10 = 10^3 = 1,000 \text{ permutations} $$

### Permutations without Repetition

Without repetition happens in situations, when you can't reuse things that have
already been chosen. In this case, you have to _reduce_ the number of choices
available to you after each selection. 

<center>
<img alt="Ice Cream Flavors" src="https://usatftw.files.wordpress.com/2015/09/olympic-winners-podium-007.jpg">
</center>

For example, how many ways can you rank 5 people (Joe, Bob, Alice, Mary, &
Frank) in a race? After choosing, say, Frank, then you can't choose him again.
You'll have 4 people to choose from next (Joe, Bob, Alice & Mary).  The total
number of permutations would be:

$$ 5 * 4 * 3 * 2 * 1 = 120 $$

If you only wanted to choose the top 3, then that would be:

$$ 5 * 4 * 3 = 60 $$

Mathematically, choosing all permutations from a total set of $n$ things is given by:

<div class="well">
$$ n! $$
</div>

The "$!$" symbol is the *[factorial function][factorial]*.

Choosing a permutation of a subset of $r$ things from an overall set of $n$
things is given by:

<div class="well">
$$ \frac{n!}{(n - r)!} $$
</div>

You might be thinking where did the division arise from?  The best way I've
found to understand it is by thinking of the above top 3 race ranking example
in the following way:

The full permutation selections for the race rankings are given by $ 5! $.  The
top 3 are given by $ 5 * 4 * 3 $.  You have to stop multiplying after 3.  How
do you do that?  How about dividing the full permutation rankings by $ 2! $.
In other words,

$$ \frac{ 5 * 4 * 3 * 2 * 1 }{ 2 * 1 } = 5 * 4 * 3 = 60 $$

#### Notation

In general, nobody writes the above formula; people use a shorthand like this:

<div class="well">
$$ P(n,r) = {}_{n}P_{r} = \frac{n!}{(n -r)!} $$
</div>

> <b>Example:</b>
> 
> $$ P(5,3) = 60 $$

Combinations
------------

Similar to permutations, combinations have two flavors: _reptition_ and _no repetition_.

### Combinations without repetition

Combinations without repetition is like the lottery.  Numbers are drawn one at
a time, and if you have the lucky numbers (no matter the order) you win!

<center>
<img alt="Ice Cream Flavors" src="http://cdn.moneycrashers.com/wp-content/uploads/2008/04/lottery-balls-cash.jpg">
</center>

Consider the case when 3 numbers, say 1, 2, & 3 are chosen from a lottery
event.  The possibilities from choosing these number from three picks are:

<center>
  <table class="table table-condensed">
    <thead>
      <tr>
         <th>Ordering Does Matter (Permutations)</th>
         <th>Ordering Doesn't Matter (Combinations)</th>
      </tr>
    </thead>
    <tbody>
        <tr>
            <td>1, 2, 3</td>
            <td></td>
        </tr>
        <tr>
            <td>1, 3, 2</td>
            <td></td>
        </tr>
        <tr>
            <td>2, 1, 3</td>
            <td>1, 2, 3</td>
        </tr>
        <tr>
            <td>2, 3, 1</td>
            <td></td>
        </tr>
        <tr>
            <td>3, 1, 2</td>
            <td></td>
        </tr>
        <tr>
            <td>3, 2, 1</td>
            <td></td>
        </tr>
    </tbody>
  </table>
</center>

Notice how the permutation possibilities are 6 times or ($3!$ times) the
combination possibilities.

Intuitively, to get a count of the combination of things you need to
**reduce it** by the number ways things can be permuted.  So, mathematically we
can adjust the permutation formula as follows:

<div class="well">
$$ \frac{n!}{(n-r)!} * \frac{1}{r!} = \frac{n!}{r!(n-r)!} $$
</div>

The above combination formula occurs so frequently in the world of
combinatorics that it's given a few special short hand notations:

<div class="well">
$$ \frac{n!}{r!(n-r)!} = {n \choose r} = C(n,r)$$
</div>

and is read as *"$n$ choose $r$"*, where $n$ is the total number of things to
choose from and $r$ is the number of selections to choose from the set ( $r$
must be less than $n$).

It also worthwhile to note that the "$n$ choose $k$" formula is symmetrical.

<div class="well">
$$ \frac{n!}{r!(n-r)!} = {n \choose r} = {n \choose n-r}$$
</div>

In other words, the number of ways to choose 3 balls out of 5, is the same as
the number of ways to throw away 2 balls out of 5.

### Combinations with repetition

<center>
<img alt="Ice Cream Flavors" src="http://www.previewbd.com/admin/uploads/project_image/142772156320100401-ice-cream-parlor-600x411.jpg">
</center>

Let's pretend that there are 5 flavors of ice cream at the ice cream parlor:  mint, chocolate, lemon, strawberry, and vanilla.

We'd like to get a [banana split][1] with 3 scoops of ice cream. How many banana split variations are possible?

Let's use single letters for the flavors: `{m, c, l, s, v}`.

Example variations can be:

* `{c, c, c}` *(3 scoops of chocolate)*
* `{m, l, v}` *(a single scoop of mint, lemon, and vanilla)*
* `{m, v, v}` *(1 mint scoop, and 2 scoops of vanilla)*

There are **$n=5$** ice cream flavors to choose from, and we can choose any **$r=3$** of them.  _Order doesn't matter, and we can repeat!_

One way to reason about counting the number of scoop variations is to think of the ice creams being in a "train of boxes" like so:




Useful Tips
-----------

While this post explains the basic counting formulas, figuring out how to
interpret a real world situation and correctly applying the right formulas can
be hard.  This skill can be acquired through practice.

Combinatorial problems often require applying some logical thinking, and some
clever insight. When you encounter one, try to break down the problem into a
manageable number of familiar subproblems.  Divide and conquer.  This way
you're less likely to make a mistake.

[factorial]: http://en.wikipedia.org/wiki/Factorial
[1]: https://en.wikipedia.org/wiki/Banana_split
[2]: https://en.wikipedia.org/wiki/Combinatorics
