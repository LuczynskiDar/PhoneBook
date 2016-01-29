from ksiazka_telefoniczna.Person import Person

class TelephoneBook(dict):

    '''

    Class is a collection for objects of the class Person.
    Class inherits from built-in class dict.

    '''
    def __init__(self):
        pass
    # end def

    def __cmp__(self, other):
        '''
        :param other: object of the class TelephoneBook
        :type other: TelephoneBook
        :returns: True or False

        To be implemented.

        '''
        pass

    def __setitem__(self, key, values):

        '''
        :param key: Key in collection TelephoneBook
        :type key: int
        :param values: Values to be set in the collection TelephoneBook
        :type values: list
        :type values: Person
        :type values: tuple

         Function sets _data into ojbject of the class TelephoneBook. Deepends on

        '''
    # def __setitem__(self, key, values,table = ['','','','','','','','']):
        if isinstance(values,list): # if the values are list then set it to and object pointed by the key
            p = Person(values)
            # p.set_table(table)
            super(TelephoneBook, self).__setitem__(key,p) # overrides the method of class dict

        elif isinstance(values,Person):
            super(TelephoneBook, self).__setitem__(key,values) # overrides the method of class dict

        elif isinstance(values,tuple):
            person=super(TelephoneBook, self).__getitem__(key)
            person.__setitem__(values[0],values[1])
            super(TelephoneBook, self).__setitem__(key,person) # overrides the method of class dict
