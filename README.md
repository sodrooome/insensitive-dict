## Insensitive Dict

Simple case for insensitive dictionary object, All previous keys that already stored in dictionary can't be adding again (avoid duplication) and all keys will preserved as lowercase regardless previously was set in uppercase or capitalize object.

### Example

```python
# simple usage
>> from utils import InsensitiveDict

>> headers = InsensitiveDict({"Content-Type": "application/json"})
>> headers["content-type"]
application/json # expected output
```