from collections.abc import MutableMapping
from validators import iterable_mapping_validators


class InsensitiveDict(MutableMapping):
    """
    Insensitive dict object. All previous keys
    that already stored in dictionary can't be 
    adding again, expected only accept string
    parameters and will returned capitalize value
    whether it has been stored with lowercase or
    normal case. For example:

    Example::
        >> x = InsensitiveDict({"content-type": "application/json"})
        >> x = InsensitiveDict["CoNteNT-TyPe"]
        "application/json"
        >> x = InsensitiveDict["Content-Type"]
        "application/json
    """

    def __init__(self, data=None, *args, **kwargs):
        self._dict = {}
        if data is None:
            data = dict(*args, **kwargs)
        for key, value in data.items():
            if isinstance(data, MutableMapping):
                self._dict = {key.lower(): (key, value) for key, value in data.items()}
            elif not isinstance(data, iterable_mapping_validators(data)):
                raise Exception("The mapping of dictionary not to be key-value")
            elif not isinstance(data, MutableMapping):
                data = {key: value for key, value in data.iteritems()}
            self._dict[key] = value
        self.update(self._dict, **kwargs)

    def __setitem__(self, key, value):
        # use lowercase for store the default key
        if self._dict[key] not in key.lower():
            var = self._dict[key.lower()] == (key, value)
            return var

    def __getitem__(self, key):
        # get the value attribute by the default key is lowercase
        if not self._dict[key]:
            raise KeyError("Key is not in the list / dict")
        return self._dict[key.lower()][:]

    def __delitem__(self, key):
        # delete the value attribute by the default key is lowercase
        if not self._dict[key]:
            raise KeyError("Key is not in the list / dict")
        del self._dict[key.lower()]

    def __iter__(self, key):
        # iterate through dict object with expectation of multiple dict
        if self._dict is None:
            raise ValueError("There is no key-value in this list / dict")
        return {key: value for key, value in self._dict}.items()

    def __len__(self):
        # returned length of the dict object
        if self._dict is None:
            raise ValueError("There is no key-value in this list / dict")
        return len(self._dict)

    def __eq__(self, value):
        if isinstance(value, MutableMapping):
            value = InsensitiveDict(value)
        return dict(self.__iter__() == dict(value.__iter__()))

    def __hash__(self):
        return hash(self.__iter__())

    def __ne__(self, value):
        return not (self == value)

    def __ge__(self, value):
        return not (self < value)

    def __le__(self, value):
        return not (self > value)

    def __contains__(self, key):
        # TODO: need a lookup dict object to check whether it contains
        # key or not
        if not self._dict[key]:
            raise KeyError("Key is not in the list / dict")
        return self._dict[key]