
import json

class OpenFromJSON():
    '''
        OpenFromJson is a class, which imports cobfiguration from JSON format.
    '''

    def __init__(self):
        pass

    def insert_config(self,**kwargs):
        '''
        :param kwargs: A dictionary containing a path to JSON file, TABLE, TABLE NAME, CSV FILE NAME and DB NAME.
        :type kwargs: dict
        Sets configuration data into a config file.
        '''

        file_to_write=kwargs['path']
        kwargs.__delitem__('path')

        # Open a file for writing
        out_file = open(file_to_write,"w")

        # Save the dictionary into this file
        # (the 'indent=4' is optional, but makes it more readable)
        json.dump(kwargs , out_file , indent=4)

        # Close the file
        out_file.close()

    def get_config(self,**kwargs):
        '''
        :param kwargs: A dictionary containing a path to JSON file.
        :type kwargs: dict
        :return: dict containing  TABLE, TABLE NAME, CSV FILE NAME and DB NAME.
        Gets the config data from the config file.
        '''
        # Open the file for reading
        path = kwargs['path']
        kwargs.__delitem__('path')
        in_file = open(path,"r")

        # Load the contents from the file, which creates a new dictionary
        kwargs = json.load(in_file)
        # kwargs['juz']='juz'

        # Close the file... we don't need it anymore
        in_file.close()
        return kwargs
