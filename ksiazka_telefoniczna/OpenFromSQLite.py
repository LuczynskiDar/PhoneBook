# -*- coding: utf-8 -*-

import sqlite3

class OpenFromSQLite():
    '''
        OpenFromSQLite class includes methods, which create, set and get _data
        from tne SQL lite _data base.
    '''

    _TABLE_NAME = 'KSIAZKA_TEL'
    _TABLE=("ID", "NAME", "SURNAME", "TELEPHONE", "STREET", "NUMBER", "CITY", "POSTALCODE", "EMAIL")
    # __TABLE = ['','','','','','','','']

    def __init__(self):
        pass

    # def __getattr__(self, item):
    #     return self.item

    def get_sql_table(self):
        '''
        :returns: TABLE
        Gets TABLE, a class attribute from OpenFromSQLite object.
        '''
        return self._TABLE

    def to_table_string(self):
        '''
        :return: str
        Prepares a string of columns to by placed in SQL table.
        '''
        return "".join([self._TABLE[i] + ',' for i in range(0, len(self._TABLE) - 1)]) + self._TABLE[len(self._TABLE) - 1]

    def get_data(self, telephone_book, db_name):
        '''
        :param telephone_book: A empty collection to be reffiled with the data from SQL database.
        :type telephone_book: TelephoneBook
        :param db_name: Name of the db file.
        :type db_name: str
        :return: TelephoneBook
        Picks the data from SQL table.
        '''
        conn = sqlite3.connect(db_name)
        cursor = conn.execute("SELECT " + self.to_table_string() + " from " + self._TABLE_NAME + ";")
        for row in cursor:
           telephone_book.__setitem__(row[0], list(row[1:9]))
        conn.close()
        return telephone_book

    def insert_data(self, telephone_book, db_name):
        '''
        :param telephone_book: Data to be inserted into SQL database.
        :type telephone_book: TelephoneBook
        :param db_name: Name of the database
        :type db_name:str
        :returns: TelephoneBook
        Function, wnich inserts data into a SQL database.
        '''
        conn = sqlite3.connect(db_name)
        primaryKey=1
        conn.execute("DELETE FROM " + self._TABLE_NAME + ";")
        for t in telephone_book.values():
            conn.execute("INSERT INTO " + self._TABLE_NAME + "(" + self.to_table_string() + ")" + " VALUES (" + str(primaryKey) +\
                         "," + t.to_table_values() + ");")
            primaryKey+=1
        conn.commit()
        conn.close()

    def create_table(self, db_name):
        '''
        :param dbName: Name of a new database.
        :type db_name: str
        Creates SQL database.
        '''
        conn = sqlite3.connect(db_name)
        conn.execute("CREATE TABLE " + self._TABLE_NAME + \
               "(ID INT PRIMARY KEY     NOT NULL,"
               "NAME           TEXT    NOT NULL,"
               "SURNAME        TEXT    NOT NULL,"
               "TELEPHONE      INT    NOT NULL,"
               "STREET         TEXT,"
               "NUMBER         TEXT     NOT NULL,"
               "CITY           TEXT    NOT NULL,"
               "POSTALCODE     TEXT    NOT NULL,"
               "EMAIL         TEXT);")

        conn.close()
