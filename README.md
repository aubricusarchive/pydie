# PyDie

Uses '[quantum](https://qrng.anu.edu.au/)' random numbers to generate a 'roll' from an n-sided die.

## Version
0.1.0 (pre-alpha)

## "Goddamnit! I rolled a 1 again!"

Unsatisfied with an implementation of a 'random' die rolling bit of an online Dungeons & Dragons service I decided to *roll* my own. (pun intended)

I wondered, "How can I get truly random numbers?" While the respective `random` module is well endowed and probably good enough, what's the point if I simply type `random` and call it a day? Besides, I know that computer generated random numbers are really only [pseudorandom](http://en.wikipedia.org/wiki/Pseudorandom_number_generator) numbers anyway and that just makes me feel dirty inside. Unacceptable! 

No, to truly achieve greatness I'll need numbers as random as I can get. But how?! Well I'll tell you how. Introducing the [ANU Quantum Random Number Server](http://qrng.anu.edu.au/index.php). Here's a bit from their homepage:

> Welcome to the ANU Quantum Random Numbers Server

>This website offers true random numbers to anyone on the internet. The random numbers are generated in real-time in our lab by measuring the quantum fluctuations of the vacuum. &hellip; By carefully measuring these fluctuations, we are able to generate ultra-high bandwidth random numbers.

Eureka! Now that I have random numbers, all I needed was to employ a bit of [docopt](http://docopt.org/) [read: bloddy f*cking amazing] magic, some dogey math and I'll have a niftly [likely useless] little commandline tool!

## Installation
Note: Installation is slightly untested at the moment.

`pip install pydie`

## Usage
The current usage pattern looks like this:
```python
"""Usage: pydie.py roll <multiplier> <die> [<modifier>]
          pydie.py [-h | --help]

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
pydie.py roll 2 d6 +3+2-1
```

And might output something like:
```bash
rolling! 2 d6
rolls: [1, 2]
total before mod: 3
bonuses: ['+3', '+2']
penalties: ['-1']
total:  7
```

## Dependencies
1. [Docopt](http://docopt.org/) – Command Line Interface

## TODO
1. Currently the server is hit for ever die roll. Cache a large set of numbers from the server ahead of time to speed things up.
- Would be nice to use a generator to access number set too.
- Add ability to configure / create macros like `{"main weapon roll": '2 d6 +1'}`
- Expand this tool to a larger application, such as a socket based chat room where people can join / chat / see others rolls.
- Probably couldn't hurt to break the code up to be a bit more testable.
- Speaking of testable, write tests.
- ~~Put this on PyPi~~
- Cleanup code, test pip install

## Credits
There was a project(s) where I borrowed code to access the ANU server API and calculate an int within a range (from an ANU result). 

Unfortunately I can't seem to remember from whom I was inspired. If you come across this and you think you contributed, please send me a message so I can give proper attribuition!

## Disclaimer
It's quite possible I've got this whole thing wrong and this doesn't simulate die rolls acurately at all. If you're especially skilled at math AND communicating to laymen like myself, please feel free to comment.

## License
Copyright 2013 aubricus [https://github.com/aubricus/pydie](https://github.com/aubricus/pydie)

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

[http://www.apache.org/licenses/LICENSE-2.0](http://www.apache.org/licenses/LICENSE-2.0)

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.