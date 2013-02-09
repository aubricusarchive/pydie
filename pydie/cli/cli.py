from docopt import docopt


class cli(object):
    """Usage: pydie.py roll <multiplier> <die> [<modifier>]
              pydie.py [-h | --help]

    Generate a random n-sided dice role.

    Options:
        -h --help  print help information for this program

    """
    def __init__(self):
        super(cli, self).__init__()

        self.arguments = {}

    def main(self):
        self.arguments = docopt(__doc__)

        if(self.arguments['roll']):
            multi = self.arguments['<multiplier>']
            die = self.arguments['<die>']
            mod = '0' if not self.arguments['<modifier>'] else self.arguments['<modifier>']
