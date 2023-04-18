from importlib import reload #reload a module that's been imported
from os import sys
pop_module = sys.modules.pop #remove the module and it's cache
from os.path import getsize #to rudimentally check if a generator file has changed or not and thus update the associated cog
from pathlib import Path
from os import listdir
from json import dump,load,JSONDecodeError
from time import time as ti
from modules.utils import *
kill()
from generators import general
print(type(general.votelog))
kill()

class generate():
    def __init__(self,files=[]):
        '''
        Use file if you want override what files are imported from, to generate commands, else the program will search for importable files in the generators dir.
        The name of the imported file in the generators dir will be used as the command group/cog name.
        The variable names in the generator files will be used as the command names and their string contents will be what is sent to discord when that command is called. 
        '''
        if Path('generator.json').exists():
            try:
                with open('generator_data.json','r') as f:
                    config=load(f)
                update_config=False
            except JSONDecodeError:
                #the config file is broken
                #generate a new file
                update_config=True
            except Exception as e:
                kill()
                raise e
        else:
            #create the file if doesn't exist
            update_config=True
        if update_config:
            #update the config file
            with open('generator_data.json','w') as f:
                f.write('{}')
            config={}


        
        if len(files)==0:
            files=listdir('./generators')
        else:
            #over-write generated cog if already exists
            over_write=True
            new_files=[]
            for file in files:
                if Path(f'generators/{file}').exists():
                    new_files.append(file)
                else:
                    print(f'File {file} does not exist in the generators dir')
            files=list(new_files)
            del new_files
        
        for file in files:
            if file.endswith('.py'):
                #is importable
                try:
                    config[file]
                    if config[file]['size']!=getsize(f'generators/{file}'):
                        over_write=True
                except KeyError:
                    over_write=True
                    #this is the first time the cog is being generated
                    config[file]={'time':ti(),'size':getsize(f'generators/{file}')}
                    #store the last time the cog was generated as well as the generator file's size
                if over_write:
                    try:
                        #<class 'cogs.generators.modules.utils.on_ready_msg'>
                        exec(f'import generators.{file[:-3]} as temp_mod')
                        vars_=vars(temp_mod)
                        keys_=list(vars_.keys())
                        potentials=[i for i in keys_ if i.startswith('__')!=True]
                        #values=[vars_[i] for i in cmds]
                        for pot in potentials:
                            if str(type(pot))=="<class 'modules.utils.on_ready_msg'>":
                                pass
                        del keys_,temp_mod,vars_
                        cog_name=file[:-3]
                        #now we have the cog_name, cmds and their values
                    except ImportError as e:
                        print(f'Cannot import {file} as an error occurred: {e}')
                
            else:
                print(f'Cannot import non-python files: {file}')