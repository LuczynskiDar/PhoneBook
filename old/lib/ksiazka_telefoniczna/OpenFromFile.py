# -*- coding: utf-8 -*-

import csv

class OpenFromFile():

    """

        :parameter _TABLE : Defines the columns in CSV file
        :type list

        Class opens and saves coma separated file: CSV. There
        is one class attribute, _TABLE. It is apploaded from the
        JSON file.

    """
    _TABLE=["ID", "NAME", "SURNAME", "TELEPHONE", "STREET", "NUMBER", "CITY", "POSTALCODE", "EMAIL"]

    def __init__(self):
        pass

    def set_table(self,table):
        '''

        :param table: Columns of the CSV file.
        :type list

            Setter of the OpenFromFile class attribute, _Table

        '''

        self._TABLE=table

    def insert_csv_data(self, telephone_book, file_name): #opens file

        '''

        :param telephone_book: An object of the class TelephoneBook
        :type TelephoneBook
        :param file_name: A path to the CSV filename and filenam
        :type str

        Inserts _data into CSV file with predefined quantity of columns.

        '''

        try:
             with open(file_name, 'w') as csvfile:
                filewriter = csv.writer(csvfile, delimiter = ',', lineterminator = "\n")
                filewriter.writerow(self._TABLE)
                t=telephone_book
                for v in telephone_book.values():
                   filewriter.writerow(v.__getitem__([]))
        finally:
             csvfile.close()

    def get_csv_data(self, telephone_book, file_name):
        '''

        :param telephone_book: An oblect of the class TelephoneBook.
        :type TelephoneBook
        :param file_name: A path to a CSV file and filename.
        :type str
        :return: An object of class TelephoneBook.

        Gets _data from the CSV file.

        '''
        try:
            with open(file_name, 'r') as f:
                reader = csv.reader(f)
                # read file row by row
                row_nr = 0
                #Skip the header row.
                for row in reader: #row is a type of list
                    if row_nr >= 1:
                        telephone_book.__setitem__(row_nr, row)
                    # Increase the row number
                    row_nr = row_nr + 1
                #end for
            return telephone_book
        finally:
            f.close()
    #end def