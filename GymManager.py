
from Regimen import Regimen


class GymManager:
    def __init__(self):
        self.customers = dict()
        self.regimen = dict()

    def addCustomer(self, customer):
        #self.customers[customer.getCustomerId()] = customer
        self.customers[customer.getName()] = customer
        self.regimen[customer.getName()] = dict ()

    def updatecustomer(self,customer):
        self.customers[customer.getName] = customer



    def addRegimen(self,customer,regimen):
        customerId = customer.getName()
        self.regimen[customerId] = regimen



