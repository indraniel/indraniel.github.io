title: Appreciating Long-Tailed Distributions
date: 2016-05-29 09:00:00
has_mathjax: 0
has_pygments: 0

[Long-Tailed Distributions][1] (or power-law distributions) are everywhere; they're especially observable in the social sciences, for example: 

* **[Wealth Distribution][a]**: a select few people control most of the [wealth][5]
* **[Social Media and Networks][b]**:  famous people have thousands of times more followers than the average user.
* **[Market Dominance][c]**:  [Amazon][d] is much larger than the next few internet retailers by revenue
* **[Internet Infrastructure][e]**:  many [DevOps][2] and computer infrastructure related issues have long tails

While these distributions are common, they always feel [suprising][3], and [mysterious][4].  

> "Despite a century of scientific familiarity, samples drawn from Pareto distributions are routinely presented to the public as anomalies, which prevents us from thinking clearly about the world.
>
> &mdash; Clay Shirky from <cite><a href="http://gu.com/p/2mdgz/stw">The Guardian</a></cite>

Below is a video I recently encountered explaining them.

<span class='embed-youtube' style='text-align:center; display: block;'>
<iframe width="560"
        height="315"
        src="https://www.youtube.com/embed/F-I-BVqMiNI"
        frameborder="0"
        allowfullscreen>
</iframe>
</span>

I really like this video because of how it gives a very intuitive reason why these distributions arise.  Additionally, it also gives an better notion of how a "winners become winners" scheme eventually leads to a power-law distributions.

It's also important to remember that the converse isn't true:  observing a power-law doesn't always mean that it was generated by a "winners become winners" scheme.  For example, in computer networking, data packet arrival times oven follow a long-tailed distribution, but the packets aren't generated from a "winners become winners" scheme.

[0]: https://www.theguardian.com/science/2011/jan/15/uncertainty-failure-edge-question
[1]: https://en.wikipedia.org/wiki/Heavy-tailed_distribution
[2]: https://theagileadmin.com/what-is-devops/
[3]: http://users.cms.caltech.edu/~adamw/papers/2013-SIGMETRICS-heavytails.pdf
[4]: http://web.stanford.edu/~ashishg/msande235/spr08_09/Lecture07.pdf
[5]: http://krugman.blogs.nytimes.com/2014/04/25/piketty-and-pareto/
[a]: http://www.theguardian.com/commentisfree/2011/nov/11/occupy-movement-wealth-power-law-distribution
[b]: https://twitter.com/potus?lang=en
[c]: https://www.theguardian.com/technology/2015/dec/12/ratio-technology-mozilla-firefox-os-90-9-1
[d]: http://www.amazon.com
[e]: https://blog.optimizely.com/2013/12/11/why-cdn-balancing/
[-1]: http://www.brendangregg.com/FrequencyTrails/mean.html
