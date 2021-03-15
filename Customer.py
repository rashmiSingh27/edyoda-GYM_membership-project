
class Customer:
    """
    Customer entity class.
    Private Attributes:
        customerID String
        name String
        phoneNo String
        joiningDate Date

    Public methods:
        Getters and setters
    """

    def __init__(self, name='',age='',gender='',phoneNo='',email='',bmi='',duration=''):
        self.__name = name
        self.__age = age
        self.__gender = gender
        self.__phoneNo = phoneNo
        self.__email = email
        self.__bmi = bmi
        self.__duration = duration





    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setPhoneNo(self, phoneNo):
        self.__phoneNo = phoneNo

    def getPhoneNo(self):
        return self.__phoneNo


    def getCustomerId(self):
        return self.__customerId

    def setAge(self, age):
        self.__age = age

    def getAge(self):
        return self.__age
    def setGender(self, gender):
        self.__gender = gender

    def getGender(self):
        return self.__gender

    def setEmail(self, email):
        self.__email = email

    def getEmail(self):
        return self.__email

    def setbmi(self, bmi):
        self.__bmi = bmi
    def getbmi(self):
        return self.__bmi

    def getDuration(self):
        return self.__duration

    def setDuration(self, duration):
        self.__duration = duration

    def __str__(self):
        return self.getName()+" "+self.getAge()+" "+self.getGender()+" "+self.getPhoneNo()+" "+self.getEmail()+" "+str(self.getbmi())+" "+self.getDuration()+" "+str(self.getCustomerId())