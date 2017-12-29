import unittest
from sample_account import Customer

class TestSampleAccount(unittest.TestCase):

        def test_set_balance(self):
                customerTest = Customer("Testing Customer")
                customerTest.set_balance(6050)
                
                
                
        def test_withdraw(self):
                customerTest = Customer("Testing Customer")
                customerTest.set_balance(2000)
                self.assertEqual(customerTest.withdraw(1000), 1000)
                self.assertEqual(customerTest.withdraw(100), 900)
                self.assertEqual(customerTest.withdraw(25), 875)
                self.assertEqual(customerTest.withdraw(175), 700)
                
                

        def test_deposit(self):
                customerTest = Customer("Testing Customer")
                customerTest.set_balance(4000)
                self.assertEqual(customerTest.deposit(200), 4200)
                self.assertEqual(customerTest.deposit(10), 4210)
                self.assertEqual(customerTest.deposit(400), 4610)
