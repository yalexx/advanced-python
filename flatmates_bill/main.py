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

    def pays(self, bill, flatmate2):
        weight = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
        to_pay = bill.amount * weight
        return to_pay


class PdfReport:
    def __init__(self, filename):
        self.filename = filename

    def generate(self):
        pass


the_bill = Bill(120, "March 2021")
john = Flatmate("John", 20)
marry = Flatmate("Marry", 25)
print('John pays: ', john.pays(the_bill, marry))
print('Marry pays: ', marry.pays(the_bill, john))
