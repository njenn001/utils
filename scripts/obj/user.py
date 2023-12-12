""" User class. """
class User:

    """

        A class representation of the user. 

        ''' 

        Attributes
        ----------
        id : int
        username : str 
        password : str 
        authority : int 

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

        """ Class variables. """
        self.id = 0
        self.username = None 
        self.password = None 
        self.authority = 0

        if (args): 
            self.id = int(args[0][0])
            self.username = args[0][1]
            self.password = args[0][2]
            self.authority = int(args[0][3])

        self.status = False
    
    """ Returns the user's id. 

    @return id : User id
    @rtype id : int
    """ 
    def get_id(self): 
        return self.id

    """ Sets the user's id.

    @param id : User id
    @type id : int
    """
    def set_id(self, id): 
        self.id = id

    """ Returns the user's username.

    @return username : User username 
    @rtype username : str 
    """ 
    def get_username(self): 
        return self.username

    """ Sets the user's username.

    @param username : User username 
    @type username : str 
    """ 
    def set_username(self, username): 
        self.username = username 

    """ Returns the user's password. 

    @return password : User password 
    @rtype password : str
    """ 
    def get_password(self): 
        return self.password 

    """ Sets the user's password. 

    @param password : User password
    @type password : str
    """ 
    def set_password(self, password): 
        self.password = password 

    """ Returns the user's authority. 

    @return authority: User authority 
    @rtype authority : int
    """ 
    def get_authority(self): 
        return self.authority 

    """ Sets the user's authority. 

    @param authority : User authority
    @type authority : int 
    """
    def set_authority(self, authority): 
        self.authority = authority 

    """ Returns the user's status. 

    @return status : User status
    @rtype status : boolean
    """
    def get_status(self): 
        return self.status 

    """ Sets the user's status. 

    @param status : User status 
    @type status : boolean
    """
    def set_status(self, status): 
        self.status = status 