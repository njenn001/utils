""" Prebuilt imports. """
import sqlite3 
import csv 

""" Class imports. """
from obj.admin import Admin

""" Data files """
admin_file = 'admin.csv'
users_file = 'users.csv'
maps_file = 'maps.csv'

""" Loads maps from file. 

@param file : Maps file 
@type file : File

"""
def load_maps(file): 

    """ New reader object. """ 
    reader = csv.reader(file, delimiter=' ')
    
    i=0
    """ Print the rows. """
    for row in reader: 
        
        """ Skip first row """
        if i > 0: 
            print(row[2])
            
        i+=1  

""" Loads admin from file.

@param file : Admin file
@type file : File 
""" 
def load_admin(file): 

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
                load_admin(file)
            elif f == 'maps.csv': 
                load_maps(file)

""" The main sequence. 

@return null
"""
def main():
    
    """ Populate filenames. """
    files = [admin_file, users_file, maps_file]

    load_data(files)

""" Waits for the program to be called. 

@return null
"""
if __name__ == '__main__':
    main()