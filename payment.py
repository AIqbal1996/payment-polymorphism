from abc import ABC, abstractmethod


# Abstraction
class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


# Credit Card Payment
class CreditCardPayment(Payment):

    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card")


# UPI Payment
class UPIPayment(Payment):

    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")


# Net Banking Payment
class NetBankingPayment(Payment):

    def pay(self, amount):
        print(f"Paid ₹{amount} using Net Banking")


# Runtime Polymorphism
payments = [
    CreditCardPayment(),
    UPIPayment(),
    NetBankingPayment()
]

for payment in payments:
    payment.pay(1000)