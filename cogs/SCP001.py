import discord
from discord import Embed
from discord.ext import commands

class SCP001(commands.Cog):
    def __init__(self,client):
        self.client=client
    @commands.Cog.listener()
    async def on_ready(self):
        print('SCP-001 Cog Ready')

    #remove the aliases arguement if you dont want any aliases.
    #example of an alias is in SCPs.py, command 'randomSC'P has an alias 'rand'
    @commands.command(aliases=['example_alias'])
    async def randomSCP001(self,ctx):
        #example command
        await ctx.channel.send('message')


#sexy

def setup(client):
    client.add_cog(SCP001(client))