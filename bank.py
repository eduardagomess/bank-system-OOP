from register import Register
from accountNotFound import AccountNotFound
from insufficientFunds import InsufficientFunds


class Bank:

    def __init__(self, bank_name, bank_code):
        self.__bank_name = bank_name
        self.__bank_code = bank_code
        self.__client_register = {}

    def openAccount(self, client_name, client_id):
        register = Register()
        register.includeClientName(client_name)
        register.includeClientId(client_id)
        self.__client_register[client_id] = register
        return client_id

    def deposit(self, account_id, value):
        self.verifyAccout(account_id)
        self.__client_register[account_id].withdrawal(value)

    def withdraw(self, account_id, value):
        self.verifyAccout(account_id)
        self.__client_register[account_id].debit(self.verifyFunds(account_id, value))

    def transfer(self, payer_account_id, payee_account_id, value):
        self.verifyAccout(payer_account_id)
        self.verifyAccout(payee_account_id)
        self.__client_register[payer_account_id].debit(self.verifyFunds(payee_account_id, value))
        self.__client_register[payee_account_id].withdrawal(value)

    def accountBalance(self, account_id):
        self.verifyAccout(account_id)
        balance = self.__client_register[account_id].getBalance()
        return balance

    def closeAccount(self, account_id):
        self.verifyAccout(account_id)
        if self.accountBalance(account_id) == 0:
            del self.__client_register[account_id]
        else:
            balance = self.accountBalance(account_id)
            self.withdraw(account_id, balance)
            del self.__client_register[account_id]

    def clientId(self, account_id):
        return self.__client_register[account_id].getClientId()

    def verifyFunds(self, account_id, value):
        if self.accountBalance(account_id) > value:
            return value
        raise InsufficientFunds

    def verifyAccout(self, account_id):
        if account_id not in self.__client_register:
            raise AccountNotFound
