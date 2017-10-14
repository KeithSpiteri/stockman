class Entry:
    'Model for an entry in the inventory'

    def __init__(self, entry):
        split = entry.split(',')
        self.name = split[0].strip()
        self.quantity = split[1].strip()

    @staticmethod
    def isValid(entry):
        """ Given a list type entry, will validate that it conforms to the Entry model"""

        split = entry.split()
        try:
            return len(split) == 2 and isinstance(int(split[1]), int)
        except ValueError:
            return False

    def __repr__(self):
        return '{Name: ' + self.name + ', Quantity: ' + self.quantity + '}'
