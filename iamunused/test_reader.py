# test_reader.py
import unittest
from reader import Reader
import warnings

class TestReader(unittest.TestCase):

    def setUp(self):
        self.reader = Reader("role", None)
        warnings.filterwarnings("ignore", category=ResourceWarning, message="unclosed.*<ssl.SSLSocket.*>") 

    def test_get_roles(self):
        roles = self.reader.get_roles()
        self.assertIsNotNone(roles)

    def test_get_unused_role_permissions(self):
        roles = self.reader.get_roles()
        unused = self.reader.get_unused_role_permissions(roles[0])
        self.assertIsNotNone(roles)
        self.assertIsNotNone(unused)

if __name__ == '__main__':
    unittest.main()