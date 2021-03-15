from GymManager import GymManager
from Customer import Customer
from Regimen import Regimen

gymManager = GymManager ()
customer = Customer ()

print ("\n")
print ("*****Gym Management System*****")
l = []


def user():
    print ("1.SuperUser")
    print ("2.Member")


def menu():
    print ("1. Add Customer")
    print ("2.Delete customer")
    print ("3.update customer deatils")
    print ("4. Show all customers")
    print ("5. Find customer by name")
    print ("6.add regimen of a  customer")
    print ("7.show regimen of customer")
    print ("8.del regimen of customer")
    print ("\nEnter You Choice: ")


# menu()  --------------------------------------------------
def menu2():
    print ("1. My Regime")
    print ("2. My Profile")
    print ("3.Exit)")


while (True):
    user()
    user1 = int (input ("\nEnter You Choice to login : "))
    if user1 == 1:  # superuser
        print ("menu for superuser********************")
        while 1:
            menu()
            inp = int (input ())
            if inp == 1:  # Add Customer
                name = str (input ("Enter customer's full name - "))
                age = (input ("Enter customer's age -"))
                gender = str (input ("Enter customer's gender(M/F/Others) - "))
                phoneNo = str (input ("Enter customer's phone no. - "))
                email = str (input ("Enter Customer's Email address - "))
                bmi = float (input ("Enter Customer's BMI - "))
                duration = (input ("Enter duration in months(3/6/12 months)-"))
                customer = Customer (name, age, gender, phoneNo, email, bmi, duration)
                gymManager.addCustomer (customer)

            elif inp == 2:  # delete customer
                name = input ("enter the name of the customer to be deleted:")
                customerId = -1
                for cusId in gymManager.customers.keys ():
                    customer = gymManager.customers[cusId]
                    if customer.getName () == name:
                        customerId = cusId
                        break;
                if customerId == -1:
                    print ("Customer with name - {0} not found".format (name))
                else:
                    gymManager.customers.pop (name)
                    print ("Member {} is deleted from the database".format (name))

            elif inp == 3:  # update customer's details.
                print ("******Update details*****")
                name0 = str (input ("Enter customer name - "))
                customerId = -1
                for cusId in gymManager.customers.keys ():
                    customer = gymManager.customers[cusId]
                    if customer.getName () == name0:
                        customerId = cusId
                        break
                if customerId == -1:
                    print ("Customer with name - {0} not found.Try adding it".format (name0))
                else:
                    bmi1 = float (input ("Enter bmi -"))
                    duration1 = (input ("Enter duration in months(3/6/12 months)-"))
                    for i in gymManager.customers.keys ():
                        duration = customer.setDuration (duration1)
                        bmi = customer.setbmi (bmi1)
                        print ("Duarion is changed")
                        gymManager.addCustomer (customer)

            elif inp == 4:  # Show all customers
                print ("Name\tAge\tGender\tPhone\temail\tBMI\t\tDuration")
                if len (gymManager.customers.keys ()) != 0:
                    for cusId in gymManager.customers.keys ():
                        customer = gymManager.customers[cusId]
                        # customerId = cusId
                        name = customer.getName ()
                        age = customer.getAge ()
                        gender = customer.getGender ()
                        phoneNo = customer.getPhoneNo ()
                        email = customer.getEmail ()
                        bmi = customer.getbmi ()
                        duration = customer.getDuration ()

                    print (name+"\t\t"+age+"\t"+gender+"\t\t"+phoneNo+"\t\t"+email+"\t\t"+str (bmi)+"\t\t"+duration)


            elif inp == 5:  # find customer by phn
                phn = str (input ("Enter customer phn - "))
                customerId = -1
                for cusId in gymManager.customers.keys ():
                    customer = gymManager.customers[cusId]
                    if customer.getPhoneNo () == phn:
                        print (customer)
                        customerId = cusId
                        break;
                if customerId == -1:
                    print ("Customer with name - {0} not found".format (phn))
                else:
                    # packageDict = gymManager.subscriptions.get(customerId)
                    print ("Customer found", gymManager.customers[name])

            elif inp == 6:  # Add Regimen
                name = input ("Enter the Member name :")
                reg = Regimen (name)
                # regimen = Regimen (bmi)
                customerId = -1
                for cusId in gymManager.customers.keys ():
                    customer = gymManager.customers[cusId]
                    if customer.getName () == name:
                        print ("True")
                        print ("customer")
                        customerId = cusId
                        bmi1 = customer.getbmi ()
                        regimen = reg.workouts (bmi1)  # returns a dict of workout acc to bmi
                        regimen = reg.workouts (bmi)
                        print ("workout plan", regimen)
                        break
                    else:
                        print ("member do not exits")
                        break
                # regimen = reg.workouts(bmi)
                # print("workout plan",regimen)
                if customerId == -1:
                    print ("Customer with name - {0} not found.".format (name))
                    print ("Try adding a new customer.")
                else:
                    if gymManager.regimen.keys ():
                        for regId in gymManager.regimen.keys ():
                            gymManager.addRegimen (gymManager.customers[name], regimen)
                            gymManager.regimen[name] = regimen
                            print ("workout plan is added for {} Member.".format (name))
                            print ("--------------------------------------------------------------------------")

            elif inp == 7:  # Show  workoutplan of a input member
                name = str (input ("Enter customer name - "))
                customerId = -1
                for cusId in gymManager.customers.keys ():
                    customer = gymManager.customers[cusId]
                    if customer.getName () == name:
                        if name in gymManager.regimen:
                            # print (customer)
                            customerId = cusId
                            break
                if customerId == -1:
                    print ("Customer with name - {0} has no workout plan yet".format (name))
                else:
                    regDict = gymManager.regimen.get (name)
                    if regDict != {}:
                        print ("workout plan of this member is -")
                        print (gymManager.regimen[name])
                    else:
                        print ("No plan found for this customer")

            elif inp == 8:  # delete customer's workout plan
                name = str (input ("Enter customer name - "))
                customerId = -1
                for cusId in gymManager.customers.keys ():
                    customer = gymManager.customers[cusId]
                    if customer.getName () == name:
                        if name in gymManager.regimen.keys ():
                            # print (customer)
                            customerId = cusId
                            break
                if customerId == -1:
                    print ("Customer with name - {0}  has no workout plan yet ".format (name))
                else:
                    if gymManager.regimen.get (name) != {}:
                        regDict = gymManager.regimen.get (name)
                        print ("Customer's regimen plan found", gymManager.customers[name])
                        if regDict != {}:
                            gymManager.regimen.pop (name)
                            print ("workout plan of this member is deleted ")
                    # print(gymManager.regimen[name])
                    else:
                        print ("No plan found for this customer")


            elif inp == 9:  # exit
                # gymManager.save()
                exit (0)
            elif inp == "exit":
                # 1gymManager.save()
                exit (0)

            else:
                print ("Please enter a valid number")
            menu ()
    if user1 == 2:
        menu2 ()
        inp2 = int (input ("Enter You Choice:"))  # choice from member menu
        if inp2 == 1:
            name = str (input ("Enter customer name - "))
            customerId = -1
            for cusId in gymManager.customers.keys ():
                customer = gymManager.customers[cusId]
                if customer.getName () == name:
                    if name in gymManager.regimen:
                        # print (customer)
                        customerId = cusId
                        break
            if customerId == -1:
                print ("No workout plan is assigned to you yet.Ask superuser to assign you workout")
            else:
                regDict = gymManager.regimen.get (name)
                if regDict != {}:
                    print ("Your workout plan is -")
                    print (gymManager.regimen[name])
                else:
                    print ("No plan found for you")
        elif inp2 == 2:
            name = str (input ("Enter your name - "))
            customerId = -1
            for cusId in gymManager.customers.keys ():
                customer = gymManager.customers[cusId]
                if customer.getPhoneNo () == name:
                    print (customer)
                    customerId = cusId
                    break;
            if customerId == -1:
                print ("Your profile is not created yet.Ask the superuser to add you")
            else:
                # packageDict = gymManager.subscriptions.get(customerId)
                print ("My profile:-", gymManager.customers[name])

        else:
            print ("Please enter a valid number")
