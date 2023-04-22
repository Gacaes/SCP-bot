import discord
from discord import Embed
from discord.ext import commands
from suggestions import suggestions
from random import choice
from html_discord import send
from funcs import msg_short
#import general_data as gd

#i have a test BRB
class General(commands.Cog):
    def __init__(self,client):
        self.client=client
    @commands.Cog.listener()
    async def on_ready(self):
        print('General Cog Ready')
    
    #here are where your commands have been moved to
    
    
    @commands.command()
    async def owner(self,ctx):
        await ctx.channel.send("I am property of 05-01 The founder.")

    @commands.command()
    async def suggestion(self,ctx):
        await ctx.channel.send(choice(suggestions))

    @commands.command()
    async def hardware(self,ctx):
        await ctx.channel.send("Here is a picture of my hardware. https://scp-wiki.wdfiles.com/local--files/scp-001-ex/erzatz.png")

    @commands.command()
    async def votelog(self,ctx):
        await ctx.channel.send(gd.votelog)

    @commands.command()
    async def vote315D27(self,ctx):
        await ctx.channel.send(gd.vote315D27)

    @commands.command()
    async def vote111H43(self,ctx):
        await ctx.channel.send(gd.vote111H43)

    @commands.command()
    async def vote672C91(self,ctx):
        await ctx.channel.send(gd.vote672C91)
    
    @commands.command()
    async def vote954E36(self,ctx):
        await ctx.channel.send("this string has moved to line 8 of generators/general.py") 
        #take this for an example
    @commands.command()
    async def vote149B22(self,ctx):
        await ctx.channel.send()
    @commands.command()
    async def vote229K36(self,ctx):
        await ctx.channel.send()
    @commands.command()
    async def vote713D27(self,ctx):
        await ctx.channel.send()
    @commands.command()
    async def vote821C95(self,ctx):
        await ctx.channel.send()
    @commands.command()
    async def vote287J09(self,ctx):
        await ctx.channel.send()
    @commands.command()
    async def vote475D47(self,ctx):
        await ctx.channel.send()
    @commands.command()
    async def vote174H62(self,ctx):
        await ctx.channel.send()
    @commands.command()
    async def vote635U01(self,ctx):
        await ctx.channel.send()
    
    @commands.command()
    async def proposal1(self,ctx):
        await ctx.channel.send()
    @commands.command()
    async def proposal2(self,ctx):
        await ctx.channel.send()
    @commands.command()
    async def proposal3(self,ctx):
        await ctx.channel.send()
    @commands.command()
    async def proposal4(self,ctx):
        await ctx.channel.send()
    @commands.command()
    async def proposal5(self,ctx):
        await ctx.channel.send()
    @commands.command()
    async def proposal6(self,ctx):
        await ctx.channel.send()
    @commands.command()
    async def proposal7(self,ctx):
        await ctx.channel.send()
    @commands.command()
    async def proposal8(self,ctx):
        await ctx.channel.send()
    @commands.command()
    async def proposal9(self,ctx):
        await ctx.channel.send()
    @commands.command()
    async def proposal10(self,ctx):
        await ctx.channel.send()
    @commands.command()
    async def proposal11(self,ctx):
        await ctx.channel.send()
    @commands.command()
    async def proposal12(self,ctx): #how is this wrong all of a sudden?
        await ctx.channel.send()

    @commands.command()
    async def BULLETIN1(self,ctx):
        await ctx.channel.send()
    @commands.command()
    async def BULLETIN2(self,ctx):
        await ctx.channel.send()
    @commands.command()
    async def BULLETIN3(self,ctx):
        await ctx.channel.send()
    @commands.command()
    async def BULLETIN4(self,ctx):
        await ctx.channel.send()
    @commands.command()
    async def BULLETIN5(self,ctx):
        await ctx.channel.send()
    @commands.command()
    async def BULLETIN6(self,ctx):
        await ctx.channel.send()
    @commands.command()
    async def BULLETIN7(self,ctx):
        await ctx.channel.send()
    @commands.command()
    async def errorreport1(self,ctx):
        await ctx.channel.send()
    @commands.command()
    async def errorreport2(self,ctx):
        await ctx.channel.send()
    @commands.command()
    async def errorreport3(self,ctx):
        await ctx.channel.send()
    @commands.command()
    async def errorreport4(self,ctx):
        await ctx.channel.send()
    @commands.command(aliases = ["class"])
    async def classes(self,ctx):
        message=send()
    
    @commands.command()
    async def commanddossier(self,ctx):
        await ctx.channel.send()
        #@commands.command(aliases=['dossier05-01'])
        #async def dossier0501(self,ctx):  
            #await ctx.send
    @commands.command(aliases=['dossier05-01'])
    async def dossier0501(self,ctx):
        #await ctx.channel.send()
        string
        for msg in msg_short(string):
            await ctx.channel.send(msg)
        
    @commands.command(aliases=['dossier05-03'])
    async def dossier0503(self,ctx):  
        await ctx.send()
    @commands.command(aliases=['dossier05-02'])
    async def dossier0502(self,ctx):  
        await ctx.send()
    @commands.command(aliases=["dossier05-04"])
    async def dossier0504(self,ctx):
        await ctx.send()
    @commands.command(aliases=["dossier05-05"])
    async def dossier0505(self,ctx):
        await ctx.send()
    @commands.command(aliases=["dossier05-06"])
    async def dossier0506(self,ctx):
        await ctx.send()
    @commands.command(aliases=["dossier05-07"])
    async def dossier0507(self,ctx):
        await ctx.send()
      @commands.command(aliases=["dossier05-08"])
    async def dossier0508(self,ctx):
        await ctx.send()
      @commands.command(aliases=["dossier05-09"])
    async def dossier0509(self,ctx):
        await ctx.send()
      @commands.command(aliases=["dossier05-10"])
    async def dossier0510(self,ctx):
        await ctx.send()
      @commands.command(aliases=["dossier05-11"])
    async def dossier0511(self,ctx):
        await ctx.send()
       @commands.command(aliases=["dossier05-12"])
    async def dossier0512(self,ctx):
        await ctx.send()
      @commands.command(aliases=["dossier05-13"])
    async def dossier0513(self,ctx):
        await ctx.send()
      @commands.command(aliases=["05staff"])
    async def 05staff(self,ctx):
        await ctx.send()
      @commands.command(aliases=["05 info"])
    async def 05info(self,ctx):
        await ctx.send()
      @commands.command(aliases=["Alternate 05 theories"])
    async def alt05theory(self,ctx):
        await ctx.send()
       @commands.command(aliases=["Admin"])
    async def administrator(self,ctx):
        await ctx.send()
      @commands.command()
    async def mtf(self,ctx):
        await ctx.send()
      @commands.command(aliases=["RedRightHand,Alpha-1"])
    async def alpha1(self,ctx):
        await ctx.send()#add emblem
      @commands.command(aliases=["PonyExpress,Alpha-4"])
    async def alpha4(self,ctx):
        await ctx.send() #add emblem
      @commands.command(aliases=["Last Hope,Alpha-9"])
    async def alpha9(self,ctx):
        await ctx.send() #add emblem
      @commands.command(aliases=["Castaways,Beta-4"])
    async def beta4(self,ctx):
        await ctx.send() #add emblem
      @commands.command(aliases=["MazHatters,Beta-7"])
    async def beta7(self,ctx):
        await ctx.send() #add emblem
      @commands.command(aliases=["HecatesSpear,Beta-777"])
    async def beta777(self,ctx):
        await ctx.send() #add emblem
      @commands.command(aliases=["RedHerrings,Gamma-5"])
    async def gamma5(self,ctx):
        await ctx.send() #add emblem
      @commands.command(aliases=["DeepFeeders,Gamma-6"])
    async def gamma6(self,ctx):
        await ctx.send() #add emblem
      @commands.command(aliases=["AsimovsLawbringers,Gamma-13"])
    async def gamma13(self,ctx):
        await ctx.send() #add emblem
      @commands.command(aliases=["FrontRunners,Delta-5"])
    async def delta5(self,ctx):
        await ctx.send() #add emblem
      @commands.command(aliases=["VillageIdiots,Epsilon-6"])
    async def epsilon6(self,ctx):
        await ctx.send("Task Force mission: MTF Epsilon-6 (Village Idiots) specializes in the investigation, containment, and subsequent cleanup of anomalies in rural and suburban environments.\nAssisting In Containment of Objects:\nSCP-2447\nSCP-2480\nSCP-2561\nSCP-2815\nSCP-3322\nSCP-3449\nSCP-3845\nUndefined\nSCP-4709\nSCP-4775\nSCP-5000\nSCP-5536\nSCP-5700\nSCP-5820\nSCP-5910\nSCP-6186\nSCP-6619\nSCP-6717") #add emblem
      @commands.command(aliases=["FireEaters,Epsilon-9"])
    async def epsilon9(self,ctx):
        await ctx.send("Task Force mission: Epsilon-9 (Fire Eaters) specializes in the use of incendiary weaponry and operations in high-temperature environments.\nAssisting In Containment of Objects:\nSCP-165\nSCP-262\nSCP-968\nSCP-2340\nSCP-3205\nSCP-4111") #add emblem
      @commands.command(aliases=["NineTailedFox,Epsilon-11"])
    async def epsilon11(self,ctx):
        await ctx.send("Task Force Mission: Mobile Task Force Epsilon-11 (Nine Tailed Fox) handles internal security for the SCP Foundation, under oversight by MTF Alpha-1. They are a special ops force deployed to Foundation Sites when standard protocols fail and multiple breaches are imminent. As such, most of their operations are classified.\nAssisting In Containment of Objects:\nSCP-2139\nSCP-2479\nSCP-3030\nSCP-4171\nSCP-4511\nSCP-5018\nSCP-5254") #add emblem
      @commands.command(aliases=["MoleRats,Zeta-9"])
    async def Zeta9(self,ctx):
        await ctx.send("Task Force Mission: Mobile Task Force Zeta-9 (Mole Rats) specializes in the investigation, exploration, and containment of underground or enclosed areas exhibiting anomalous phenomena, particularly those with inconsistent topography or unstable spacetime.\nAssisting In Containment of Objects:\nSCP-001: AMONI-RAM\nSCP-184\nSCP-455\nSCP-835\nSCP-1162\nSCP-1444\nSCP-1730\nSCP-2518\nSCP-2591\nSCP-2955\nSCP-3066\nSCP-3512\nSCP-3667\nSCP-5015\nSCP-5100\nSCP-5392\nSCP-5653\nSCP-5992\nSCP-6991") #ditto
      @commands.command(aliases=["BegoneThoth,Eta-4"])
    async def Eta4(self,ctx):
        await ctx.send("Task Force Mission: Mobile Task Force Eta-4 (Begone Thoth) is a unit of intelligent SCP-3095-affected seabirds. Eta-4 specializes in information collection and analysis, complementary field research and support, and in extreme cases, airborne combat. The task force was ultimately charged with protecting humanity after the BE-Class \"Migration\" End-of-Consciousness Scenario.\nAssisting In Containment of Objects:\nEE-3570\nSCP-4688\nSCP-5106") #ditto
      @commands.command(aliases=["JaegerBombers,Eta-5"])
    async def Eta5(self,ctx):
        await ctx.send("Task Force Mission: Mobile Task Force Eta-5 (Jaeger Bombersis a rapid-response unit specializing in the tracking, capturing, and containment of Large-Scale Aggressors (entities over 30m in height). Deploys from, and detains LSAs within Dimensional-Site-172.\nAssisting In Containment of Objects:\nSCP-2764\nSCP-3534\nSCP-4315\nSCP-5391\nSCP-5514") #ditto
      @commands.command(aliases=["SeeNoEvil,Eta-10"])
    async def Eta10(self,ctx):
        await ctx.send("Task Force Mission: Mobile Task Force Eta-10 (See No Evil) specializes in the investigation, acquisition, and initial containment of objects or entities exhibiting visual cognitohazards, visual memetic agents, or otherwise require indirect or alternative observation in order to safely handle.\nAssisting In Containment of Objects:\nSCP-020\nSCP-125\nSCP-571\nSCP-904\nSCP-1561\nSCP-2136\nSCP-2140\nSCP-2155\nSCP-2828\nSCP-3393\nSCP-3519\nSCP-3597\nSCP-4149\nSCP-4550\nSCP-4600\nSCP-4879\nSCP-5052\nSCP-6178") #ditto
      @commands.command(aliases=["SavageBeasts,Eta-11"])
    async def Eta11(self,ctx):
        await ctx.send("Task Force Mission: Mobile Task Force Eta-11 (Savage Beasts) specializes in the investigation, acquisition, and containment of auditory and musical anomalies, including any auditory cognitohazards or sound-based anomalous threats.\nAssisting In Containment of Objects:\nSCP-1687\nSCP-1844\nSCP-2402\nSCP-2828\nSCP-3447\nSCP-3519\nSCP-4150\nSCP-4614") #ditto
      @commands.command(aliases=["SavageBeasts,Eta-11"])
    async def Eta11(self,ctx):
        await ctx.send
     
  
def setup(client):
    client.add_cog(General(client))