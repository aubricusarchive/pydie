# PyDie

Uses '[quantum](https://qrng.anu.edu.au/)' random numbers to generate a result from an n-numbered 'roll' from an n-sided die.

## Version
0.1.7 (pre-alpha)

## "Goddamnit! I rolled a 1 again!"

Unsatisfied with an implementation of a 'random' die rolling bit of an online Dungeons & Dragons service I decided to *roll* my own. (pun intended)

I wondered, "How can I get truly random numbers?" While the respective `random` module is well endowed and probably good enough, what's the point if I simply type `random` and call it a day? Besides, I know that computer generated random numbers are really only [pseudorandom](http://en.wikipedia.org/wiki/Pseudorandom_number_generator) numbers anyway and that just makes me feel dirty inside. Unacceptable! 

No, to truly achieve greatness I'll need numbers as random as I can get. But how?! Well I'll tell you how. Introducing the [ANU Quantum Random Number Server](http://qrng.anu.edu.au/index.php). Here's a bit from their homepage:

> Welcome to the ANU Quantum Random Numbers Server

>This website offers true random numbers to anyone on the internet. The random numbers are generated in real-time in our lab by measuring the quantum fluctuations of the vacuum. &hellip; By carefully measuring these fluctuations, we are able to generate ultra-high bandwidth random numbers.

Eureka! Now that I have random numbers, all I needed was to employ a bit of [docopt](http://docopt.org/) [read: amazing] magic, some dogey math and I'll have a niftly [likely useless] little commandline tool!

## Installation

Install pip? See: [How to install Pip.](http://guide.python-distribute.org/installation.html#pip-installs-python-pip)

Then simply:

`pip install pydie`

## Usage
The current usage pattern looks like this:
```python
"""Usage: pydie roll <multiplier> <die> [<modifier>]
          pydie [-h | --help]

Generate a random n-sided dice role.

Options:
    -h --help  print help information for this program

"""
```
The command arguments are simple:

```bash
<multiplier> # required, essentially the number of die you are rolling, usually a number between 1-9`
<die>        # required, they 'type' of die you are rolling, e.g., "d20"
[<modifier>] # optional, any bonuses or penalties to modify your roll, e.g., "+3+2-1"
```
An example roll looks a lot like this:
```bash
pydie roll 2 d4 +1
```

And might output something like:
```bash
Rolling 2 d4s

Your result is 4!
Your original rolls were [1, 2]
Your original total was 3
You applied the following modifiers +1
```

## Dependencies
1. [Docopt](http://docopt.org/) – Command Line Interface

## Credits
There was a project(s) where I borrowed code to access the ANU server API and calculate an int within a range (from an ANU result). 

Unfortunately I can't seem to remember from whom I was inspired. If you come across this and you think you contributed, please send me a message so I can give proper attribuition!

## Disclaimer
Ok, so this little toy in no way calculates the 'actual' probability of a certain die roll. I'm sure that to be 'truly' accurate it should probably account for that in some way. But, you know, that sounds like a lot of math and I'm not exactly a math major. 

Let's just say this boils down to a fancy random number generator that allows you to specify a range.

If you are good at math and my blatant disregard for accuracy has insensed your sensibilities feel free to comment! 
