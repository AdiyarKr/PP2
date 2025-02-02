class Account:
  def __init__(self, owner, balance):
    self.owner = owner
    self.balance = balance

  def deposit(self, money):
    self.balance += money

  def withdraw(self, money):
    self.balance -= money
    if(self.balance < 0):
      print("You haven`t enough money")
    else:
      print(self.balance)

my_account = Account("Adiyar", 20000)
my_account.deposit(5000)
my_account.withdraw(15000)