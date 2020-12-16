from bank import Bank

bank = Bank("Nubank", 421)
pedro_account = bank.openAccount("Pedro", 987234)
ana_account = bank.openAccount("Ana", 135793)

bank.deposit(ana_account, 500.00)
bank.deposit(pedro_account, 80.00)
bank.transfer(ana_account, pedro_account, 40.00)
bank.withdraw(ana_account, 1000)

