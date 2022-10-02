class Category:
 #Class Object Attribute
  #balance = 0
  #ledger = []
  def __init__(self, category):
    self.category = category
    self.ledger = list()
    self.balance = int()

  
  def deposit(self, amount=" ", description=" "):
    self.amount = amount
    self.description = description
    self.balance += self.amount
    self.ledger.append({'amount' : self.amount, 'description' : self.description})
    #return self.ledger
   
    
  def withdraw(self, amount=" ", description=" "):
    self.amount = amount
    self.description = description
    if(self.balance >= self.amount):
      self.ledger.append({'amount' : -self.amount, 'description' : self.description})
      return True
    else:
      return False

    
  def get_balance(self):
    blc = 0
    for i, num in enumerate(self.ledger):
      #print(i, num)
      blc += num['amount']
    #print(self.balance)  
    self.balance = self.balance - (self.balance - blc)
    return blc
    

  def transfer(self, amount, category):
    self.amount = amount
    #self.category = category
    if (self.balance >= self.amount):
      self.ledger.append({'amount': -self.amount, 'description':f'Transfer to {category.category}'})
      category.deposit(self.amount, f'Transfer from {self.category}')
      self.balance = self.balance - amount
      #print(self.balance)
      
      return True
    else:
      return False

  def check_funds(self, amount):
    self.amount = amount
    if(amount > self.balance):
      return False
    else:
      return True
    

  

def create_spend_chart(categories):
  pass

food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)
