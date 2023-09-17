class BankAccount:
  def __init__(self,accountNumber,accountHolderName,initialBalance=0):
    self.__accountNumber=accountNumber
    self.__accountHolder=accountHolderName
    self.__AccountBalance=initialBalance
    
  def deposit(self,amount):
    if amount>0:
      self.__AccountBalance +=amount
      print("deposited Rs {}.New balance:Rs{}".format
          (amount,self.__AccountBalance))
    
    else:
       print("invalid deposit amt")

  def withdraw(self,amount):
   if amount>0 and amount<=self.__AccountBalance:
     self.__AccountBalance -=amount
     print("withdrew Rs {}.New balance:Rs{}".format
          (amount,self.__AccountBalance))
    
   else:
    print("invalid beenwithdrawn amount")

  def display_balance(self):
    print("account balance for {} (account#{}):Rs{}".format(
        self.__accountHolder,self.__accountNumber,
             self.__AccountBalance))

account = BankAccount(accountNumber="123445",
                      accountHolderName="kirthika",
                    initialBalance=5000)

account.display_balance()
account.deposit(5000)
account.withdraw(2000)
