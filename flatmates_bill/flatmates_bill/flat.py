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
