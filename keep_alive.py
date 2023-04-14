from threading import Thread

from multiprocessing import Process
#proc = Process(target=your_proc_function, args=())
#proc.start()
# Terminate the process
#proc.terminate()  # sends a SIGTERM

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

keep_alive=keep_alive_()