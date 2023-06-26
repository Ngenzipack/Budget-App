class Category:
  def __init__(self, product):
    self.product = product
    self.ledger = list()  # to keep the items in ledger
  def deposit(self, amount, description = ""):
    self.ledger.append({"amount": float(amount), "description": description})
  def withdraw(self, amount, description = ""):
    if self.check_funds(amount) == True:
      self.ledger.append({"amount": -float(amount), "description": description})
      return True
    else: return False
  def get_balance(self):
    balance = 0.0
    for item in self.ledger:
      balance += item['amount']
    return balance
  def transfer(self, amount, sub_category):
    if self.check_funds(amount) == True:
      self.withdraw( float(amount), f"Transfer to {sub_category.product}")
      sub_category.deposit( float(amount), "Transfer from " + '{}'.format(self.product))
      return True
    else: return False
  def check_funds(self, amount):
    balance = 0
    for item in self.ledger:
      balance += item['amount']
    if balance < float(amount): return False
    else: return True
  def __str__(self):
    display = ""
    total = 0
    display += self.product.center(30, '*') + "\n"
    for item in self.ledger:
      display += item["description"][:23].ljust(23) + '{:.2f}'.format(item["amount"]).rjust(7)

      display += "\n"
      total += item['amount']
    display += "Total: " + str(total) 
    return display
def create_spend_chart(categories):
  percentage_spent = []
  category_names = []
  category_amount = []
  display = ""
  for names in categories:
    amount_spent = 0.0
    for item in names.ledger:
      if item['amount']<0:
        amount_spent += float(item['amount'])
    category_amount.append(amount_spent)
    category_names.append(names.product)
  for percentages in category_amount:
    percentage_spent.append(round(percentages/sum(category_amount),2)*100)
  display += 'Percentage spent by category\n'
  for i in range(100, -10, -10):
    display += str(i).rjust(3) + "| "
    k =0
    while k < len(percentage_spent):
      if i <= percentage_spent[k]:
        display += "o  "
      else:
        display += "   "
      k = k + 1
    display += "\n"
  display += '    ----' + '---'*(len(category_names)-1)
  display += "\n     "
  high = 0
  for names in category_names:
    if high < len(names):
      high = len(names)
  for i in range(high):
    for names in category_names:
      if i < len(names):
        display += str(names[i]) + "  "
      else:
        display += "   "
    if i < high - 1:
      display += "\n     "
  return display
