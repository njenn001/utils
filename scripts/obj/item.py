""" Prebuilt imports. """ 
import sqlite3

""" Item class. """
class Item(): 

    """ 

        A class representation of an item. 

        '''

        Attributes 
        ----------
        id : int 
        kind : str 
        health : int 
        hunger : int
        thirst : int 
        excitement : int 
        strength : int 
        symbol : str 

        Methods 
        -------
        
        get/set_attributes 
            Returns or sets each individual attribute. 

    """

    """ Initializes the Item. 

    @param args : List of arguments 
    @type args : list
    """
    def __init__(self, *args): 

        self.id = 0 
        self.kind = ''
        self.health = 0 
        self.hunger = 0 
        self.thirst = 0 
        self.excitement = 0 
        self.strength = 0 
        self.symbol = ''

        if (args): 
            self.id = args[0] 
            self.kind = args[1]
            self.health = args[2]
            self.hunger = args[3]
            self.thirst = args[4]
            self.excitement = args[5]
            self.strength = args[6]
            self.symbol = args[7]

        self.status = False 

    """ Return the items id. 

    @return id : Item id
    @rtype id : int
    """ 
    def get_id(self): 
        return self.id

    """ Sets the items id. 

    @param id : Item id 
    @type id : int 
    """ 
    def set_id(self, id): 
        self.id = id 

    """ Returns the items kind. 

    @return kind : Item kind 
    @rtype kind : str
    """ 
    def get_kind(self): 
        return self.kind 

    """ Sets the items kind. 

    @param kind : Item kind 
    @type kind : str 
    """ 
    def set_kind(self, kind): 
        self.kind = kind 

    """ Returns the items health benefit. 

    @return health : Item health benefit 
    @rtype health : int 
    """ 
    def get_health(self): 
        return self.health

    """ Sets the items health benefit. 

    @param health : Item health benefit 
    @type health : int 
    """ 
    def set_health(self, health): 
        self.health = health 

    """ Returns the items hunger benefit. 

    @return hunger : Item hunger benefit 
    @rtype hunger : int 
    """ 
    def get_hunger(self): 
        return self.hunger 

    """ Sets the items hunger benefit. 

    @param hunger : Item hunger benefit 
    @type hunger : int 
    """
    def set_hunger(self, hunger): 
        self.hunger = hunger

    """ Returns the items thirst benefit. 

    @return thirst : Item thirst benefit 
    @rtype thirst : int 
    """ 
    def get_thirst(self): 
        return self.thirst
    
    """ Sets the items thirst benefit.

    @param thirst : Item thirst benefit 
    @type thirst : int 
    """ 
    def set_thirst(self, thirst): 
        self.thirst = thirst 

    """ Returns the items exitement benefit. 

    @return excitement : Item excitement benefit 
    @rtype excitement : int 
    """ 
    def get_excitement(self): 
        return self.excitement 

    """ Sets the items excitement benefit. 

    @param excitement : Item excitement benefit 
    @type excitement : int 
    """ 
    def set_excitement(self, excitement): 
        self.excitement = excitement 

    """ Returns the items strength benefit. 

    @return strength : Item strength benefit 
    @rtype strength : int 
    """ 
    def get_strength(self): 
        return self.strength
    
    """ Sets the items strength benefit. 

    @param strength : Item strength benefit 
    @type strength : int
    """
    def set_strength(self, strength): 
        self.strength = strength 

    """ Returns the items symbol. 

    @return symbol : Item symbol 
    @rtype symbol : str 
    """ 
    def get_symbol(self): 
        return self.symbol

    """ Sets the items symbol. 

    @param symbol : Item symbol
    @type symbol : str 
    """ 
    def set_symbol(self, symbol): 
        self.symbol = symbol

    """ Returns the items status. 

    @return status : Item status 
    @rtype status : boolean 
    """ 
    def get_status(self): 
        return self.status

    """ Sets the items status. 

    @param status : Item status 
    @type status : boolean
    """ 
    def set_status(self, status):
        self.status = status 

    """ Inject Item into database. 

    @return status : Action status 
    @rtype status : boolean 
    """ 
    def inject(self): 
        
        status = False
        
        """ Database file path. """
        path = r'D:\repos\laboratory\instance\flaskr.sqlite'

        """ DB connection & cursor. """
        connection = sqlite3.connect(path)
        cursor = connection.execute("INSERT INTO items VALUES (?, ?, ?, ?, ?, ?, ?, ?)", 
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
        cursor = connection.execute("SELECT * from items")
        
        for r in cursor:
            if int(self.get_id()) in r: 
                self.set_status(True)
                return self.get_status()
            else:
                pass