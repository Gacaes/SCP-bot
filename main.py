import discord
from discord.ext import commands, tasks
from random import choice
from keep_alive import keep_alive
from os import listdir, system, environ, system
from threading import Thread
from time import sleep
from sys import exit as exi
from pathlib import Path

#system('clear') #clear the terminal from previous errors

cog_override=['generate_cogs']

running = True
if Path('online_toggle.py').exists():
    from online_toggle import online_toggle
else:
    online_toggle=False
    with open('online_toggle.py','w') as f:
        f.write('online_toggle=False')

def loop():
    #check ln297    
    global running
    while running:
        inp = input('thread> ')
        if inp == 'kill':
            running = False
            print('Bot Exiting')
            break
        try:
            exec(inp)
        except Exception as e:
            print('exec exception:', e)
        try:
            print('eval =', eval(inp))
        except Exception as e:
            print('eval exception:', e)


def run_check():
    #check ln297
    thread = Thread(target=loop)
    thread.daemon = True
    thread.start()
    while True:
        sleep(1)
        if not running:
            #thread.close()
            #kill_()
            exi()


def is_dev(ctx):
    async def predicate(ctx):
        return str(ctx.author) in [
            'archibald4#2956', 'Femboy Lukas#0287', 'serena.steal#7127'
        ]
    return commands.check(predicate)


####    **DO NOT DELETE THIS OR EVERYTHING WILL BREAK**    ####
client = commands.Bot(command_prefix='.',
                      description='Femboy Lukas\' SCP bot',
                      case_insensitive=True)
bot = client
#you can change the description string to whatever you want it to be


'''DONT FUCKING DELETE THIS'''
@client.event
async def on_message(message):
    if message.author == client.user:
        return None
    ctx = await client.get_context(message)
    await client.invoke(ctx)


'''DONT FUCKING DELETE THIS'''


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(
        name='Being a good boy | .help'))
    #await client.get_channel(811975440927293482).send('I am <@983701898580336640>: I let my daddies <@602331305161654278> and <@425748749462274048> use my commands\n(I am also online)\nI also might need my mommy fox\'s help <@120816817055727616> :)')
    if online_toggle:
        #await client.get_channel(811975440927293482).send('Predictive algorithm ready for use')
        
        #changes the name of the game that the bot is supposedly playing
        embed = discord.Embed(title=f'{client.user.name} Is Now Online', color=discord.Color.from_rgb(0, 255, 0))
        #embed.set_footer(text=client.footer)
        #embed.set_author(name='A good boy')  #,icon_url=client.footer_image)
        await client.get_channel(811975440927293482).send(embed=embed)
        #this makes an embed and can send it to a specific channel that the bot is in
        

    print('Bot Ready.')


@client.event
async def on_command_error(ctx, error):
    'this replies to the user that sent the command to tell them that an error occurred'
    if isinstance(error, commands.CommandNotFound):
        #this is a command that the user tried to execute, but doesn't exist
        #pass
        if not ctx.message.content[:2]=='..':
            await ctx.send(f'Hey <@{ctx.author.id}>, it seems like you have entered a command that doesnt exist. Do .help for a list of commands')
            
            await ctx.message.add_reaction('❓')
        print(f'Hey <@{ctx.author.id}> ({ctx.author}) entered an invalid command: \'{ctx.message.content}\'')
    elif isinstance(error, commands.MissingRequiredArgument):
        #this is a command that needs an arguement which the user failed to provide
        #pass
        await ctx.send(
            f'Hey <@{ctx.author.id}>, it seems like youre missing some valuble information at the end of the command you just tried to execute.'
        )
        await ctx.message.add_reaction('⁉️')
        print(
            f'Hey <@{ctx.author.id}> ({ctx.author}), it seems like youre missing some valuble information at the end of the command you just tried to execute.'
        )
    else:
        #this is an unknown error
        print(f'main ln117: {error} by <@{ctx.author.id}> ({ctx.author})')
        await ctx.send(f'main ln126 error: {error}')
        await ctx.message.add_reaction('‼️')


@client.command(
    help=
    'Toggles whether to display the online message when bot comes online (Requires bot admin)',
    aliases=['online'])
@commands.check(is_dev)
async def toggle_online(ctx):
    global online_toggle
    online_toggle = not online_toggle
    with open('online_toggle.py','w') as f:
        f.write(f'online_toggle={online_toggle}')
    await ctx.send(f'Toggled the the bot\'s online message to {online_toggle}')


@client.command(help='(Bot Admin Required)')
@commands.check(is_dev)
async def module(ctx, name, command, args=None):
    print(name, command)
    try:
        exec('from ' + name + ' import ' + command)
        if args == None:
            try:
                await ctx.send(eval(command))
            except:
                await ctx.send(exec(command + '()'))
        else:
            await ctx.send('Calling module.command(args) is a WIP')
    except ImportError:
        print('Cannot Import Module: ' + name + ', Command: ' + command)
        await ctx.send('Cannot Import Module: ' + name + ', Command: ' +
                       command)
    except Exception as ex:
        print(ex)
        await ctx.send('main.module Generic Error Caught: ' + str(ex))
        raise Exception(ex)
    #await ctx.message.add_reaction('✅')


