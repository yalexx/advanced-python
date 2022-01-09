import json


class Bill:
    """
    Object that contains data about a bill,
    such as total amount and period of the bill.
    """
    def __init__(self, amount, period):
        self.period = period
        self.amount = amount


class Flatmate:
    def __init__(self, name, days_in_house):
        self.days_in_house = days_in_house
        self.name = name

    def pays(self, bill):
        return bill.amount / 2


class PdfReport:
    def __init__(self, filename):
        self.filename = filename

    def generate(self):
        pass


the_bill = Bill(amount=120, period = "March 2021")
john = Flatmate(name="John", days_in_house=20)
marry = Flatmate(name="Marry", days_in_house=10)
print(john.pays(bill=the_bill))
