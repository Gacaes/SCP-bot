def kill(msg=""):
    raise Exception(f'Program killed{": "+str(msg) if msg!="" else ""}')

def msg_short(msg):
    sent=''
    array=[]
    while len(msg):
        index=msg.find('.')
        if len(sent)+index+2<2000:
            sent+=msg[:index+1]
            msg=msg[index+1:]
        else:
            array.append(str(sent))
            sent=''
    array.append(str(sent))
    return array

class on_ready_msg():
    def __init__(self,msg='<cog> Cog Loaded'):
        """Set a custom message to print to the terminal when the cog is imported

        Args:
            msg (string): The message to be printed to terminal
        """
        self.msg=msg

class command():
    def __init__(self,msg,aliases=[]):
        """Set a custom message to print to the terminal when the cog is imported

        Args:
            msg (string): The basic message to be print to discord when the command is run
            aliases (list (string)): A list of string aliases to use for the command
        """
        self.aliases=aliases
        self.msg=msg_short(msg)