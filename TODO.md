## TODO

### Short List
- ~~Probably couldn't hurt to break the code up to be a bit more testable.~~
- ~~Speaking of testable, write tests.~~
- ~~Put this on PyPi~~
- ~~Cleanup code, test pip install~~
- Make pydie more randomer-er...
    - ANU site has a demo that takes "six values, mixes them thourghly and writes down the result"
    - Maybe pydie could do the same thing
        - Instead of a range of one result, grab n-sides in a set (20 results for a d20)
        - Get an additional result (might be more efficient to get n-sides + 1)
        - Reduce additional result to range (1-20)
        - And use that number to pick an index from the original set at random
        - Repeat n-rolls
        - Again maybe more efficient to total number of sides + n-rolls

### Long List
- Create a larger application out of this
    - Enters a 'session' so we can store
        - store a set of random numbers instead of hitting the server each time
        - store macros
        - generate metrics / log 
    - Implements a curses interface
    - Connects to a chat server, that will display rolls from mutiple people
