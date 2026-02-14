from abc import ABC, abstractmethod

class bank(ABC):
    def account_name(self):
        pass

    def balance(self):
        pass

    def deposit(self, amount):
        pass

    def withdraw(self, amountt):
        pass

class myacount(bank):
      def __init__(self, account_name, balance):
          self.account_name=account_name
          self.balance=balance

      def deposit(self, amount):
          self.balance+=amount
          print(f"Depositing ${amount}")
          print("Your current balance is: $",self.balance)

      def withdraw(self, amountt):
          if amountt>self.balance:
              print("Sorry, you don't have enough balance.")

          else:
              print(f"Withdrawing ${amountt}")
              self.balance-=amountt
              print(f"You have withdrew ${amountt}. Now you have ${self.balance} left in your account")

account_name=input("Enter you Account name")
balance=int(input("Enter your Balance"))
a1=myacount(account_name,balance)

print("yes/no")
d1=input("Do you want to withdraw?").lower()
if d1=="yes":
    amountt=int(input("How much do you want to Withdraw?"))
    a1.withdraw(amountt)

else:
    print("No withdrawal made")

print("yes/no")
d2=input("Do you want to make a deposit?").lower()

if d2=="yes":
    amount=int(input("How much do you want to deposit?"))
    a1.deposit(amount)

else:
    print("No deposit made")