# -*- coding: utf-8 -*-

import sqlite3

class OpenFromSQLite():
    '''

        OpenFromSQLite class includes methods, which create, set and get _data
        from tne SQL lite _data base.

    '''

    _TABLE_NAME = 'KSIAZKA_TEL'
    _TABLE=("ID", "NAME", "SURNAME", "TELEPHONE", "STREET", "NUMBER", "CITY", "POSTALCODE", "EMAIL")

    def __init__(self):
        pass

    # def __getattr__(self, item):
    #     return self.item

    def get_sql_table(self):
        return self._TABLE

    def to_table_string(self):
       return "".join([self._TABLE[i] + ',' for i in range(0, len(self._TABLE) - 1)]) + self._TABLE[len(self._TABLE) - 1]

    def get_data(self, telephone_book, db_name):
        conn = sqlite3.connect(db_name)
        cursor = conn.execute("SELECT " + self.to_table_string() + " from " + self._TABLE_NAME + ";")
        for row in cursor:
           telephone_book.__setitem__(row[0], list(row[1:9]))
        conn.close()
        return telephone_book

    def insert_data(self, telephone_book, db_name):
        conn = sqlite3.connect(db_name)
        primaryKey=1
        conn.execute("DELETE FROM " + self._TABLE_NAME + ";")
        for t in telephone_book.values():
            conn.execute("INSERT INTO " + self._TABLE_NAME + "(" + self.to_table_string() + ")" + " VALUES (" + str(primaryKey) +\
                         "," + t.to_table_values() + ");")
            primaryKey+=1
        conn.commit()
        conn.close()

    def create_table(self, dbName):
        conn = sqlite3.connect(dbName)
        conn.execute("CREATE TABLE " + self._TABLE_NAME + \
               '''(ID INT PRIMARY KEY     NOT NULL,
               NAME           TEXT    NOT NULL,
               SURNAME        TEXT    NOT NULL,
               TELEPHONE      INT    NOT NULL,
               STREET         TEXT,
               NUMBER         TEXT     NOT NULL,
               CITY           TEXT    NOT NULL,
               POSTALCODE     TEXT    NOT NULL,
               EMAIL         TEXT);''')

        conn.close()
