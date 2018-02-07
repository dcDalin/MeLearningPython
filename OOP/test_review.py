import unittest
from review import BankAccount

class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.initBankAccount = BankAccount()

    def test_show_balance(self):
        result = self.initBankAccount.show_balance()
        self.assertEqual(result, 3000)