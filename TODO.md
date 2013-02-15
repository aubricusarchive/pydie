## TODO

### Short List
- ~~Probably couldn't hurt to break the code up to be a bit more testable.~~
- ~~Speaking of testable, write tests.~~
- ~~Put this on PyPi~~
- ~~Cleanup code, test pip install~~
- Make pydie more randomer-er...
    - ANU site has a demo that takes "six values, mixes them thourghly, picks one, and writes down the result"
    - Maybe pydie could do the same thing
        - create range 1 - 20
        - shuffle range
- Update Cli to accept combinations of die e.g.,
    - 1 d10 +1 1d6 +1

### Long List
- Create a larger application out of this
    - Enters a 'session' so we can store
        - store a set of random numbers instead of hitting the server each time
        - store macros
        - generate metrics / log 
    - Implements a curses interface
    - Connects to a chat server, that will display rolls from mutiple people
