from pprint import pprint


class BotParser:

    givenPath = None
    _bots = None

    def __init__(self, path):
        self.givenPath = path

    def getToArray(self):
        parsed = {}
        try:
            with open(self.givenPath, 'r') as f:
                self._bots = f.readlines()

        except IOError:
            print('File cannot been found!')

        data = {}
        for line in self._bots:
            temp = line.rstrip()
            #parsed = BotParser.parse(temp)
            tempp = list(temp.split('#'))

            data[tempp[0]] = tempp[1]
        return data




