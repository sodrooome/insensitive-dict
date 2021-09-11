## Insensitive Dict

[![Build Status](https://app.travis-ci.com/sodrooome/insensitive-dict.svg?token=rHmyG6UiRrnXStqxuNMc&branch=main)](https://app.travis-ci.com/sodrooome/insensitive-dict)

Simple case for insensitive dictionary object, All previous keys that already stored in dictionary can't be adding again (avoid duplication) and all keys will preserved as lowercase regardless previously was set in uppercase or capitalize object.

### Example

```python
# simple usage
>> from utils import InsensitiveDict

>> headers = InsensitiveDict({"Content-Type": "application/json"})
>> headers["content-type"]
application/json # expected output
```

### Testing

Just run with execute following command `python test_utils.py`

### Acknowledgments

This repository was created just to learn how to create an ordered dictionary object without using `dict` module that already provided by Python. You might be found some interesting in here :

- [Ordered Dict in Python](https://realpython.com/python-ordereddict/)
- [Code Review for Insensitive Dictionary](https://codereview.stackexchange.com/questions/264411/python-case-insensitive-dictionary)
- [Stack Overflow answer](https://stackoverflow.com/questions/45114985/how-to-create-an-ordereddict-in-python)
