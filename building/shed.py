from building import Building


class Shed(Building):
    """
    *This is a DocString*
    Author: Steve Brownlee
    Arguments:
        Building{[type]} -- [description]
    Purpose: 
    To represent any kind of shed for users to build in the UI        
    """
    def __init__(self):
        """
        Initialize method for shed
        Arguments:
            windows {windows} -- Integer for number of windows on the shed
        """
        super().__init__()
        self.workbench = True
        self.tools = []