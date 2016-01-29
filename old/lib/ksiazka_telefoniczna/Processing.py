# -*- coding: utf-8 -*-

from ksiazka_telefoniczna.GetData import GetData
from ksiazka_telefoniczna.TelephoneBook import TelephoneBook
import os,sys,pkgutil,pkg_resources
# print(os.path.realpath(__file__))
# print(os.path.dirname(os.path.realpath(__file__)))
# KT_PATH=os.path.dirname(os.path.realpath(__file__))
# KT_PATH=KT_PATH+os.path.sep+'db'
# print(os.listdir(KT_PATH))
# print(KT_PATH)
# print(os.listdir(os.path.dirname(os.path.realpath(__file__))+os.path.sep+"db"))
# print(os.listdir(os.path.dirname(os.path.realpath(__file__))+os.path.sep+"db")))
# print(os.path.pathsep)
# print(os.path.sep)
# print(os.listdir(os.path.dirname(os.path.realpath(__file__+"/db"))))
# print(os.listdir(os.path.realpath(__file__+"/db")))
# print('proc')
# print(os.listdir(os.path.realpath(__file__+"/db")))
# print(pkgutil.get_loader('ksiazka_telefoniczna'))
# print([p for p in pkg_resources._namespace_packages])
# print(os.get_exec_path())
# sys.path.append(os.path.dirname(os.path.realpath(__file__)))

# global PATH
# PATH=os.getcwd()

