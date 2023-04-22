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