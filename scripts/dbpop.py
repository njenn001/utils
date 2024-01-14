""" Prebuilt imports. """
import sqlite3 
import csv 

""" Class imports. """
from obj.admin import Admin
from obj.user import User 
from obj.map import Map
from obj.item import Item 
from obj.sprite import Sprite 

""" Data files """
admin_file = './files/admin.csv'
users_file = './files/users.csv'
maps_file = './files/maps.csv'
items_file = './files/items.csv'
sprites_file = './files/sprites.csv'

""" Loads sprites from files. 

@param file : Items file 
@type file : File 
""" 
def load_sprites(file): 
    
    """ New reader object. """ 
    reader = csv.reader(file, delimiter=' ')
    
    i=0
    """ Print the rows. """
    for row in reader: 
        
        """ Skip first row """
        if i > 0: 
                        
            """ New item injection. """
            sprite = Sprite(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            
            if (not sprite.check()):
                #print(sprite.get_status())
                sprite.inject()
            else: 
                print('Sprite ' + sprite.get_kind() + ' exists')
        
        """ Increment. """ 
        i+=1

""" Loads items from file. 

@param file : Items file
@type file : File 
"""
def load_items(file): 
    
    """ New reader object. """ 
    reader = csv.reader(file, delimiter=' ')
    
    i=0
    """ Print the rows. """
    for row in reader: 
        
        """ Skip first row """
        if i > 0: 
            
            """ New item injection. """
            item = Item([row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]])
            
            if (not item.check()):
                #print(item.get_status())
                item.inject()
            else: 
                print('Item ' + item.get_kind() + ' exists')
        
        """ Increment. """ 
        i+=1

""" Loads maps from file. 

@param file : Maps file 
@type file : File

"""
def load_maps(file): 

    """ New reader object. """ 
    reader = csv.reader(file, delimiter=' ')
    
    """ Variables. """
    i=0
    id = 0 
    temp_rows = [] 

    """ Print the rows. """
    for row in reader: 
        
        """ Skip first row """
        if i > 0: 
            """ Check row id. """ 
            if (id == int(row[0])): 

                """ Loop event. """
                temp_rows.append(row[2])

            elif (id != int(row[0])):

                """ New map injection. """
                map = Map(id, temp_rows)

                if (not map.check()):
                    #print(map.get_status())
                    map.inject()
                else: 
                    print('Map ' + str(map.get_id()) + ' exists')

                """ Loop event. """
                id+=1 
                temp_rows = []  
                temp_rows.append(row[2]) 

        """ Increment. """       
        i+=1    

    """ New map injection. """
    map = Map(id, temp_rows)

    if (not map.check()):
        #print(map.get_status())
        map.inject()
    else: 
        print('Map ' + str(map.get_id()) + ' exists')

""" Loads users from file.

@param file : User file
@type file : File 
""" 
def load_users(file): 

    """ New reader object. """ 
    reader = csv.reader(file, delimiter=' ')
    
    i=0
    """ Print the rows. """
    for row in reader: 
        
        """ Skip first row """
        if i > 0: 

            """ New admin injection. """
            user = User([row[0], row[1], row[2], row[3]])
            
            if (not user.check()):
                #print(admin.get_status())
                user.inject()
            else: 
                print('User ' + user.get_username() + ' exists')
        
        """ Increment. """ 
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

            """ New admin injection. """
            admin = Admin(row[0], row[1], row[2], row[3])
            
            if (not admin.check()):
                #print(admin.get_status())
                admin.inject()
            else: 
                print('Admin ' + admin.get_username() + ' exists')
        
        """ Increment. """ 
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
            if 'admin.csv' in f:
                load_admin(file)
            elif 'users.csv' in f: 
                load_users(file)
            elif 'maps.csv' in f: 
                load_maps(file)
            elif 'items.csv' in f: 
                load_items(file)
            elif 'sprites.csv' in f:
                load_sprites(file)

""" The main sequence. 

@return null
"""
def main():
    
    """ Populate filenames. """
    files = [admin_file, users_file, maps_file, items_file, sprites_file]

    """ Load data from files. """
    load_data(files)

""" Waits for the program to be called. 

@return null
"""
if __name__ == '__main__':
    main()