class PyDieError(Exception):
    pass


class AnuApiFailed(PyDieError):
    def __init__(self, length):
        self.length = length

    def __str__(self):
        return "The attempt to access the ANU Server API has failed. The max length allowed is {0} but the max length spcified was {1}".format(self.length)
