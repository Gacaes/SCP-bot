def kill(msg=""):
    raise Exception(f'Program killed{": "+str(msg) if msg!="" else ""}')

class on_ready_msg():
    def __init__(self,msg='<cog> Cog Loaded'):
        """Set a custom message to print to the terminal when the cog is imported

        Args:
            msg (string): The message to be printed to terminal
        """
        self.msg=msg

class command():
    def __init__(self,msg,aliases=[]):
        self.aliases=aliases
        self.msg=msg