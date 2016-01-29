# -*- coding: utf-8 -*-

import sys
from ksiazka_telefoniczna.Processing import Processing

class Console:
    '''
    Class controls view, of the Telephone Boook
    '''

    # Message to be set in the message box
    message=''

    def __init__(self):
    # initiate controller
        self.process=Processing()

        #starting console menu
        self.menu_root()

    def set_message(self, message):
        '''
        :param message: A message to be placed in the message box.
        :type message: str
        '''
        self.message=message

    def getMessage(self):
        '''
        :return: message
        Function returns a message, a class attribute.
        '''
        return self.message

    def message_box(self):
        '''
        Function prints a message box in the console window.
        '''
        #Program and author
        def top_headder():
            print("#".join(['#' for i in range(1,3)]) + ' Dariusz Łuczyński ' + "#".join(['#' for i in range(1,2)]) \
                  + ' Kiążka Telefoniczna ' + "#".join(['#' for i in range(1,3)]) + ' AGH 2016' + "#".join(['#' for i in range(1,12)]))

        # Full hash line
        def line_hash():
            print("#".join(["#" for i in range(1,40)]))

        def line_message(message):
            patch = "#" + " ".join([" " for i in range(1,2)]) + message
            for j in range(1,80):
                patch=patch + " "
                if len(patch) == 76:
                    patch = patch + "#"
                    break
            print(patch)

        #messenger body
        print('\n')
        top_headder(); line_hash()
        line_message(self.message)
        #line_message("")
        line_hash()

    def to_confirm(self, message):
        '''
        :param message: Message with request of confirmation.
        :type message: str
        :return: True or False
        Function asks to confirm an action.
        '''
        confirmation = input(message + " Naciśnij T/N:")

        # To execute the selected option
        try:
            parameter = str(confirmation)
            if parameter == "t" or parameter == "T":
                return True
            elif parameter == "n" or parameter == "N":
                return False
            else:
                self.set_message("Niewłaściwy znak! Wybierz T lub N.")
                self.message_box()
                self.to_confirm(message)

        except ValueError:
            self.set_message("Niewłaściwy znak! Wybierz T lub N")
            self.message_box()
            self.to_confirm(message)

    def to_print_dictionary(self, print_dictionary):
        '''
        :param print_dictionary: A dictionary to be printed.
        :type print_dictionary: dict
        Prints a dictionary.
        '''
        for d in print_dictionary.values():
            print(d)

    def menu_root(self):
        '''
        Prints a root menu.

                1. Dodaj nowy kontakt
                2. Zarządzaj bazą danych
                3. Zapisz lub pobierz książkę telefoniczną z pliku
                4. Znajdź kontakt
                0. Wyjdź z programu
        '''
        self.message_box()
        print ("1. Dodaj nowy kontakt")
        print ("2. Zarządzaj bazą danych")
        print ("3. Zapisz lub pobierz książkę telefoniczną z pliku")
        print ("4. Znajdź kontakt")
        print ("0. Wyjdź z programu")
        inputParam = input("Wybierz opcję: ")
        print("\n")

        # To execute the selected option
        try:
            parameter = int(inputParam)
            if parameter >= 0 and parameter < 5:
                if parameter == 1:
                    self.set_message("")
                    self.menu_new()
                elif parameter == 2:
                    self.set_message("")
                    self.menu_sql_db()
                elif parameter == 3:
                    self.set_message("")
                    self.menu_csv_file()
                elif parameter == 4:
                    self.set_message("")
                    self.menu_find()
                elif parameter == 0:
                    self.menu_quit()
            else:
                self.set_message("Niewłaściwy numer! Wybierz wartość 1-4.")
                self.message_box()
                self.menu_root()
            #end if
        except ValueError:
            self.set_message("Niewłaściwy znak! Wybierz wartość 1-4.")
            self.message_box()
            self.menu_root()

    def menu_new(self):
        '''
        Sets a new contact to the telephone book.

            1. Podaj imię:
            2. Podaj nazwisko:
            3. Podaj numer telefonu:
            4. Podaj ulicę:
            5. Podaj numer domu i mieszkania:
            6. Podaj kod pocztowy:
            7. Podaj miasto:
            8. Podaj email:

        '''
        self.set_message("")

        def repeat_new_menu(name_user, surname_user, phone_user):
            phone_user = str(phone_user)
            street_user = input("4. Podaj ulicę: ")
            number_user = input("5. Podaj numer domu i mieszkania: ")
            postalcode_user = input("6. Podaj kod pocztowy: ")
            city_user = self.process.to_upper_first_character(input("7. Podaj miasto: "))
            email_user = input("8. Podaj email: ")
            print("\n" + name_user + " " + surname_user + "\n" + phone_user + "\n" + street_user + " " + number_user + "\n" + \
                  postalcode_user +" " + city_user +"\n" + email_user)
            confirmation = self.to_confirm("Czy dane wprowadzono poprawnie?")

            if confirmation:
                do_not_repeats = self.process.new_contacts([name_user, surname_user, phone_user, street_user, number_user, \
                                                        city_user, postalcode_user, email_user])
                #self.process.new_contacts
                if do_not_repeats:
                    self.set_message("Nowy kontakt został dodany do książki telefonicznej.")
                    #self.message_box()
                    self.menu_root()
                else:
                    self.set_message("Kontakt znajduje się już w książce telefonicznej!")
                    self.menu_root()

            else:
                confirm = self.to_confirm("Czy wprowadzić nowy kontakt?")
                if confirm:
                    self.menu_new()
                else:
                    self.set_message("")
                    self.menu_root()

        def new_user_proceed(name_user, surname_user):
            try:
                phone_user = int(input("3. Podaj numer telefonu: "))
                repeat_new_menu(name_user, surname_user, phone_user)
            except ValueError:
                self.set_message("Niewłaściwy znak!")
                self.message_box()
                new_user_proceed(name_user, surname_user)

        name_user = self.process.to_upper_first_character(input("1. Podaj imię: "))#to sort the right way
        surname_user = self.process.to_upper_first_character(input("2. Podaj nazwisko: "))
        new_user_proceed(name_user,surname_user)

    def menu_file_list(self, file_type, start_point=1):
        '''
        :param file_type: Type of the file to be found in a directory.
        :type fileType: str
        :param start_point: Points on the beggining of the list.
        :type start_point: int
        Searches to choose a file from a directory.

            Wartość 3-9, reprezentuje pliki znajdujące się w katalogu domyślnym.
            1. Poprzedni ekran   2. Następny ekran   0. Wyjście do porzedniego menu
            Wybierz plik lub opcję 0-2:
        '''

        def do_vector(pointer, file_list):
            if len(file_list) >= 7:
                if int((pointer - 1)/7) == 0:
                    return [1,8]
                else:
                    return [1, len(file_list) % 7 + 1]
            else:
                return[1, len(file_list) + 1]

        def to_print_file_list(pointer, file_list, display_vector):
             print("".join([str(2 + i) + ". " + file_list[pointer - 2 + i] + "   " for i in range(display_vector[0], display_vector[1])]))

        pointer = start_point
        file_list = self.process.from_directory_file_list(file_type)
        display_vector = do_vector(pointer,file_list)
        to_print_file_list(pointer,file_list,display_vector)

        # To execute the selected option
        try:
            print("\nWartość 3-9, reprezentuje pliki znajdujące się w katalogu domyślnym.")
            print("1. Poprzedni ekran   2. Następny ekran   0. Wyjście do porzedniego menu")
            parameter=int(input("\nWybierz plik lub opcję 0-2: "))

            if parameter >= 0 and parameter <= 9:
                if parameter == 1:
                    self.set_message("")
                    if pointer - 7 >= 0:
                        self.menu_file_list(file_type, pointer - 7)
                    else:
                        self.menu_file_list(file_type, len(file_list) - (len(file_list) % 7) + 1)
                elif parameter == 2:
                    if pointer + 7 < len(file_list):
                        self.menu_file_list(file_type, pointer + 7)
                    else:
                        self.menu_file_list(file_type)
                elif parameter == 0:
                    if file_type== "csv": self.menu_csv_file()
                    elif file_type== "db": self.menu_sql_db()
                else:
                    if file_type == "csv":
                        self.process.set_start_file(file_list[pointer+parameter-4])
                        self.set_message("Wybrano plik " + file_list[pointer + parameter - 4])
                        self.menu_csv_file()
                    elif file_type== "db":
                        self.process.set_start_db(file_list[pointer + parameter - 4])
                        self.set_message("Wybrano bazę " + file_list[pointer + parameter - 4])
                        self.menu_sql_db()
            else:
                self.set_message("Niewłaściwy numer! Wybierz wartość 1-9.")
                self.message_box()
                self.menu_file_list(file_type)
            #end if
        except ValueError:
            self.set_message("Niewłaściwy znak! Wybierz wartość 1-9.")
            self.message_box()
            self.menu_file_list(file_type)

    def menu_sql_db(self):
        '''
        Interface to the SQL _data base.

            1. Zmień bazę danych
            2. Wczytaj kontakty z bazy danych
            3. Stwórz bazę danych
            4. Usuń bazę danych
            0. Wyjdź z programu
        '''
        self.set_message("")
        self.message_box()
        type="db"

        print ("1. Zmień bazę danych")
        print ("2. Wczytaj kontakty z bazy danych")
        print ("3. Stwórz bazę danych")
        print ("4. Usuń bazę danych")
        print ("0. Wyjdź z programu")
        input_param=input("Wybierz opcję: ")
        print("\n")

        # To execute the selected option
        try:
            parameter = int(input_param)
            if parameter >= 0 and parameter<5:
                if parameter == 1:
                    self.set_message("")
                    self.message_box()
                    self.menu_file_list(type)

                elif parameter == 2:
                    self.set_message("")
                    self.message_box()
                    sql_dictionary = self.process.get_sql_contacts()
                    self.to_print_dictionary(sql_dictionary)
                    confirm=self.to_confirm("Dodać dane?")
                    if confirm:
                        self.process.edit_update(sql_dictionary)
                        self.menu_sql_db()
                    else:
                        self.menu_sql_db()
                elif parameter == 3:
                    file_name = input("Wprowadź nazwę dla pliku .db:")
                    # self.process.set_start_db=_fileName
                    self.process.create_sql_db(file_name)
                    self.set_message("Baza została stworzona")
                    self.menu_sql_db()
                elif parameter == 4:
                    table_delete = self.process.delete_sql_table()
                    if table_delete: self.set_message("Baza danych została usunięta.")
                    else: self.set_message("Brak bazy danych w liście.")
                    self.menu_file_list(type)
                elif parameter == 0:
                    self.set_message("")
                    self.message_box()
                    self.menu_root()
            else:
                self.set_message("Niewłaściwy numer! Wybierz wartość 1-4.")
                self.message_box()
                self.menu_sql_db()
            #end if
        except ValueError:
            self.set_message("Niewłaściwy znak! Wybierz wartość 1-4.")
            self.message_box()
            self.menu_sql_db()

    def menu_csv_file(self):
        '''
        Import or export data to/from a CSV file.
            1. Wybierz plik CSV
            2. Wczytaj kontakty z pliku CSV
            3. Zapisz dane do pliku CSV
            0. Wyjdź z programu
        '''
        self.set_message("")
        self.message_box()

        #print(self.message)
        print ("1. Wybierz plik CSV")
        print ("2. Wczytaj kontakty z pliku CSV")
        print ("3. Zapisz dane do pliku CSV")
        print ("0. Wyjdź z programu")
        input_param = input("Wybierz opcję: ")
        print("\n")

        # To execute the selected option
        try:
            parameter = int(input_param)
            if parameter >= 0 and parameter < 4:
                if parameter == 1:
                    self.set_message("")
                    self.message_box()
                    type = "csv"
                    self.menu_file_list(type)

                elif parameter == 2:
                    self.set_message("")
                    self.message_box()
                    csv_dictionary = self.process.get_csv_contacts()
                    self.to_print_dictionary(csv_dictionary)
                    confirm = self.to_confirm("Dodać dane?")
                    if confirm:
                        self.process.edit_update(csv_dictionary)
                        self.menu_csv_file()
                    else:
                        self.menu_csv_file()
                elif parameter == 3:
                    self.process.set_csv_contacts()
                elif parameter == 0:
                    self.set_message("")
                    self.menu_root()
            else:
                self.set_message("Niewłaściwy numer! Wybierz wartość 1-4.")
                self.menu_csv_file()
        except ValueError:
            self.set_message("Niewłaściwy znak! Wybierz wartość 1-4.")
            self.menu_csv_file()

    def menu_find(self):
        '''
        Finds a contact in the database with requested string.

            Po wyszukaniu jednego kontaktu możliwa jest jego edycja oraz jego usunięcie
            1. Wyszukaj kontakt
            0. Wróć do menu główneg

            pisz tekst aby wyszukać kontakt:

            Wybierz pole, które chcesz edytować:
            1. Imię           2. Nazwisko                3. Numer telefonu
            4. Ulica          5. Numer domu/mieszkania   6. Miasto
            7. Kod pocztowy   8. Email                   0. Wyjście

        If one contact is found the menu enables it to edit or delete.

            1. Edytuj kontakt:
            5. Usuń kontakt:
            0. Wyjdź z menu:
        '''

        def int_check():
            try:
                my_string=input("Podaj nową wartość: ")
                int(my_string) #checks String
                return my_string

            except ValueError:
                self.set_message("Niewłaściwy znak!")
                self.message_box()
                int_check()

        def sub_menu_edit_contact(new_dictionary):
            print("Wybierz pole, które chcesz edytować: ")
            print("1. Imię           2. Nazwisko                3. Numer telefonu")
            print("4. Ulica          5. Numer domu/mieszkania   6. Miasto")
            print("7. Kod pocztowy   8. Email                   0. Wyjście")
            input_param = input("Wybierz opcję: ")

            # To execute the selected option
            try:
                parameter = int(input_param)
                if parameter >= 0 and parameter <= 8:
                    if parameter == 0:
                        confirm = self.to_confirm("Zapisać zmiany? ")
                        if confirm:
                            update = self.process.edit_update(new_dictionary)
                            if update:
                                self.set_message("Zmiany zapisano")
                                self.message_box()
                                self.menu_find()
                            else:
                                self.set_message("Kontakt już znajduje się w książce telefonicznej")
                                self.message_box()
                                sub_menu_edit_contact(new_dictionary)

                    elif parameter == 3:
                        my_string = int_check()
                        new_dictionary = self.process.edit_contact(new_dictionary, parameter - 1, my_string)
                        sub_menu_edit_contact(new_dictionary)

                    else:
                        self.set_message("")
                        self.message_box()
                        my_string = input("Podaj nową wartość: ")
                        new_dictionary = self.process.edit_contact(new_dictionary, parameter - 1, my_string)
                        sub_menu_edit_contact(new_dictionary)

                else:
                    self.set_message("Niewłaściwy numer! Wybierz wartość 1,5 lub 0.")
                    sub_menu_find_edit(new_dictionary)

            except ValueError:
                self.set_message("Niewłaściwy znak! Wybierz wartość 1,5 lub 0.")
                sub_menu_find_edit(new_dictionary)

        def sub_menu_find_edit(new_dictionary):
            print("1. Edytuj kontakt: ")
            print("5. Usuń kontakt: ")
            print("0. Wyjdź z menu: ")

            input_param = input("Wybierz opcję: ")
            print("\n")

            # To execute the selected option
            try:
                parameter = int(input_param)
                if parameter == 0 or parameter == 5 or parameter == 1:
                    if parameter == 1:
                        self.set_message("")
                        self.message_box()
                        sub_menu_edit_contact(new_dictionary)

                    elif parameter == 5:
                        confirm = self.to_confirm("Kontakt zostanie usunięty. ")
                        if confirm:
                            self.process.delete_contact(new_dictionary)
                            self.set_message("Kontakt został usunięty")
                            self.message_box()
                            self.menu_find()
                        else:
                            self.set_message("")
                            self.message_box()
                            sub_menu_find_edit(new_dictionary)
                    elif parameter==0:
                        self.menu_find()

                else:
                    self.set_message("Niewłaściwy numer! Wybierz wartość 1,5 lub 0.")
                    sub_menu_find_edit(new_dictionary)

            except ValueError:
                self.set_message("Niewłaściwy znak! Wybierz wartość 1,5 lub 0.")
                sub_menu_find_edit(new_dictionary)

        def sub_menu_find():

            find_string=input("Wpisz tekst aby wyszukać kontakt: ")
            new_dictionary=self.process.find_contact_sting(find_string)

            if len(new_dictionary) == 0:
                self.set_message("Brak kontaktów.")
                self.message_box()
                self.menu_find()

            elif len(new_dictionary) == 1:
                self.to_print_dictionary(new_dictionary)
                sub_menu_find_edit(new_dictionary)

            elif len(new_dictionary) > 1:
                self.to_print_dictionary(new_dictionary)
                self.set_message("")
                self.message_box()
                self.menu_find()

        print ("Po wyszukaniu jednego kontaktu możliwa jest jego edycja oraz jego usunięcie")
        print ("1. Wyszukaj kontakt")
        print ("0. Wróć do menu głównego")

        input_param = input("Wybierz opcję: ")
        print("\n")

        # To execute the selected option
        try:
            parameter = int(input_param)
            if parameter >= 0 and parameter <= 1:
                if parameter == 1:
                    self.set_message("")
                    self.message_box()
                    sub_menu_find()

                elif parameter == 0:
                    self.set_message("")
                    self.message_box()
                    self.menu_root()
            else:
                self.set_message("Niewłaściwy numer! Wybierz wartość 0-1.")
                self.menu_find()

        except ValueError:
            self.set_message("Niewłaściwy znak! Wybierz wartość 0-1.")
            self.menu_find()

    def menu_quit(self):
        '''
        Saves configuration and quits console menu.
        '''
        self.process.save_configuration()




