""" Prebuilt imports. """
import sqlite3

""" Map class. """
class Map: 

    """ 
        A class representation of a map.

        '''

        Attributes
        ----------
        id : int
        rows : list 

        Methods 
        -------

        get/set_attributes 
            Returns or sets each individual attribute. 

    """

    """ Initializes the map. 

    @param args : List of arguments 
    @type args : list
    """
    def __init__(self, *args):

        self.id = 0 
        self.rows = []

        if (args): 
            self.id = args[0]
            self.rows = args[1]

        self.status = False

    """ Returns the maps id. 

    @return id : Map id
    @rtype id : int
    """ 
    def get_id(self): 
        return self.id 

    """ Sets the maps id. 

    @param id : Map id 
    @type id : int 
    """ 
    def set_id(self, id): 
        self.id = id 

    """ Returns the maps rows

    @return rows : Map rows 
    @rtype rows : list
    """
    def get_rows(self): 
        return self.rows 

    """ Sets the maps rows 

    @param rows : Map rows 
    @type rows : list 
    """
    def set_rows(self, rows):
        self.rows = rows 

    """ Returns the maps status 
    
    @return status : Map status 
    @rtype status : boolean 
    """
    def get_status(self): 
        return self.status 

    """ Sets the maps status. 

    @param status : Map status 
    @type status : boolean
    """
    def set_status(self, status): 
        self.status = status

    """ Injects Map into database. 

    @return status : Action status 
    @rtype status : boolean 
    """ 
    def inject(self): 
        
        status = False
        
        """ Database file path. """
        path = r'D:\repos\laboratory\instance\flaskr.sqlite'

        """ DB connection & cursor. """
        connection = sqlite3.connect(path)

        i=0
        for row in self.get_rows(): 
            cursor = connection.execute("INSERT INTO maps VALUES (?, ?, ?)", 
                                        (self.get_id(), 
                                        i,
                                        row))
            i+=1

        """ Close connection. """
        cursor.close()
        connection.commit() 

        print('Injected\n')
        return status 

    """ Checks the database for the current map.
    
    @return status : Map status 
    @rtype status : boolean 
    """
    def check(self): 

        """ Database file path. """
        path = r'D:\repos\laboratory\instance\flaskr.sqlite'

        """ DB connection & cursor. """
        connection = sqlite3.connect(path)
        cursor = connection.execute("SELECT * from maps")
        
        for r in cursor:
            if self.get_id() in r: 
                self.set_status(True)
                return self.get_status()
            else:
                pass

    """ Shows the maps rows. 

    @return null    
    """
    def show(self): 
        
        """ Variables. """
        i=0

        """ Iterate through rows. """
        for row in self.get_rows(): 
            print(str(i) + " " + row)
            i+=1