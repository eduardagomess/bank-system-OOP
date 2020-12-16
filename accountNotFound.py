class AccountNotFound(Exception):
    def __init__(self):
        super().__init__("Account not found")
