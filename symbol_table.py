
class SymbolTable:
    """ This class is used for the symbol table. """
    def __init__(self):
        """ Creates a new empty symbol table. """
        self.table = {
            "sp":     0x0000,
            "lcl":    0x0001,
            "arg":    0x0002,
            "this":   0x0003,
            "that":   0x0004,
            "screen": 0x4000
        }

        for i in range(16):
            self.table["r{}".format(i)] = i

    def __getitem__(self, symbol):
        """ Returns the ddress associated with the symbol. """
        return self.table[symbol]

    def __setitem__(self, symbol, address):
        """ Adds the pair (symbol, address) to the table. """
        self.table[symbol] = address

    def __contains__(self, symbol):
        """ Does the symbol table contain the given symbol """
        return symbol in self.table
