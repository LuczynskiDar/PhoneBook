# Phone Book (ksiazka_telefoniczna)

> The phone book, Książka Telefoniczna, is a qualification project, from high-level programming languages course,
at AGH University of Science and Technology.

## Description

Phone book from the polish context menu, picks up new data and keeps it in local data base, run on SQL lite. A user can search for the contacts, switch the data base or import/export data from the csv file. The phone book contains such data as: Name, Surname, Telephone, Street, Flat/House Number, Postal Code and Email.

### Desig approach

- Setup Python project using [PyScaffold  2.5.3.](https://pyscaffold.org).
- Use Console GUI to do I/O.
- Use SQL lite to save data.
- Use CSV as an option to save data.
- Write/Read configuration from JSON file.
- Create docs.
- Unit tests are not required.

#### Modules

- [HTML docummentation available after download](https://github.com/LuczynskiDar/PhoneBook/tree/master/docs/html)

![PhoneBook modules](https://github.com/LuczynskiDar/PhoneBook/blob/master/Img/PhoneBook_modules.PNG)

- [Console](https://github.com/LuczynskiDar/PhoneBook/blob/master/ksiazka_telefoniczna/Console.py)

Console GUI, root menu :

``` console gui
1. Dodaj nowy kontakt (Add new contact)
2. Zarządzaj bazą danych (Manage contact database)
3. Zapisz lub pobierz książkę telefoniczną z pliku (Save or open Phone Book from file)
4. Znajdź kontakt (Find contact)
0. Wyjdź z programu (Exit)
```

- [Processing](https://github.com/LuczynskiDar/PhoneBook/blob/master/ksiazka_telefoniczna/Processing.py)
- [GetData](https://github.com/LuczynskiDar/PhoneBook/blob/master/ksiazka_telefoniczna/GetData.py)
- [OpenFromFile](https://github.com/LuczynskiDar/PhoneBook/blob/master/ksiazka_telefoniczna/OpenFromFile.py)
- [OpenFromSQLite](https://github.com/LuczynskiDar/PhoneBook/blob/master/ksiazka_telefoniczna/OpenFromSQLite.py)
- [TelephoneBook](https://github.com/LuczynskiDar/PhoneBook/blob/master/ksiazka_telefoniczna/TelephoneBook.py)
- [Person](https://github.com/LuczynskiDar/PhoneBook/blob/master/ksiazka_telefoniczna/Person.py)

#### Relation betweenthe modules

- **UML Diagram**

![UML diagram](https://github.com/LuczynskiDar/PhoneBook/blob/master/Img/Uml.png)