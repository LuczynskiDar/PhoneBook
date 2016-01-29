# -*- coding: utf-8 -*-

class Person:
    '''
        Definition of Class Person, which is a container for:
        first name, surname, telephone number, street, house and flat number,
        city, postal code and email.
    '''

    # __TABLE = ['','','','','','','','']
    __TABLE = ["Imię","Nazwisko","Telefon","Ulica","Numer","Miasto ","Kod pocztowy","Email"]

    def __init__(self, list_of_data):
        '''
        :param list_of_data:
        :type list

        Function initiates and object of a class Person with a list of parameters.
        Parameters are type string. However, the third parameter, telephone, might be a type of
        integer. Then it's being casted to string.
        '''
        self.list_of_data = list_of_data
        if type(self.list_of_data[2]) == int:
            self.list_of_data[2] = str(self.list_of_data[2])
    #end def

    def set_table(self,*args):
        '''
        :param args: List of parameters of the contact.
        :type args: list

        Function sets a list of parameters to tje class attribute Table.
        '''
        self.__TABLE = args

    def __setitem__(self,pointer,value):
        '''
        :param pointer: from 0 to 7
        :type pointer: int
        :parameter value: as describedin diekinition of class Person
        :type value: str

        Built in fuction, which sets in an value into list_of_data,
        poited out by the pointer.
        '''
        self.list_of_data[pointer] = value

    def __getitem__(self, item):
        '''
        :param item: points on an item or on a whole list
        :type item: list
        :return: list_of_data
        :type item: int
        :returns: list_of_data[item]

        The function is a getter. Gets a value from an object of class Person.
        '''
        if isinstance(item,list):
            return self.list_of_data
        elif isinstance(item,int):
            return self.list_of_data[item]

    def __eq__(self, other):
        '''
        :param other: Another object of the class Person
        :type other: Person
        :returns: True or False

        Compares two objects of class Person.
        This builtin function, which overloads the parameter "="
        '''
        return self.list_of_data == other

    def __iter__(self):
        '''
        :returns: self

        Definition of an iterator, which iterates through items of the list
        starting from first item in the list, thus handle value is 0.
        '''
        self.handle =- 1
        return self

    def __next__(self):
        '''
        :returns: list_of_data[handle]

        Definition of an iterator. Increase handle by 1 or raises an exception
        of stopping an itreration.
        '''
        if self.handle > len(self.list_of_data) - 2:
            raise StopIteration
        else:
            self.handle += 1
        return self.list_of_data[self.handle]
    #end def


    def __str__(self):
        '''
        :returns: All srings from list_of_data

        Builtin function, overloads the object of class Person.
        '''

        return "".join([self.__TABLE[k] + ": " + self.list_of_data[k] + "\n" for k in range(len(self.list_of_data))])

        #end def

    def to_table_values(self):
        '''
        :returns: SQL _TABLE's input string

        Fuction returns _data from an object of class Person for rquirements inserting _data to a SQL _TABLE
        '''
        return "".join([ "'" + self.list_of_data[i] + "'" + "," if i != 2 else  self.list_of_data[i]+"," \
                         for i in range(len(self.list_of_data)-1)])+"'"+self.list_of_data[len(self.list_of_data)-1]+"'"
