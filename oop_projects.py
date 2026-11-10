from bank_accounts import *


James = BankAccount(12000, "James")
Lavender = BankAccount(23000, "Lavender")

James.getBalance()
Lavender.getBalance()

James.deposit(10000)

Lavender.withdraw(300000)

Lavender.withdraw(1000)

James.transfer(344444, Lavender)
James.transfer(3002, Lavender)

Jim = InterestRewardsAcct(100000, "Jim")

Jim.getBalance()

Jim.deposit(1000)

Jim.transfer(20000, James)

Blaze =  SavingsAcct(10000, "Blaze")

Blaze.getBalance()
Blaze.deposit(10000)
Blaze.transfer(40000, Lavender)