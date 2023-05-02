from traceback import extract_stack as ex
from re import compile

def traceback_var(var,stack):
    filename, lineno, function_name, code = stack[-2]
    vars_name = compile(r'\((.*?)\).*$').search(code).groups()[0]
    return vars_name


init_cogs=[]

def kill(msg=""):
    raise Exception(f'Program killed{": "+str(msg) if msg!="" else ""}')

#fellas in paris
def msg_short(msg):
    sent=''
    array=[]
    while len(msg):
        index=msg.find('.')
        if index==-1:
            #if a dot doesnt exist
            if len(sent)+len(msg)<2000:
                #oops I forgot to add the result to the array to be returned
                array.append(str(sent+msg))
            elif len(msg)>1999:
                #cba to fix this but shouldnt run into this issue yet
                #this means that the message is 2000 chars or long and doesnt
                #have a fullstop in it which is really unlikely
                pass
            else:
                #if both sent and msg are under 2000 but together are 2000+
                array.append(str(sent))
                array.append(str(msg))

            msg=''
            sent=''
        else:
            #if a dot does exist
            if len(sent)+index+2<2000:
                sent+=str(msg[:index+1])
                msg=str(msg[index+1:])
            else:
                array.append(str(sent))
                sent=''
    if sent!='':
        array.append(sent)
    return array

class on_ready_msg():
    msgs={}
    def __init__(self,msg):
        """Set a custom message to print to the terminal when the cog is imported

        Args:
            msg (string): The message to be printed to terminal
        """
        self.msg=msg
        try:
            on_ready_msg.msgs[ex()[-2][0]].append(self)
        except KeyError:
            on_ready_msg.msgs[ex()[-2][0]]=[self]

class command():
    cmds={}
    
    def __init__(self,msg,aliases=[]):
        """Set a custom message to print to the terminal when the cog is imported

        Args:
            msg (string): The basic message to be print to discord when the command is run
            aliases (list (string)): A list of string aliases to use for the command
        """
        self.aliases=aliases
        self.msg=msg_short(msg)
        #[print(_) for _ in ex()]
        stack=ex()[-2]
        self.var_name=stack[3][:stack[3].find('=')]
        try:
            command.cmds[stack[0]].append(self)
        except KeyError:
            command.cmds[stack[0]]=[self]
            
def create_cog():
    global init_cogs
    temp=ex()[-2][0]
    if temp not in init_cogs:
        init_cogs.append(temp)
        on_ready_msg.msgs[temp]=[]
        command.cmds[temp]=[]
    del temp

#From the keep_alive.py

#from threading import Thread

#new method
def wsgi():
    from wsgiref.simple_server import make_server, demo_app
    
    with make_server('', 8000, demo_app) as httpd:
        print("Serving HTTP on port 8000...")
    
        # Respond to requests until process is killed
        httpd.serve_forever()


class keep_alive_():
    def __init__(self,method='new'):
        '''
        Method can either be 'new' or 'old'.
        '''
        from multiprocessing import Process
        #proc = Process(target=your_proc_function, args=())
        #proc.start()
        # Terminate the process
        #proc.terminate()  # sends a SIGTERM
        
        if method=='new':
            
            self.p = Process(target=wsgi)
            self.p.start()
            
        elif method=='old':
            #old method
            from flask import Flask
            
            app = Flask('')
            @app.route('/')
            
            def home():
                return "Hello. I am a penis-lover"
            
            def run():
              app.run(host='0.0.0.0',port=8080)
            
            self.p = Process(target=run)
            self.p.start()

    def kill(self):
        self.p.terminate()
        #stops the webserver so we dont get any weird bugs like it restarts itself or turn itself back on again

#keep_alive=keep_alive_()