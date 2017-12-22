class Customer(object):
	"""A customer of ABC Bank with a checking account. 
	Customers have the
    following properties:
	
	Attributes:
       
	name: A string representing the customer's name.
        
	balance: A float tracking the current balance of the customer's account.
    """

	def __init__(self, name):
		"""Return a Customer object whose name is *name*.""" 
		self.name = name
	
	def set_balance(self, balance=0.0):
		"""Set the customer's starting balance."""
		self.balance = balance

	def withdraw(self, amount):
		"""Return the balance remaining after withdrawing *amount*
        dollars."""
		if amount > self.balance:
			raise RuntimeError('Amount greater than available balance.')
		self.balance -= amount
		return self.balance

	def deposit(self, amount):
		"""Return the balance remaining after depositing *amount*
        dollars."""
		self.balance += amount
		return self.balance


#  * * * * * * * * * *  CODE ADDED BELOW * * * * * * * * * *

	# Getter method to Display Name 
	def displayCustomerName(self):
		print "Customer Name: ", self.name
	# Getter method to Display Current Balance 
	def displayCustomerBalance(self):
		print "Customer Current Balance: ", self.balance

# Initialze first customer
customerA = Customer("Danny")
# Display Name to screen
customerA.displayCustomerName()

# set balance of customer
customerA.set_balance(1250)

# Display customer balance to screen

customerA.displayCustomerBalance()

# set a deposit for customer

amountDeposit = customerA.deposit(500)

# Display deposit amount to screen

print "Amount after deposit: ", amountDeposit

# withdraw an amount from customer

amountWithdraw = customerA.withdraw(300)

# Display withdrawal amount to screen

print "Amount after withdrawal ", amountWithdraw

#Total Amount in Bank

print "\nFinal Transaction\n"

customerA.displayCustomerName()

customerA.displayCustomerBalance()

	