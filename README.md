# PyDie

[![Latest Version](https://img.shields.io/pypi/v/pydie.svg)](https://pypi.python.org/pypi/pydie/)
[![Downloads](https://img.shields.io/pypi/dm/pydie.svg)](https://pypi.python.org/pypi/pydie/)

Uses '[quantum](https://qrng.anu.edu.au/)' random numbers to generate a result from an n-numbered 'roll' from an n-sided die adding any specified modifiers.

## Dependencies
1. [Docopt](http://docopt.org/) – Command Line Interface

## Installation

Install pip? See: [How to install Pip.](http://guide.python-distribute.org/installation.html#pip-installs-python-pip)

Then simply:

`pip install pydie`

## Usage

You can use this package from the cli or within python.

To use it within python:

```python
import pydie

pydie.roll('1d3', '2d6', '3d12+2')

# should return something like:
# [
#   {
#     'raw': [1],
#     'modifiers': [],
#     'multiplier': '1',
#     'die': '3',
#     'rolls': [1],
#     'argv': '1d3'
#   },
#   {
#     'raw': [1, 1],
#     'modifiers': [],
#     'multiplier': '2',
#     'die': '6',
#     'rolls': [1, 1],
#     'argv': '2d6'
#   },
#   {
#     'raw': [1, 12, 5],
#     'modifiers': ['+2'],
#     'multiplier': '3',
#     'die': '12',
#     'rolls': [3, 14, 7],
#     'argv': '3d12+2'
#   }
# ]
```

Current cli usage pattern:

```python
"""Usage:
    pydie roll [-r|--result-info] <roll>...
    pydie (-v | --version)
    pydie (-h | --help)

    Description:
        Generate a random n-sided for n-die roles.

    Commands:
        roll  Roll any kind of die to receive a randomized dice roll.
              - Roll command format {multiplier}{die}[{modifiers}...]...
              - Multipler is required, min 1; 0 will cause error
              - "+", plus, or "-", minus, is required before each modifier

    Examples:
        pydie roll 1d3               (single roll no mods)
        pydie roll 2d4+1             (single roll mod)
        pydie roll 3d6-1+3           (single roll with multi-mods)
        pydie roll 4d8+2 5d12+1-2+3  (multi roll, separated with a space)

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

## Other Projects

- <https://pypi.python.org/pypi/quantumrandom/>
- <https://github.com/pcragone/anurandom>

## Disclaimer

Ok, full-disclosure, I majored in something other than math and probability is hard. So instead, I borrowed this example from [ANU's Site](http://qrng.anu.edu.au/index.php).

> Put N balls into a bag numbered between Minimum number and Maximum number. Mix the balls thoroughly. Pick out one ball and write down its number. Repeat the process m times (either with replacement or without replacement).

> – <http://qrng.anu.edu.au/Lucky.php>

Through completely unscientific means I have judged this technique acceptable.

## Changelog

### 0.2.5
- Removed "m" from roll argv
- Added better cli errors

### 0.2.4
- Fixed bug in version util that was breaking install
- Added docstrings

### 0.2.3
- Added a more convenient "roll" method for use in python

### 0.2.1
- Refactored roll handling out of cli.py

### 0.2.0
- Major refactor
- Added multiroll
- Simplified roll argv
