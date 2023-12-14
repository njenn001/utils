""" Prebuild imports. """ 
import sqlite3
import os 

""" Class imports. """ 
from obj.user import User

""" Admin class. """ 
class Admin(User): 

    """
        A class representation of a user. 

        '''

        Attributes
        ----------
        id : int
        username : str 
        password : str 
        authority : int 
        status : boolean

        Methods 
        -------

        get/set_attributes 
            Returns or sets each individual attribute. 

    """

    """ Initializes the User. 

    @param args : List of arguments 
    @type args : list
    """
    def __init__(self, *args): 
        super().__init__(args)

    """ Injects Administrator into database. 
    
    @return status : Action status 
    @rtype status : boolean 
    """
    def inject(self):

        status = False
        
        """ Database file path. """
        path = r'D:\repos\laboratory\instance\flaskr.sqlite'

        """ DB connection & cursor. """
        connection = sqlite3.connect(path)
        cursor = connection.execute("INSERT INTO administrators VALUES (?, ?, ?, ?)", 
                                    (int(self.get_id()), 
                                    self.get_username(),
                                    self.get_password(),
                                    int(self.get_authority()) ) )
        
        """ Close connection. """
        cursor.close()
        connection.commit() 

        print('Injected\n')
        return status 

    """ Checks the database for current admin. 

    @return status : Admin status 
    @rtype status : boolean
    """ 
    def check(self): 
        """ Database file path. """
        path = r'D:\repos\laboratory\instance\flaskr.sqlite'

        """ DB connection & cursor. """
        connection = sqlite3.connect(path)
        cursor = connection.execute("SELECT * from administrators")
        
        for r in cursor:
            if self.get_id() in r: 
                self.set_status(True)
                return self.get_status()
            else:
                pass
