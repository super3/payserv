import json
import unittest
from payserv.Payee import Payee


class TestPayee(unittest.TestCase):

    def test_valid_address(self):
        addr = '1CmFuDcdvhShHB9QgcrXckJF4UEmMFbu7V'
        in_addr1 = "4CmFuDcdvhShHB9QgcrXckJF4UEmMFbu7V"
        in_addr2 = "notavalidaddress"

        self.assertTrue(Payee(addr).is_valid_address())
        self.assertFalse(Payee(in_addr1).is_valid_address())
        self.assertFalse(Payee(in_addr2).is_valid_address())

    def test_addr_data(self):
        addr1 = '14K1kmduk5q3aS8SmkFdHU8mufzr4whwWz'
        addr2 = '1CmFuDcdvhShHB9QgcrXckJF4UEmMFbu7V'
        addr3 = "notavalidaddress"

        payee1 = Payee(addr1)
        payee2 = Payee(addr2)
        payee3 = Payee(addr3)

        json_response = payee1.get_addr_data()
        self.assertEqual(json_response["data"][0]["asset"], 'SJCX')
        self.assertEqual(json_response["data"][0]["amount"], '1000.00000000')

        invalid = {"success":0,"error":"Invalid address"}
        self.assertEqual(payee2.get_addr_data(), invalid)
        self.assertEqual(payee3.get_addr_data(), invalid)

    def test_addr_bal(self):
        addr1 = '14K1kmduk5q3aS8SmkFdHU8mufzr4whwWz'
        addr2 = '1CmFuDcdvhShHB9QgcrXckJF4UEmMFbu7V'

        payee1 = Payee(addr1)
        payee2 = Payee(addr2)

        self.assertEqual(payee1.get_balance(), 1000)
        self.assertEqual(payee2.get_balance(), 0)