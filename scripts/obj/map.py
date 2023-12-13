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
            self.id = args[0][0]
            self.rows = args[0][1]


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

    """ Injects Map into database. 

    @return status : Action status 
    @rtype status : boolean 
    """ 
    def inject(self): 
        print()

