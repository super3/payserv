import unittest
from payserv.Payee import Payee

class TestPayee(unittest.TestCase):

    def test_valid_address(self):
        addr = '1CmFuDcdvhShHB9QgcrXckJF4UEmMFbu7V'
        user = Payee(addr)

        self.assertTrue(user.is_valid_address(addr))