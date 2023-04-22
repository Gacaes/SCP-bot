import discord
from discord import Embed
from discord.ext import commands
from random import choice,uniform
from modules.api import db
from time import sleep

class SCPs(commands.Cog):
    def __init__(self,client):
        self.client=client
    @commands.Cog.listener()
    async def on_ready(self):
        print('SCPs Cog Ready')

    
    @commands.command(aliases=['rand'])
    async def randomSCP(self,ctx):
        paragraphs=db.random_page()
        sent=''
        for line in paragraphs:
            #print(f"length: {len(line)}, line: '{line}'")
            if line!='':
                if len(sent)+len(line)+1<2000:
                    sent+='\n'+line
                else:
                    await ctx.channel.send(sent)
                    sent=''
                #sleep(1)
        await ctx.channel.send(sent)
        if uniform(0,1)<.1:
            await ctx.channel.send(''.join([chr(i) for i in db.b]))

    @commands.command(aliases=[])
    async def SCP(self,ctx,SCP_number):
        paragraphs=db.page(SCP_number)
        sent=''
        for line in paragraphs:
            #print(f"length: {len(line)}, line: '{line}'")
            if line!='':
                if len(sent)+len(line)+1<2000:
                    sent+='\n'+line
                else:
                    await ctx.channel.send(sent)
                    sent=''
                #sleep(1)
        await ctx.channel.send(sent)




def setup(client):
    client.add_cog(SCPs(client))