@client.command(help='Loads A Cog (Bot Admin Required)')
@commands.check(is_dev)
async def load(ctx, extension):
    try:
        if extension in cog_override:
            raise Exception(f'File {extension} in cog_override, not attempting to import')
        client.load_extension(f'cogs.{extension}')
        await ctx.send(f'{extension} Loaded.')
        #await ctx.message.add_reaction('✅')
    except commands.ExtensionAlreadyLoaded:
        await ctx.send(f'{extension} has already been loaded.')
        #await ctx.message.add_reaction('✅')
    except Exception as ex:
        print(f'main.load error: {ex}')
        await ctx.send(f'main.load error: {ex}')
        #await ctx.message.add_reaction('‼️')


@client.command(help='Unloads A Cog (Bot Admin Required)')
@commands.check(is_dev)
async def unload(ctx, extension):
    try:
        client.unload_extension(f'cogs.{extension}')
        await ctx.send(f'{extension} Unloaded.')
        #await ctx.message.add_reaction('✅')
    except commands.ExtensionNotLoaded:
        await ctx.send(f'{extension} already unloaded.')
        #await ctx.message.add_reaction('✅')
    except Exception as ex:
        print(f'main.unload error: {ex}')
        await ctx.send(f'main.unload error: {ex}')
        #await ctx.message.add_reaction('‼️')


@client.command(help='Reloads A Cog (Bot Admin Required)')
@commands.check(is_dev)
async def reload(ctx, extension):
    checking1 = [extension]
    if extension == 'all':
        checking1 = list(checking0)
    for i in checking1:
        try:
            client.unload_extension(f'cogs.{i}')
            client.load_extension(f'cogs.{i}')
            await ctx.send(f'{i} Reloaded.')
            #await ctx.message.add_reaction('✅')
        except commands.ExtensionNotLoaded as ex:
            await ctx.send(f'{i} already unloaded: {ex}')
            #await ctx.message.add_reaction('‼️')
        except commands.ExtensionFailed as ex:
            await ctx.send(f'{i} failed to load: {ex}')
            #await ctx.message.add_reaction('‼️')
        except Exception as ex:
            print(f'main.reload error: {ex}')
            await ctx.send(f'main.reload error: {ex}')
            #await ctx.message.add_reaction('‼️')


checking0 = []
for filename in listdir('./cogs'):  # all files in cogs dir
    if filename.endswith('.py'):  # all .py files in cogs
        try:
            filename = filename[:-3]
            if filename in cog_override:
                raise Exception(f'File {filename} in cog_override, not attempting to import')
            client.load_extension(f'cogs.{filename}')  # load the cog
            print(f'cogs/{filename} Loaded.')
            checking0.append(filename)
        except commands.ExtensionFailed as ex:
            print(f'Failed To Load {filename}: {ex}')
        except ImportError:
            pass  #print(f'cogs.{filename} has no shop')
        except Exception as ex:
            print(f'main cog loading error: {ex}')


@client.event
async def on_command(ctx):
    print(f"Handling command {ctx.command.qualified_name} for {ctx.author} in {ctx.guild.name}")
    #this is executed everytime any command is executed successfully i.e. you can give users xp or track how many commands they've used
    #if db.is_updating:
    #    await ctx.message.send(
    #        'The SCP-Bot database is updating so data may not be fully accurate.'
    #    )
    #await ctx.message.add_reaction('⏳')
    #data_handler.add_data_value(ctx.author.id,'commands',1)
    #data_handler.add_data_value(ctx.author.id,'xp',1)


@client.command()
async def ping(ctx):
    await ctx.send(f"Pong {int(client.latency*1000)}")


@client.command(help='Terminates the bot and the webserver keeping it alive (Bot Admin Required)',aliases=['die','fuckoff'])
@commands.check(is_dev)
async def kill(ctx):
    global running,keep_alive
    running = False
    embed = discord.Embed(
        title=f'{client.user.name} Is Shutting Down For Maintenance',
        color=discord.Color.from_rgb(255, 0, 0))
    embed.set_author(name='A good boy')
    await client.get_channel(811975440927293482).send(embed=embed)
    #this makes an embed and can send it to a specific channel that the bot is in
    keep_alive.kill() #stop the webserver
    sleep(2)
    await bot.close() # Don't use exit() when you can use the proper shutdown function

@client.command()
async def fuckon(ctx):
    await ctx.send(f'<@{ctx.author.id}> <a:SmugBrow:835590843171471442>')

async def kill_():
    embed = discord.Embed(
        title=f'{client.user.name} Is Shutting Down For Maintenance',
        color=discord.Color.from_rgb(255, 0, 0))
    embed.set_author(name='A good boy')
    await client.get_channel(811975440927293482).send(embed=embed)
    #this makes an embed and can send it to a specific channel that the bot is in


class MyHelpCommand(commands.MinimalHelpCommand):
    async def send_pages(self):
        destination = self.get_destination()
        e = discord.Embed(color=discord.Color.blurple(), description='')
        for page in self.paginator.pages:
            e.description += page
        await destination.send(embed=e)

debugging=False
if __name__=="__main__":
    if not debugging:
        client.help_command = MyHelpCommand()
        
        runner = Thread(target=run_check)
        runner.daemon = True
        #runner.start()
        #this starts a sub thread to have access to the console while the main file is running
        
        try:
            client.run(environ['client_key'])
            from keep_alive import keep_alive
            #I made it into an object which has a method called kill
            #to stop the bot, run keep_alive.kill() to stop the webserver before this main process
        except discord.errors.HTTPException:
            print('\nDiscord has rate-limited and therefore temp-banned the bot')
    else:
        import cogs.generate_cogs as gc

