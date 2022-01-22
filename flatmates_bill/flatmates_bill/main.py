from flatmates_bill.flatmates_bill.flat import Bill, Flatmate

the_bill = Bill(120, "March 2021")
john = Flatmate("John", 30)
marry = Flatmate("Marry", 25)
print('John pays: ', john.pays(the_bill, marry))
print('Marry pays: ', marry.pays(the_bill, john))
