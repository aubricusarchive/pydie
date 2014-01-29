# PyDie

Uses '[quantum](https://qrng.anu.edu.au/)' random numbers to generate a result from an n-numbered 'roll' from an n-sided die adding any specified modifiers.

## Version
0.2.0 (pre-alpha)

## Dependencies
1. [Docopt](http://docopt.org/) – Command Line Interface

## Installation

Install pip? See: [How to install Pip.](http://guide.python-distribute.org/installation.html#pip-installs-python-pip)

Then simply:

`pip install pydie`

## Usage

**Note:**
The command arguments have been simplified since the last version (0.1.7). In fact, there are **no arguments at all!** The argv is now super simple, see the usage below for examples.

Current usage pattern:

```python
"""Usage:
    pydie roll [-r|--result-info] <roll>...
    pydie (-v | --version)
    pydie (-h | --help)

    Description:

        Generate a random n-sided for n-die roles.

    Commands:

        roll  Roll any kind of die to receive a randomized dice roll.

              - Roll command format {multiplier}{die}[m{modifiers}]...
              - Multipler is required, min 1; 0 will cause error
              - "m" is required when specifying modifiers
              - "+", plus, or "-", minus, is required before each modifier

    Examples:

        1d3                (single roll no mods)
        2d4m+1             (single roll mod)
        3d6m-1+3           (single roll with multi-mods)
        4d8m+2 5d12m+1-2+3 (multi roll, separated with a space)

    Options:
        -r --result-info    Display full result information (optional)
        -v --version        Display the version number
        -h --help           Display this screen
"""
```

## Backstory

**"Goddamnit! I rolled a 1 again!"**

Unsatisfied with an implementation of a 'random' die rolling bit of an online Dungeons & Dragons service I decided to *roll* my own. (pun intended)

I wondered, "How can I get truly random numbers?" While the respective `random` module is well endowed and probably good enough, what's the point if I simply type `random` and call it a day? Besides, I know that computer generated random numbers are really only [pseudorandom](http://en.wikipedia.org/wiki/Pseudorandom_number_generator) numbers anyway and that just makes me feel dirty inside. Unacceptable!

No, to truly achieve greatness I'll need numbers as random as I can get. But how?! Well I'll tell you how. Introducing the [ANU Quantum Random Number Server](http://qrng.anu.edu.au/index.php). Here's a bit from their homepage:

> Welcome to the ANU Quantum Random Numbers Server

>This website offers true random numbers to anyone on the internet. The random numbers are generated in real-time in our lab by measuring the quantum fluctuations of the vacuum. &hellip; By carefully measuring these fluctuations, we are able to generate ultra-high bandwidth random numbers.

Eureka! Now that I have random numbers, all I needed was to employ a bit of [docopt](http://docopt.org/) [read: amazing] magic, some dogey math and I'll have a niftly (likely useless) little commandline tool!

## Credits

There was a project(s) where I borrowed code to access the ANU server API and calculate an int within a range (from an ANU result).

Unfortunately I can't seem to remember from whom I was inspired. If you come across this and you think you contributed, please send me a message so I can give proper attribuition!

## Disclaimer

Ok, full-disclosure, I majored in something other than math and probability is hard. So instead, I borrowed this example from [ANU's Site](http://qrng.anu.edu.au/index.php). Through completely unscientific means I have judged this technique acceptable:

> Put N balls into a bag numbered between Minimum number and Maximum number. Mix the balls thoroughly. Pick out one ball and write down its number. Repeat the process m times (either with replacement or without replacement).

> – <http://qrng.anu.edu.au/Lucky.php>
