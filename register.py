class Register:

    def __init__(self):
        self.__name = ""
        self.__id = ""
        self.__balance = 0

    def includeClientName(self, name):
        self.__name = name

    def includeClientId(self, account_id):
        self.__id = account_id

    def getClientName(self):
        return self.__name

    def getClientId(self):
        return self.__id

    def getBalance(self):
        return self.__balance

    def withdrawal(self, value):
        self.__balance += value

    def debit(self, value):
        self.__balance -= value
