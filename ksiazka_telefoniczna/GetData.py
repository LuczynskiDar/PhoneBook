# -*- coding: utf-8 -*-

from ksiazka_telefoniczna.OpenFromFile import OpenFromFile
from ksiazka_telefoniczna.OpenFromSQLite import OpenFromSQLite
from ksiazka_telefoniczna.OpenFromJSON import OpenFromJSON


class GetData(OpenFromSQLite,OpenFromFile,OpenFromJSON):
    '''
        GetData is a virtual class, which inherits from OpenFromFile, OpenFromSQLite
        and OpenFromJSON. Purpose of the class is supply one interface for class Processing,
        to listed above classes.
    '''
    def __init__(self):
        pass
