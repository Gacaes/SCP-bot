from importlib import reload #reload a module that's been imported
from os import sys
pop_module = sys.modules.pop #remove the module and it's cache
from os.path import getsize #to rudimentally check if a generator file has changed or not and thus update the associated cog
from pathlib import Path
from os import listdir
from json import dump,load,JSONDecodeError
from time import time as ti
from modules.utils import *
#from generators import general

class generate():
    def __init__(self,files=[]):
        '''
        Use file if you want override what files are imported from, to generate commands, else the program will search for importable files in the generators dir.
        The name of the imported file in the generators dir will be used as the command group/cog name.
        The variable names in the generator files will be used as the command names and their string contents will be what is sent to discord when that command is called. 
        '''
        if Path('cogs/generator.json').exists():
            try:
                with open('cogs/generator_data.json','r') as f:
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
            with open('cogs/generator_data.json','w') as f:
                f.write('{}')
            config={}


        
        if len(files)==0:
            files=listdir('cogs/generators')
        else:
            #over-write generated cog if already exists
            over_write=True
            new_files=[]
            for file in files:
                if Path(f'cogs/generators/{file}').exists():
                    print(f'Over-writing cogs/generators/{file}')
                    new_files.append(file)
                else:
                    print(f'File cogs/generators/{file} does not exist')
            files=list(new_files)
            del new_files
        
        for file in files:
            if file.endswith('.py'):
                #is importable
                try:
                    config[file]
                    if config[file]['size']!=getsize(f'cogs/generators/{file}'):
                        over_write=True
                except KeyError:
                    over_write=True
                    #this is the first time the cog is being generated
                    config[file]={'time':ti(),'size':getsize(f'cogs/generators/{file}')}
                    #store the last time the cog was generated as well as the generator file's size
                if over_write:
                    try:
                        #<class 'cogs.generators.modules.utils.on_ready_msg'>
                        #print('importing')
                        exec(f'import cogs.generators.{file[:-3]} as temp_mod')
                        #print('imported')
                        '''
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
                        #redundant code ^
                        '''
                        for path_ in init_cogs:
                            #print(path_)
                            if file==path_[-1*len(file):]:
                                #the create_cog has been called in this file
                                with open("cogs/"+file,'w') as f:
                                    #create the cog
                                    f.write(f'import discord\nfrom discord.ext import commands\n\nclass {file[:-3]}(commands.Cog):\n    def __init__(self,client):\n        self.client=client')
                                    #then make the on_ready function
                                    f.write(f'''
    @commands.Cog.listener()
    async def on_ready(self):
        print(\'{file[:-3]+" Cog Ready" if not len(on_ready_msg.msgs[path_]) else on_ready_msg.msgs[path_][0].msg}\')
''')
                                    #print(command.cmds[path_])
                                    #then generate the commands
                                    for cmd in command.cmds[path_]:
                                        f.write(f'''
    @commands.command(aliases={cmd.aliases})
    async def {cmd.var_name}(self,ctx):''')
                                        #print('ln107',len(cmd.msg))
                                        if not len(cmd.msg):
                                            f.write(f'\n    #This might be a bug/error or intentional\n        pass')
                                        for message in cmd.msg:
                                            f.write(fr'''
        await ctx.channel.send("""{message}""")''')
                                        #cmd.aliases : list
                                        #cmd.msg : list
                                    #make the setup
                                    f.write(f'\ndef setup(client):\n    client.add_cog({file[:-3]}(client))')
                        #pop_module(temp_mod)
                    except ImportError as e:
                        print(f'ln103 Cannot import {file} as an error occurred: {e}')
                
            else:
                print(f'Cannot import non-python files: {file}')