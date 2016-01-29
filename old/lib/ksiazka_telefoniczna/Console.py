# -*- coding: utf-8 -*-

import sys
from ksiazka_telefoniczna.Processing import Processing

class Console:
    '''
    Class controls view, of the Telephone Boook
    '''
    #Class atributes
    message=""
    __level=0
    errorList={}
    def __init__(self):
    # def __init__(self,PATH):
        #path set
        # print(PATH)
        # sys.path.append(PATH)
        #initiate controller
        self.process=Processing()
        #loading the _data base
        # self.process.get_sql_contacts()
        #starting console menu
        self.menuRoot()


    #end def

    def setMessage(self,message):
        self.message=message
    #end def

    def getMessage(self):
        return self.message

    def messager(self):
        # Full hash line
        def lineHash():
            print("#".join(["#" for i in range(1,40)]))
        #end def

        def lineMessage(message):
            patch="#"+" ".join([" " for i in range(1,2)])+message
            for j in range(1,80):
                patch=patch+" "
                if len(patch)==76:
                    patch=patch+"#"
                    break
            print(patch)
        #end def

        #messenger body
        print('\n'); lineHash()
        #lineMessage("")
        lineMessage(self.message)
        #lineMessage("")
        lineHash()
    #end def

    def toConfirm(self,message):
        confirmation=input(message+" Naciśnij T/N:")

        # To execute the selected option
        try:
            parameter=str(confirmation)
            if parameter=="t" or parameter=="T":
                return True
            elif parameter=="n" or parameter=="N":
                return False
            else:
                self.setMessage("Niewłaściwy znak! Wybierz T lub N.")
                self.messager()
                self.toConfirm(message)
            #end if
        except ValueError:
            self.setMessage("Niewłaściwy znak! Wybierz T lub N")
            self.messager()
            self.toConfirm(message)

    def toPrintDictionary(self,printDictionary):
        for d in printDictionary.values():
            print(d)

    def menuRoot(self):
        self.messager()
        print ("1. Dodaj nowy kontakt")
        print ("2. Zarządzaj bazą danych")
        print ("3. Zapisz lub pobierz książkę telefoniczną z pliku")
        print ("4. Znajdź kontakt")
        print ("0. Wyjdź z programu")
        inputParam=input("Wybierz opcję: ")
        print("\n")

        # To execute the selected option
        try:
            parameter=int(inputParam)
            if parameter>=0 and parameter<5:
                if parameter==1:
                    self.setMessage("")
                    self.menuNew()
                elif parameter==2:
                    self.setMessage("")
                    self.menuSqlDb()
                elif parameter==3:
                    self.setMessage("")
                    self.menuCsvFile()
                elif parameter==4:
                    self.setMessage("")
                    self.menuFind()
                elif parameter==0:
                    self.menuQuit()
            else:
                self.setMessage("Niewłaściwy numer! Wybierz wartość 1-4.")
                self.messager()
                self.menuRoot()
            #end if
        except ValueError:
            self.setMessage("Niewłaściwy znak! Wybierz wartość 1-4.")
            self.messager()
            self.menuRoot()

    def menuNew(self):
        self.setMessage("")

        def repeatNewMenu(nameUser,surnameUser,phoneUser):
            phoneUser=str(phoneUser)
            streetUser=input("4. Podaj ulicę: ")
            numberUser=input("5. Podaj numer domu i mieszkania: ")
            postalcodeUser=input("6. Podaj kod pocztowy: ")
            cityUser=self.process.to_upper_first_character(input("7. Podaj miasto: "))
            emailUser=input("8. Podaj email: ")
            print("\n"+nameUser+" "+surnameUser+"\n"+phoneUser+"\n"+streetUser+" "+numberUser+"\n"+\
                              postalcodeUser+" "+cityUser+"\n"+emailUser)
            confirmation=self.toConfirm("Czy dane wprowadzono poprawnie?")

            if confirmation:
                doNotRepeats=self.process.new_contacts([nameUser, surnameUser, phoneUser, streetUser, numberUser, \
                                                        cityUser, postalcodeUser, emailUser])
                #self.process.new_contacts
                if doNotRepeats:
                    self.setMessage("Nowy kontakt został dodany do książki telefonicznej.")
                    #self.message_box()
                    self.menuRoot()
                else:
                    self.setMessage("Kontakt znajduje się już w książce telefonicznej!")
                    self.menuRoot()

            else:
                confirm=self.toConfirm("Czy wprowadzić nowy kontakt?")
                if confirm:
                    self.menuNew()
                else:
                    self.setMessage("")
                    self.menuRoot()

        def newUserProceed(nameUser,surnameUser):
            try:
                phoneUser=int(input("3. Podaj numer telefonu: "))
                repeatNewMenu(nameUser,surnameUser,phoneUser)
            except ValueError:
                self.setMessage("Niewłaściwy znak!")
                self.messager()
                newUserProceed(nameUser,surnameUser)

        nameUser=self.process.to_upper_first_character(input("1. Podaj imię: "))#to sort the right way
        surnameUser=self.process.to_upper_first_character(input("2. Podaj nazwisko: "))
        newUserProceed(nameUser,surnameUser)

    def menuFilelist(self,fileType,startPoint=1):

        def doVector(pointer,fileList):
            if len(fileList)>=7:
                if int((pointer-1)/7)==0:
                    return [1,8]
                else:
                    return [1,len(fileList)%7+1]
            else:
                return[1,len(fileList)+1]

        def toPrintFileList(pointer,fileList,displayVector):
             print("".join([str(2+i)+". "+fileList[pointer-2+i]+"   " for i in range(displayVector[0],displayVector[1])]))

        pointer=startPoint
        fileList=self.process.from_directory_file_list(fileType)
        displayVector=doVector(pointer,fileList)
        toPrintFileList(pointer,fileList,displayVector)

        # To execute the selected option
        try:
            print("\nWartość 3-9, reprezentuje pliki znajdujące się w katalogu domyślnym.")
            print("1. Poprzedni ekran   2. Następny ekran   0. Wyjście do porzedniego menu")
            parameter=int(input("\nWybierz plik lub opcję 0-2: "))

            if parameter>=0 and parameter<=9:
                if parameter==1:
                    self.setMessage("")
                    if pointer-7>=0:
                    # if pointer-7>=0:
                        self.menuFilelist(fileType,pointer-7)
                    else:
                        self.menuFilelist(fileType,len(fileList)-(len(fileList)%7)+1)
                elif parameter==2:
                    if pointer+7<len(fileList):
                    # if pointer+7<len(fileList):
                        self.menuFilelist(fileType,pointer+7)
                    else:
                        self.menuFilelist(fileType)
                elif parameter==0:
                    print("menu 0")
                    if fileType=="csv": self.menuCsvFile()
                    elif fileType=="db": self.menuSqlDb()
                else:
                    if fileType=="csv":
                        self.process.set_start_file(fileList[pointer+parameter-4]+"."+fileType)
                        # self.process.setFileName(fileList[pointer+parameter-4]+"."+fileType)
                        self.setMessage("Wybrano plik "+fileList[pointer+parameter-4])
                        self.menuCsvFile()
                    elif fileType=="db":
                        self.process.set_start_db(fileList[pointer + parameter - 4] + "." + fileType)
                        self.setMessage("Wybrano bazę "+fileList[pointer+parameter-4])
                        self.menuSqlDb()
            else:
                self.setMessage("Niewłaściwy numer! Wybierz wartość 1-9.")
                self.messager()
                self.menuFilelist(fileType)
            #end if
        except ValueError:
            self.setMessage("Niewłaściwy znak! Wybierz wartość 1-9.")
            self.messager()
            self.menuFilelist(fileType)

    def menuSqlDb(self):
        self.setMessage("")
        self.messager()
        print ("1. Zmień bazę danych")
        print ("2. Wczytaj kontakty z bazy danych")
        print ("3. Stwórz bazę danych")
        print ("4. Usuń bazę danych")
        print ("0. Wyjdź z programu")
        inputParam=input("Wybierz opcję: ")
        print("\n")

        # To execute the selected option
        try:
            parameter=int(inputParam)
            if parameter>=0 and parameter<5:
                if parameter==1:
                    self.setMessage("")
                    self.messager()
                    type="db"
                    self.menuFilelist(type)

                elif parameter==2:
                    self.setMessage("")
                    self.messager()
                    sqlDictionary=self.process.get_sql_contacts()
                    self.toPrintDictionary(sqlDictionary)
                    confirm=self.toConfirm("Dodać dane?")
                    if confirm:
                        self.process.edit_update(sqlDictionary)
                        self.menuSqlDb()
                    else:
                        self.menuSqlDb()
                elif parameter==3:
                    fileName=input("Wprowadź nazwę dla pliku .db:")
                    # self.process.set_start_db=_fileName
                    self.process.create_sql_db(fileName)
                    self.setMessage("Baza została stworzona")
                    self.menuSqlDb()
                elif parameter==4:
                    self.process. delete_sql_table()
                elif parameter==0:
                    self.setMessage("")
                    self.messager()
                    self.menuRoot()
            else:
                self.setMessage("Niewłaściwy numer! Wybierz wartość 1-4.")
                self.messager()
                self.menuSqlDb()
            #end if
        except ValueError:
            self.setMessage("Niewłaściwy znak! Wybierz wartość 1-4.")
            self.messager()
            self.menuSqlDb()

    def menuCsvFile(self):
        self.setMessage("")
        self.messager()
        #print(self.message)
        print ("1. Wybierz plik CSV")
        print ("2. Wczytaj kontakty z pliku CSV")
        print ("3. Zapisz dane do pliku CSV")
        print ("0. Wyjdź z programu")
        inputParam=input("Wybierz opcję: ")
        print("\n")

        # To execute the selected option
        try:
            parameter=int(inputParam)
            if parameter>=0 and parameter<4:
                if parameter==1:
                    self.setMessage("")
                    self.messager()
                    type="csv"
                    self.menuFilelist(type)

                elif parameter==2:
                    self.setMessage("")
                    self.messager()
                    csvDictionary=self.process.get_csv_contacts()
                    self.toPrintDictionary(csvDictionary)
                    confirm=self.toConfirm("Dodać dane?")
                    if confirm:
                        self.process.edit_update(csvDictionary)
                        self.menuCsvFile()
                    else:
                        self.menuCsvFile()
                elif parameter==3:
                    self.setCsvContacts()
                elif parameter==0:
                    self.setMessage("")
                    self.menuRoot()
            else:
                self.setMessage("Niewłaściwy numer! Wybierz wartość 1-4.")
                self.menuCsvFile()
            #end if
        except ValueError:
            self.setMessage("Niewłaściwy znak! Wybierz wartość 1-4.")
            self.menuCsvFile()

    def menuFind(self):

        def intCheck():
            try:
                myString=input("Podaj nową wartość: ")
                checkString=int(myString)
                return myString

            except ValueError:
                self.setMessage("Niewłaściwy znak!")
                self.messager()
                intCheck()

        def subMenuEditContact(newDictionary):
            print("Wybierz pole, które chcesz edytować: ")
            print("1. Imię           2. Nazwisko                3. Numer telefonu")
            print("4. Ulica          5. Numer domu/mieszkania   6. Miasto")
            print("7. Kod pocztowy   8. Email                   0. Wyjście")
            inputParam=input("Wybierz opcję: ")

            # To execute the selected option
            try:
                parameter=int(inputParam)
                if parameter>=0 and parameter<=8:
                    if parameter==0:
                        confirm=self.toConfirm("Zapisać zmiany? ")
                        if confirm:

                            update=self.process.edit_update(newDictionary)
                            if update:
                                self.setMessage("Zmiany zapisano")
                                self.messager()
                                self.menuFind()
                            else:
                                self.setMessage("Kontakt już znajduje się w książce telefonicznej")
                                self.messager()
                                subMenuEditContact(newDictionary)
                    elif parameter==3:
                        myString=intCheck()
                        newDictionary=self.process.edit_contact(newDictionary, parameter - 1, myString)

                        subMenuEditContact(newDictionary)
                    else:
                        self.setMessage("")
                        self.messager()
                        myString=input("Podaj nową wartość: ")
                        newDictionary=self.process.edit_contact(newDictionary, parameter - 1, myString)
                        subMenuEditContact(newDictionary)
                else:
                    self.setMessage("Niewłaściwy numer! Wybierz wartość 1,5 lub 0.")
                    subMenuFindEdit(newDictionary)
                #end if
            except ValueError:
                self.setMessage("Niewłaściwy znak! Wybierz wartość 1,5 lub 0.")
                subMenuFindEdit(newDictionary)

        def subMenuFindEdit(newDictionary):
            print("1. Edytuj kontakt: ")
            print("5. Usuń kontakt: ")
            print("0. Wyjdź z menu: ")

            inputParam=input("Wybierz opcję: ")
            print("\n")

            # To execute the selected option
            try:
                parameter=int(inputParam)
                if parameter==0 or parameter==5 or parameter==1:
                    if parameter==1:
                        self.setMessage("")
                        self.messager()
                        subMenuEditContact(newDictionary)
                    elif parameter==5:
                        confirm=self.toConfirm("Kontakt zostanie usunięty. ")
                        if confirm:
                            self.process.delete_contact(newDictionary)
                            self.setMessage("Kontakt został usunięty")
                            self.messager()
                            self.menuFind()
                        else:
                            self.setMessage("")
                            self.messager()
                            subMenuFindEdit(newDictionary)
                    elif parameter==0:
                        self.menuFind()
                else:
                    self.setMessage("Niewłaściwy numer! Wybierz wartość 1,5 lub 0.")
                    subMenuFindEdit(newDictionary)
                #end if
            except ValueError:
                self.setMessage("Niewłaściwy znak! Wybierz wartość 1,5 lub 0.")
                subMenuFindEdit(newDictionary)

        def subMenuFind():

            findString=input("Wpisz tekst aby wyszukać kontakt: ")
            newDictionary=self.process.find_contact_sting(findString)

            if len(newDictionary)==0:
                self.setMessage("Brak kontaktów.")
                self.messager()
                self.menuFind()
            elif len(newDictionary)==1:
                self.toPrintDictionary(newDictionary)
                subMenuFindEdit(newDictionary)

            elif len(newDictionary)>1:
                self.toPrintDictionary(newDictionary)
                self.setMessage("")
                self.messager()
                self.menuFind()

        print ("Po wyszukaniu jednego kontaktu możliwa jest jego edycja oraz jego usunięcie")
        print ("1. Wyszukaj kontakt")
        print ("0. Wróć do menu głównego")

        inputParam=input("Wybierz opcję: ")
        print("\n")

        # To execute the selected option
        try:
            parameter=int(inputParam)
            if parameter>=0 and parameter<=1:
                if parameter==1:
                    self.setMessage("")
                    self.messager()
                    subMenuFind()

                elif parameter==0:
                    self.setMessage("")
                    self.messager()
                    self.menuRoot()
            else:
                self.setMessage("Niewłaściwy numer! Wybierz wartość 0-1.")
                self.menuFind()
            #end if
        except ValueError:
            self.setMessage("Niewłaściwy znak! Wybierz wartość 0-1.")
            self.menuFind()

    def menuQuit(self):
        pass

########Main############################################################################################################
# consoleGUI=Console(Processing())