class Processing:

    #Applying paths to the _data
    _KT_PATH = os.path.dirname(os.path.realpath(__file__))
    _CFG_PATH = _KT_PATH + os.path.sep + 'cfg' + os.path.sep
    _DB_PATH = _KT_PATH + os.path.sep + 'db' + os.path.sep
    _CSV_PATH = _KT_PATH + os.path.sep + 'csv' + os.path.sep

    #Appends the paths
    sys.path.append(_KT_PATH)
    sys.path.append(_CFG_PATH)
    sys.path.append(_DB_PATH)
    sys.path.append(_CSV_PATH)

    #Making new objects
    _telphone_book = TelephoneBook()
    _get_data = GetData()

    #Reads the _data from the config
    # human readable
    print(os.listdir(_CFG_PATH))
    # _data = _get_data.get_config(path =_CFG_PATH + 'config.json')
    # _data = _get_data.get_config({'path':_CFG_PATH + 'config.json'})
    # print(_data)

    #Setting the parameters
    _START_FILE = 'ksiazka_telefoniczna.csv'
    _START_DB = 'TRAIS.db'

    def __init__(self):

        self._fileName = self._CSV_PATH + self._START_FILE
        self._db_name = self._DB_PATH + self._START_DB

        # Reads the _data from SQL lite database and sets it into telephone_book attribute
        self.set_telephone_book(self.get_sql_contacts())


    def set_telephone_book(self, telephone_book):
        '''

        :param telephone_book: Function's attribute is an oblect of class TelephoneBook
        :type TelephoneBook
        :return: telephone_book: Returns an object of class TelephoneBook

        Function is a setter of a class attribute telephone_book.

        '''

        self._telphone_book=telephone_book

    def get_telephone_book(self):
        '''

        :return: TelephneBook

        Funtion is a getter, which gets the object of class TelephoneBook from
        from object of class Processing.

        '''

        return self._telphone_book

    def set_start_file(self, file_name):
        '''

        :param file_name: The name of CSV file.
        :type str

        Function is a setter of a class attribute _START_FILE.

        '''
        self._START_FILE = file_name

    def set_start_db(self, db_name):
        '''

        :param db_name: Name of _data base which contains SQL _data
        :type str

        Function is a setter of a class attribute _START_DB.

        '''
        self._START_DB = db_name

    def to_upper_first_character(self, contacts_string):
        '''

        :param contacts_string: Name, Surname, etc.
        :type str
        :return: str or empty str

         Function brings the first character of the string to capital.

        '''
        upper_contacts_string=''
        if contacts_string[0].lower():
            upper_contacts_string = contacts_string[0].upper() + contacts_string[1:]
        return upper_contacts_string

    def from_directory_file_list(self, file_type):

        '''

        :param file_type:
        :type str
        :return: list of strings

        Function from_directory_file_list reads files wiht the type file_type:
        'db', 'csv', 'json' from a directory.
.        '''

        file_type_list=[]

        if file_type == 'db' : file_path = self._DB_PATH
        elif file_type == 'csv' : file_path = self._CSV_PATH
        elif file_type == 'json' : file_path = self._CFG_PATH

        file_list=os.listdir(file_path)

        # file_list=os.listdir(os.getcwd())
        for f in file_list:
            if f.__contains__(file_type):
                file_type_list.append(f[:-len(file_type) - 1])
        return file_type_list

    def temporaryTelephoneBook(self,tempList):
        temp=TelephoneBook()
        temp.__setitem__("temp",tempList)
        return temp

    def mergeTelepchoneBook(self,telephoneBook):
        """
        :param telephoneBook: An object of clas TelephoneBook
        :type
        :return: co zwraca, typ danych i co one oznaczaja
        """
        self._telphone_book.update(telephoneBook)#updates telephone book with new items

    def sortTelephoneBook(self):
        newTelephoneBook=TelephoneBook() #Makes a new _telephone_book
        sorted_list_of_contacts = sorted(self._telphone_book.items(), key=lambda t: t[1].__getitem__(0)) #sorts a items in the book and returns a list
        iterattion=1
        for key in sorted_list_of_contacts:
            newTelephoneBook.__setitem__(iterattion,key[1])#writes to the new book items from the sorted list
            iterattion+=1
        self.set_telephone_book(newTelephoneBook)#sets new book as a telephone book
        return newTelephoneBook

    def findContactSting(self,mySring): #dodac zmiane wielkosci liter na lower zeby poprawnie wyszukac znak i pozniej wrocic
        myList=mySring.split()
        newDictionary=TelephoneBook()
        keyList=[]
        for m in myList:
            for t in self._telphone_book.items():
                for p in t[1]:
                    if p.lower().__contains__(m.lower()):
                        keyList.append(t[0])
                        break
        for k in keyList: newDictionary.__setitem__(k, self._telphone_book[k])
        return newDictionary


    def compareContact(self,telephoneBook):
        p=telephoneBook.values()
        keyList=[]
        for t in self._telphone_book.items():
            if p==t[1]:
                keyList.append(t[0])
        return keyList

    def editContact(self,telephoneBook,pointer,myString):
        myString=self.to_upper_first_character(myString)
        values=(pointer,myString)
        for k in telephoneBook.keys():
            telephoneBook.__setitem__(k,values)
        return telephoneBook

    def editUpdate(self,telephoneBook):
        keyList=self.compareContact(telephoneBook)
        if len(keyList)==0:
            self.mergeTelepchoneBook(telephoneBook)
            new=self.sortTelephoneBook()
            self.insertSqlContacts()
            return len(keyList)==0
        else:
            return len(keyList)==0

    def deleteContact(self,telephoneBook):
        for k in telephoneBook.keys():key=k
        self._telphone_book.__delitem__(key)
        new=self.sortTelephoneBook()
        self.insertSqlContacts()
    # end def

    def newContacts(self,listOnNewUser):
        tempTelephoneBook=self.temporaryTelephoneBook(listOnNewUser)
        keyList=self.compareContact(tempTelephoneBook)
        if len(keyList)==0:
            self.mergeTelepchoneBook(tempTelephoneBook)
            new=self.sortTelephoneBook()
            self.insertSqlContacts()
            return len(keyList)==0
        else:
            return len(keyList)==0

    def get_sql_contacts(self):
        return self._get_data.get_data(self._telphone_book, self._db_name)

    def insertSqlContacts(self):
        self._get_data.insert_data(self._telphone_book, self._db_name)

    def createSqlDb(self,dbBame):
        self.set_start_db(dbBame)
        self._get_data.create_table(self._db_name + ".db")

    def deleteSqlTable(self):
        os.remove(self._db_name)
        flist=self.from_directory_file_list(".db")
        for f in flist:
            if f.__contains__(self._db_name):
                return False
            else:
                return True

    def getCsvContacts(self):
        csvTelephoneBook=TelephoneBook()
        return  self._get_data.get_csv_data(csvTelephoneBook, self._fileName)

    def setCsvContacts(self):
        return  self._get_data.insert_csv_data(self._telphone_book, self._fileName)

