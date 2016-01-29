
import json
import os,sys

class OpenFromJSON():
    '''

        OpenFromJson is a class, which imports cobfiguration from JSON format.

    '''

    def __init__(self):
        pass

    def insert_config(self,**kwargs):

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





# o=OpenFromJSON()
#
# kwargs={'a':'a',1:1,555:555,"sasd":"sasd"}
# path = os.path.dirname(os.path.realpath(__file__))+ os.path.sep + 'cfg' + os.path.sep + 'test.json'
# print(path)
# o.insert_config(path = path , a = 'a' , b = 15)
# o.get_config(path = path)
