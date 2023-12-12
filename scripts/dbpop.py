""" Prebuilt imports. """
import sqlite3 
import csv 

""" Class imports. """
from obj.admin import Admin

""" Data files """
admin_file = 'admin.csv'

""" Load data from files. 

@param files : List of filenames
@type files : List
"""
def load_data(files): 

    """ Open and read the files. """ 
    for f in files: 

        """ Open file. """
        with open(f, newline='') as file:

            """ Check name. """
            if f == 'admin.csv':

                """ New reader object. """ 
                reader = csv.reader(file, delimiter=' ')
                
                i=0
                """ Print the rows. """
                for row in reader: 
                    
                    """ Skip first row """
                    if i > 0: 
                        admin = Admin(row[0], row[1], row[2], row[3])
                        if (not admin.check()):
                            print(admin.get_status())
                            admin.inject()
                        else: 
                            print('Admin ' +admin.get_username() + ' exists')
                    i+=1

""" The main sequence. 

@return null
"""
def main():
    
    """ Populate filenames. """
    files = [admin_file]

    load_data(files)

""" Waits for the program to be called. 

@return null
"""
if __name__ == '__main__':
    main()