def round_to_ten(n):
  multiple = 10
  rounded = int(n * multiple) / multiple
  return rounded

def get_percentages(categories):
  '''Obtain a list of percentages rounded a multiple of 10'''
  total_spend = 0
  category_spend = []
  for category in categories:
    total_spend += category.get_withdrawals()
    category_spend.append(category.get_withdrawals())
  rounded_values = list(map(lambda x: round_to_ten(x/total_spend), category_spend))
  return rounded_values

def create_spend_chart(categories):
  '''Takes in a list and creates a chart formatted in a specific manner to display percentage spending as a bar chart in string format'''
  output = "Percentage spent by category\n"
  i = 100
  percentages = get_percentages(categories)
  while i >= 0:
    spaces = " "
    for percentage in percentages:
      if percentage * 100 >= i:
        spaces += "o  "
      else:
        spaces += "   "
    output += str(i).rjust(3) + "|" + spaces + ("\n")
    i -= 10
  
  add_dash = "-" +"---"*len(categories)
  names = []
  name_titles = ""
  for category in categories:
    names.append(category.title)
  
  longest_name = max(names, key=len)

  for x in range(len(longest_name)):
    name_string = '     '
    for name in names:
      if x >= len(name):
        name_string += "   "
      else:
        name_string += name[x] + "  "
    
    if (x != len(longest_name) -1):
      name_string += '\n'
    
    name_titles += name_string

  output += add_dash.rjust(len(add_dash)+4) + "\n" + name_titles
  return output


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
      ledger_item += f"{item['description'][0:23]:<23}" + f"{item['amount']:>7.2f}\n"
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
    '''Finds the current balance'''
    balance = 0
    for item in self.ledger:
      balance += item["amount"]
    return balance

  def transfer(self, amount, category):
    '''Transfer = withdraw from one category, and add to another'''
    if self.check_funds(amount):
      self.withdraw(amount, "Transfer to " + category.title)
      category.deposit(amount, "Transfer from " + self.title)
      return True
    return False

  def check_funds(self, amount):
    '''Tests if there are sufficient funds within the account for the next transaction'''
    if amount > self.get_balance(amount):
      return False
    return True

  def get_withdrawals(self):
    '''Add up the total amount spent in this category'''
    total = 0
    for item in self.ledger:
      if item["amount"] < 0:
        total += item["amount"]
    return total