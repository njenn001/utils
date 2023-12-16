""" Prebuilt imports. """ 
import sqlite3

""" Class imports. """ 
from obj.item import Item 

""" Sprite class. """
class Sprite(Item): 

    def __init__(self, *args): 
        
        super().__init__() 

        if (args): 
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
        cursor = connection.execute("INSERT INTO sprites VALUES (?, ?, ?, ?, ?, ?, ?, ?)", 
                                    (int(self.get_id()), 
                                    self.get_kind(),
                                    int(self.get_health()),
                                    int(self.get_hunger()),
                                    int(self.get_thirst()),
                                    int(self.get_excitement()),
                                    int(self.get_strength()),
                                    self.get_symbol() ))
        
        """ Close connection. """
        cursor.close()
        connection.commit() 

        #print('Injected\n')
        return status 

    """ Checks the database for current sprite. 

    @return status : Sprite status 
    @rtype status : boolean
    """ 
    def check(self): 
        """ Database file path. """
        path = r'D:\repos\laboratory\instance\flaskr.sqlite'

        """ DB connection & cursor. """
        connection = sqlite3.connect(path)
        cursor = connection.execute("SELECT * from sprites")
        
        for r in cursor:
            if self.get_kind() in r: 
                self.set_status(True)
                return self.get_status()
            else:
                pass 
