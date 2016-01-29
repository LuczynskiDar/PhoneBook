# -*- coding: utf-8 -*-

from ksiazka_telefoniczna.GetData import GetData
from ksiazka_telefoniczna.TelephoneBook import TelephoneBook
import os,sys,pkgutil,pkg_resources

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
    _telephone_book = TelephoneBook()
    _get_data = GetData()

    #Reads the _data from the config
    _config_file = 'config.json'
    # human readable
    # print(os.listdir(_CFG_PATH))
    _data = _get_data.get_config(path = _CFG_PATH + _config_file)
    # _data = _get_data.get_config({'path':_CFG_PATH + 'config.json'})
    # print(_data)

    #Setting the parameters
    _START_FILE = _data['START_FILE']
    _START_DB = _data['START_DB']
    _TABLE_NAME = _data['TABLE_NAME']
    _TABLE = _data['TABLE']

    def __init__(self):

        self._fileName = self._CSV_PATH + self._START_FILE
        self._db_name = self._DB_PATH + self._START_DB

        # Reads the _data from SQL lite database and sets it into telephone_book attribute
        self.set_telephone_book(self.get_sql_contacts())


    def set_telephone_book(self, telephone_book):
        '''
        :type TelephoneBook
        :return: telephone_book: Returns an object of class TelephoneBook

        Function is a setter of a class attribute telephone_book.
        '''

        self._telephone_book=telephone_book

    def get_telephone_book(self):
        '''
        :return: TelephneBook

        Funtion is a getter, which gets the object of class TelephoneBook from
        from object of class Processing.
        '''

        return self._telephone_book

    def set_start_file(self, file_name):
        '''
        :param file_name: The name of CSV file.
        :type file_name: str
        Function is a setter of a class attribute _START_FILE.

        '''
        self._START_FILE = file_name

    def set_start_db(self, db_name):
        '''
        :param db_name: Name of _data base which contains SQL _data
        :type db_name: str
        Function is a setter of a class attribute _START_DB.
        '''
        self._START_DB = db_name
        self._db_name = self._DB_PATH + self._START_DB

    def to_upper_first_character(self, contacts_string):
        '''
        :param contacts_string: Name, Surname, etc.
        :type contacts_string: str
        :returns: str or empty str

         Function brings the first character of the string to capital.
        '''
        upper_contacts_string=''
        if contacts_string[0].lower():
            upper_contacts_string = contacts_string[0].upper() + contacts_string[1:]
        return upper_contacts_string

    def from_directory_file_list(self, file_type):

        '''
        :param file_type: Could be 'db', 'csv', 'json'
        :type file_type: str
        :returns: list of strings
        Function from_directory_file_list reads files wiht the type file_type:
        'db', 'csv', 'json' from a directory.
.        '''

        file_type_list=[]

        #filetype entry is .db, .csv
        if file_type.__contains__('db'): file_path = self._DB_PATH
        elif file_type.__contains__('csv'):  file_path = self._CSV_PATH
        elif file_type.__contains__('json'): file_path = self._CFG_PATH

        # print(file_path)

        file_list=os.listdir(file_path)

        # file_list=os.listdir(os.getcwd())
        for f in file_list:
            if f.__contains__('.'+file_type):
                file_type_list.append(f)
                # file_type_list.append(f[:-len(file_type)])
                # file_type_list.append(f[:-len(file_type) - 1])
        return file_type_list

    def temporary_telephone_book(self, temp_list):
        '''
        :param temp_list: List of parameters for a new contact.
        :type list
        :return: TelephoneBook
        Function temporary_telephone_book makes a temporary object of class TelephoneBook.
        '''
        temp=TelephoneBook()
        temp.__setitem__("temp", temp_list)
        return temp

    def merge_telephone_book(self, telephone_book):
        """
        :param telephone_book: An object of class TelephoneBook
        :type telephone_book: TelephoneBook
        :returns  TelephoneBook
        Function merges two objects of class TelephoneBook.
        """
        self._telephone_book.update(telephone_book)#updates telephone book with new items

    def sort_telephone_book(self):
        '''
        :returns: TelephoneBook
        Function sorts the object's Procosseng class attribute: telephone_book.
        '''
        new_telephone_book=TelephoneBook() #Makes a new _telephone_book
        sorted_list_of_contacts = sorted(self._telephone_book.items(), key = lambda t: t[1].__getitem__(0)) #sorts a items in the book and returns a list
        iterattion = 1
        for key in sorted_list_of_contacts:
            new_telephone_book.__setitem__(iterattion,key[1])#writes to the new book items from the sorted list
            iterattion+=1
        self.set_telephone_book(new_telephone_book)#sets new book as a telephone book
        return new_telephone_book

    def find_contact_sting(self, my_sring):
        '''
        :param my_sring: String to be found
        :type my_sring: str
        :returns: TelephoneBook
        Returns a TelephoneBook object with all the data that contains desired string.
        '''
        my_list=my_sring.split()
        new_dictionary=TelephoneBook()
        key_list=[]
        for m in my_list:
            for t in self._telephone_book.items():
                for p in t[1]:
                    if p.lower().__contains__(m.lower()):
                        key_list.append(t[0])
                        break
        for k in key_list: new_dictionary.__setitem__(k, self._telephone_book[k])
        return new_dictionary

    def compare_contact(self, telephone_book):
        '''
        :param telephone_book: A TelephoneBook object to compare with telephone_book class Processing's attribute.
        :type telephone_book: TelephoneBook
        :returns: list of the keys of data whicha are the same
        Function compares values of two objects of class TelephoneBook.
        '''
        p=telephone_book.values()
        key_list=[]
        for t in self._telephone_book.items():
            if p==t[1]:
                key_list.append(t[0])
        return key_list

    def edit_contact(self, telephone_book, pointer, my_string):
        '''

        :param telephone_book: TelephoneBook object to be edited
        :type telephone_book: TelephoneBook
        :param pointer: Points on an item from a table in object Person.
        :type pointer: int
        :param my_string: Desired string to be changed.
        :type my_string: str
        :returns: TelephoneBook

        Function which edits contats in Peocessing class attribute telephone_book.
        '''
        my_string=self.to_upper_first_character(my_string)
        values=(pointer, my_string)
        for k in telephone_book.keys():
            telephone_book.__setitem__(k, values)
        return telephone_book

    def edit_update(self, telephone_book):
        '''
        :param telephone_book: An object of class TelephoneBook, which contains contacts.
        :type telephone_book: TelephoneBook
        :returns: True or False
        Function checks if there are the same contacts on the contact list, if they are different SQL
        Lite database is being updated.
        '''
        key_list=self.compare_contact(telephone_book)
        if len(key_list)==0:
            self.merge_telephone_book(telephone_book)
            self.sort_telephone_book()
            # new=self.sort_telephone_book()
            self.insert_sql_contacts()
            return len(key_list)==0
        else:
            return len(key_list)==0

    def delete_contact(self, telephone_book):
        '''

        :param telephone_book: Object of class TelephoneBook, which contains one contact.
        :type telephone_book: TelephoneBook
        Function delete_contact removes one contact from telephone_book.
         '''
        for k in telephone_book.keys():key=k
        self._telephone_book.__delitem__(key)
        self.sort_telephone_book()
        self.insert_sql_contacts()

    def new_contacts(self, list_of_new_user):
        '''

        :param list_of_new_user: New contact data
        :type list_of_new_user: list
        :returns: True or False
        Function new_contacts makes a new contact from the list of strings.
        Comopare if the contact exists, then inserts into the database.
        '''
        temp_telephone_book=self.temporary_telephone_book(list_of_new_user)
        key_list=self.compare_contact(temp_telephone_book)
        if len(key_list)==0:
            self.merge_telephone_book(temp_telephone_book)
            self.sort_telephone_book()
            self.insert_sql_contacts()
            return len(key_list)==0
        else:
            return len(key_list)==0

    def get_sql_contacts(self):
        '''
        Function get_sql_contacts downloads data from the SQL database.
        :return:
        '''
        return self._get_data.get_data(self._telephone_book, self._db_name)

    def insert_sql_contacts(self):
        '''
        Function insert_sql_contacts inserts data into SQL database.
        '''
        self._get_data.insert_data(self._telephone_book, self._db_name)

    def create_sql_db(self, db_name):
        '''

        :param db_name: Name of new database file.
        :type db_name: str
        Makes new sql database.
        '''
        # self.set_start_db(db_name)
        self._get_data.create_table(self._DB_PATH + db_name + '.db')
        # self._get_data.create_table(self._db_name + ".db")

    def delete_sql_table(self):
        '''
        :returns: True or False
        Removes SQL lite 'db' file from the 'db' directory. File name is set by variable db_name.
        '''

        flist = self.from_directory_file_list("db")
        container = False
        # print(sys.path)
        for f in flist:
            if f.__contains__(self._START_DB):
                os.remove(self._db_name)
                container = True
                break
        return container

    def get_csv_contacts(self):
        '''
        :returns: TelephoneBook
        Fuction get_csv_contacts picks contacts from CSV file.
        '''
        csv_telephone_book=TelephoneBook()
        return  self._get_data.get_csv_data(csv_telephone_book, self._fileName)

    def set_csv_contacts(self):
        '''
        Function set_csv_contacts exports TelephoneBook into CSV file.
        '''
        self._get_data.insert_csv_data(self._telephone_book, self._fileName)

    def save_configuration(self):
        '''
        Function save_configuration saves final configuration of the START_FILE, START_DB,
        TABLE_NAME and TABLE to the JSON configuration file.
        '''
        self._get_data.insert_config(path = self._CFG_PATH + self._config_file , START_FILE = self._START_FILE, \
                                     START_DB = self._START_DB, TABLE_NAME = self._TABLE_NAME, TABLE = self._TABLE)
