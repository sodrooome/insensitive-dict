class Lookup(dict):
    """
    A class method used for looking up a pair
    of key in dictionary object
    """
    
    def __init__(self, key, iterable=None):
        self.key = key
        super(Lookup, self).__init__(iterable)

    def __getitem__(self, key):
        # default value if there's any item is None
        return super(Lookup, self).__getitem__(key, None)