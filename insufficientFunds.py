class InsufficientFunds(Exception):
    def __init__(self):
        super().__init__("Insufficient funds")
