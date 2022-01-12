from _typeshed import Self


class Category:

  '''The class takes in different categories present within a budget and manipulates the budget to account for different transactions'''

  def __init__(self, title):
    self.title = title
    self.ledger = []

  def deposit(self, amount, description=""):
    self.ledger.append({"amount": amount, "description": description})

  def withdraw(self, amount, description=""):
    if funds >= amount:
      self.ledger.append({"amount": -amount, "description": description})
      return True
    else:
      return False

  def get_balance():
    '''current balance of the budget category based on teh transactions that have occurred'''

  def transfer(self, amount, )

  def check_funds(self, amount):
    if amount > get_balance

  def create_spend_chart(categories):