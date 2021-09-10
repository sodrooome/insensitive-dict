def iterable_mapping_validators(data):
    # method for check whether the dictionary object
    # contains pair of key-value and only expected
    # to be string object for accepted value
    for index, element in enumerate(data):
        if len(element) != 2:
            raise ValueError("Dictionary must be pair of key-value")
        if not isinstance(element, str):
            raise TypeError("Value must be string object")
        return element