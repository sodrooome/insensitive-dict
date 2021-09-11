import unittest
from utils import InsensitiveDict


class TestInsensitiveDictMethod(unittest.TestCase):
    def test_value(self):
        x = InsensitiveDict({"content-type": "application/json"})
        self.assertEqual(x["content-type"], "application/json")

    def test_value_capitalize(self):
        x = InsensitiveDict({"content-type": "application/json"})
        self.assertFalse(x["content-type"].isupper())
        self.assertTrue(x["content-type"].islower())

    def test_length(self):
        x = InsensitiveDict({"content-type": "application/json"})
        self.assertEqual(len(x), 1)
        self.assertEqual(x.__len__(), 1)

    def test_get_value(self):
        x = InsensitiveDict({"content-type": "application/json"})
        self.assertTrue(x.__getitem__("content-type"), "application/json")

    def test_delete_value(self):
        x = InsensitiveDict({"content-type": "application/json"})
        self.assertEqual(x.__delitem__("content-type"), None)

    def test_set_value(self):
        x = InsensitiveDict({"content-type": ""})
        self.assertEqual(x.__setitem__("content-type", "value"), None)


if __name__ == "__main__":
    unittest.main()
