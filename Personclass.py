class Person:
    def __init__(self, name, add, tele):
        self.__name = name
        self.__address = add
        self.__tele = tele

    def print_person(self):
        return self.__name, self.__address, self.__tele

class Customer(Person):
    def __init__(self, name, add, tele, cusnum, ml):
        Person.__int__(self, name, add, tele)
        self.__cnumber = cusnum
        self.__mail_list = ml
    
    def print_person(self):
        Person.print_person(self)
        print('Customer number:', self.__cnumber)
        if self.__mail_list:
            print('On mailing list: Yes')
        else:
            print('On mailing list: No')