

class Category:

  '''The class takes in different categories present within a budget and manipulates the budget to account for different transactions'''

  def __init__(self, title):
    self.title = title
    self.ledger = list()

  def __str__(self,):
    '''format specifiers used for text formatting'''
    title = f"{self.title:*^30}\n"
    ledger_item = ""
    total = 0
    for item in self.ledger:
      ledger_item += f"{item['description'][0:23]:<23}" + f"{item['amount'][23:]:>7.2f}\n"
      total += item['amount']
    return title + ledger_item + "Total: " + str(total)

  def deposit(self, amount, description=""):
    self.ledger.append({"amount": amount, "description": description})

  def withdraw(self, amount, description=""):
    if self.check_funds(amount):
      self.ledger.append({"amount": -amount, "description": description})
      return True
    else:
      return False

  def get_balance(self):
    '''A get_balance method that returns the current balance of the budget category based on the deposits and withdrawals that have occurred.'''
    balance = 0
    for item in self.ledger:
      balance += item["amount"]
    return balance

  def transfer(self, amount, category):
    '''A transfer method that accepts an amount and another budget category as arguments. The method should add a withdrawal with the amount and the description "Transfer to [Destination Budget Category]". The method should then add a deposit to the other budget category with the amount and the description "Transfer from [Source Budget Category]". If there are not enough funds, nothing should be added to either ledgers. This method should return True if the transfer took place, and False otherwise.'''
    if self.check_funds(amount):
      self.withdraw(amount, "Transfer to " + category.title)
      category.deposit(amount, "Transferred from" + self.title)
      return True
    return False

  def check_funds(self, amount):
    '''A check_funds method that accepts an amount as an argument. It returns False if the amount is greater than the balance of the budget category and returns True otherwise. This method should be used by both the withdraw method and transfer method.'''
    if amount > self.get_balance(amount):
      return False
    return True

  def create_spend_chart(categories):
    pass