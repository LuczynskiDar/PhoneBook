from ksiazka_telefoniczna.Person import Person

class TelephoneBook(dict):
    def __init__(self):
        pass
    # end def

    def __cmp__(self, other):
        pass

    def __setitem__(self, key, values):
        if isinstance(values,list):
            p = Person(values)
            super(TelephoneBook, self).__setitem__(key,p)
        elif isinstance(values,Person):
            super(TelephoneBook, self).__setitem__(key,values)
        elif isinstance(values,tuple):
            ''' In tuple is pointer[0] and value[1]'''
            person=super(TelephoneBook, self).__getitem__(key)
            person.__setitem__(values[0],values[1])
            super(TelephoneBook, self).__setitem__(key,person)
        else:
            print("Problem to be solved")
