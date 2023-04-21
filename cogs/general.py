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
        await ctx.send("Note The Administrator's role within the SCP Foundation is often nebulous, but they always seem to have played a role in the organisation's founding, and are credited with writing the Mission Statement. Consistently associated with SCP-262. These things, at least, seem to be true, at least assuming the Administrator exists.\nIf reports are to be believed, each Administrator has had some anomalous traits which may be a factor of the position, including partial protection from reality shifts and extremely slow aging. Some reports even indicate that \"the Administrator\" is an anomalous entity contained by the Foundation.\nThe Administrator's position in relation to O5 Command is unclear. The Administrator may hold a position similar to an O5 Council member, and may be less powerful or more powerful depending on the situation and time. Because of all this, the Administrator often comes off seeming like a wild card, albeit a rather calm wild card.\nThere may have been multiple Administrators throughout the Foundation's history, but very few reports have indicated more than one at a time. Some reports claim that the Administrator has retired, others claim that the Administrator is deceased, and still others claim that \"the Administrator\" was only ever an alias used by another member of the O5 Council, possibly O5-1.\nThe Offical\nMale. European descent. American origin. Verified post-human lifespan; reported as appearing between mid-30s and mid-50s. No unusual appearance.\nNote: This version of the Administrator has been repeatedly confirmed as a false front, used as a cover for one or more of the Foundation's actual Administrators. May still be worth looking into further.\nDeliberately over-the-top reputation. Lack of aging made relatively public by way of universally repeated rumor. Associates with numerous major heads of government, representing Foundation interests to them. Said (rather insultingly) to have \"a penchant for suits, fine liquors and loose women\". An example from a typical report:\"He has been friendly with people of many political stances and is generally well liked if not respected. When he does become angered, even heads of state are quick to appease him and commonly offer sincere apologies.\"\nUsually said to have a number of over-the-top traits, such as never bringing his hands more than a few inches apart, and ordinarily being slow and sluggish and then displaying amazing feats of strength.\nF.Williams\nMale. European descent. American origin. Mid-30s. No unusual appearance.\nAccording to these reports, an individual known as \"F. Williams\" created the original [CORRUPTED]\n[FURTHER DATA LOST]\nWe're not even sure what that first initial is short for. We've found sources claiming it's \"Frederick\", \"Francis\", \"Fritz\", \"Friedrich\" or \"Franz\". Sometimes, the surname's something else or the name's \"William Fritz\" or \"Fritzwillis\", but the letters \"F. W.\" keep showing up.\nAgnes Peterson\nFemale. European descent. American origin. Verified post-human lifespan. Appears 50+. Old fashioned, wears horn-rim glasses, keeps hair in a bun. Very proper.\nOne of the original founders of the SCP Foundation. Pulled together the initial members into an organization; produced order from the initial chaos. Jokingly referred to as being very good at herding cats. Brisk in manner. Smart, ambitious, and good at knowing when to either create or ignore rules of order.\nKismet\nFemale. Middle Eastern descent. American origin. Verified post-human lifespan. Appears 50+. No unusual appearance.\nHer role is to track down and select each new and future member of O5 Command. She is a trained mathematician, and uses a form of statistics along with occultic procedures for her selection methods. She has personally selected every single member of O5 Command, in some cases years in advance. She occasionally also opts to choose their number, though which number is sometimes kept secret from all others except her and her staff until the new promotion is ready (presumably via a slot being opened).\nSpider\nMasculine. Descent/origin unknown. Head appears 30+. Unkempt white hair. Wears thick-lensed glasses and SCP-262 (Coat of Many Arms). Nonhuman body.\nApparently a human hybrid, or nonhuman entirely. Remarkable in appearance: A mostly human head, albeit with orange eyes. Body is completely nonhuman and hardly even bipedal, made of a twisted, weathered charcoal-like material, with atrophied natural limbs. A steel mesh covering holds the body inside the Coat of Many arms, and some of the many arms keep it in place. Other arms make up his \"arms\" and \"legs\", giving him either a generally humanoid look or a rather spidery look depending on how subtle he's attempting to be.\nApparently associated with the SCP Foundation since its inception, though always in a supporting role, not at the top of the power structure. Possibly owns the land Site-19 is built on. Only a few personnel outside of O5 Command have ever seen him. Softly spoken, but harshly punishes failure.\nReferences in reports claim this Administrator originates from \"The Plane Where Eyes Cannot Follow.\"\nThe Middleman\nMale. Unknown ethnicity. Unknown nationality. Unknown age.\nEfforts to obscure this man's identity go beyond what would be expected, even for someone of his position - I've seen video recordings of him and still couldn't describe what he actually looks like. It does seem that he was originally a file clerk for a government organisation dealing with the anomalous, but sold his secrets to the thirteen people that would become the O5 Council. Despite this, it's rumored that he's sided with the Foundation's Ethics Committee in opposing several O5 decisions. Reported dead multiple times, but never seems to stay that way, for some unknown reason.\nPossibly commands Mobile Task Force Rēsh-1 (\"Seat of Consciousness\"), although it's unclear if such a Task Force even exists.\nThe Archaeologist\nMale. European descent. English Origin. Appears 60+ (verified post-human lifespan).\nAccording to official records, Frederick William Abernathy engaged in some minor archaeological research, discovered nothing of note and died in obscurity. Unofficial sources indicate a much more eventful career, starting with the discovery of a Mesopotamian Goddess while excavating an Egyptian Tomb. Later encountered the entity known as the \"Guardian At the Gate\" and commanded to \"PREPARE\" (for what?). This was the impetus for the establishment of the Secret Society for Cultural Preservation, ~~the precursor~~ one possible precursor to the SCP Foundation. Current location and status unknown, but believed to still be in an influential position within the Foundation.\nCertain reports suggest that this individual (or someone similar) may have been succeeded by a female Administrator. If so, the original Administrator is likely deceased, although there are rumors that he's still able to advise the Foundation.\nThe Duke\nMale. European Descent. Austrian origin? Appears to be in his 40s, despite being over 300 years old. Human?\nKnown as Franz C. Williams. Inherited a title as an Austrian Duke within the Hapsburg Empire in the early 1700s. Emigrated to the USA during the Seven Years' War (also known as the First Occult War). Played an unknown role in the conflict, reason for leaving Europe unclear. Established a precursor to the Foundation from his mansion in rural Virginia. Arrived in the Americas with eleven others - the original twelve Overseers? Outlived multiple O5 Councils, continues to lead the Foundation in the present day.\nEthan Horowitz\nMale. Undetermined European ethnicity. Anomalous artifacts and techniques have extended his physical capabilities/longevity. Unknown true age.\nAn acquaintance of the Serpent prior to the Foundation's creation, and frequent face in the Wanderer's Library. Perpetually youthful, optimistic, charismatic, and charming. Creator of novel spellcraft. Formed the Foundation alongside O5-1, having been inspired by the Serpent's rejection from Heaven.\nHe drinks love so deeply, it's a wonder he hasn't drowned.\nToo many arms,\ntoo many faces,\nfor one man to carry.\nAssumed the form of Death in 2016.\nLed his ground-forces against humanity in 2███.\nAssented to the disembowelment of Heaven.\ni think\nhe simply\nlost sight\nof everything.")
      @commands.command()
    async def mtf(self,ctx):
        await ctx.send("Mobile Task Forces (MTFs) are elite units comprised of personnel drawn from across the Foundation and are mobilized to deal with specific threats or situations that sometimes exceed the operational capacity or expertise of regular field personnel and — as their name suggests — may be relocated between facilities or locations as they are needed. Mobile Task Force personnel represent the \"best of the best\" of the Foundation.\nMobile Task Forces vary greatly in size, composition, and purpose. A battalion-strength combat-oriented task force trained to deal with highly aggressive anomalous entities may consist of hundreds of troops plus support personnel, vehicles, and equipment and can be deployed in whole or in part to deal with threats across the globe. However, a Mobile Task Force can also be a small, specialized intelligence-gathering or investigative task force that may have fewer than a dozen personnel if that is deemed sufficient to accomplish their goals.\nWhile in the field, task force members often pose as emergency responders, local or federal law enforcement, or military personnel appropriate to the region in which they are operating. Mobile Task Force Commanders can also request the assistance of local field units or personnel stationed at nearby Foundation facilities in order to accomplish their missions.\nOrganization\nEach unit is fundamentally structured in a way that best suits their intended purpose. While combat-oriented task forces may closely follow military hierarchy and organization, smaller units may have an informal or otherwise esoteric chain of command. As such, the responsibilities of the Mobile Task Force Commander (MTFC) for each particular task force can vary greatly; the commander for a large task force might focus on maintaining multiple teams and deploying them as necessary to each assigned operation, whereas the commander of a small team might deploy with their team and direct the operation from on location.\nSimilarly, the cohesion of each unit will vary as well. Some Mobile Task Forces consist of personnel who have trained and worked for many years or even decades together, whereas the personnel of a Mobile Task Force formed on a moment's notice to deal with a specific incident may know little more than each others' names and fields of expertise.\nCreation\nMobile Task Forces are typically commissioned as deemed necessary by the Foundation's Director of Task Forces, often with the direct approval of one or more O5 Council members. A significant number of Mobile Task Forces are created to deal with specific anomalies exhibiting traits that standard containment or response teams are unable to effectively counteract, though many were also created to pre-empt an emerging or theoretical threat.\nDeactivation\nMobile Task Forces created for the purpose of containing a particular anomaly are typically deactivated at the end of the recovery operation or when ongoing containment is deemed no longer necessary. Occasionally, such task forces remain operational if the expertise and experiences learned are considered useful for future incidents, but otherwise the task force will likely be disbanded and its personnel returned to their prior posts. Very rarely, a Mobile Task Force will also be disbanded if it suffers sufficient casualties to render it incapable of operation. In these cases, if the prior capability of that particular task force is deemed necessary, a new task force may be commissioned to replace it.")
      @commands.command(aliases=["RedRightHand,Alpha-1"])
    async def alpha1(self,ctx):
        await ctx.send("Task Force Mission: Mobile Task Force Alpha-1 (Red Right Hand) is a task force that reports directly to the O5 Council and is used in situations that require the strictest operational security. The task force consists of the Foundation's best and most loyal operatives, and serves as the O5 Council's special operations unit. Further information regarding MTF Alpha-1 is classified Level 5.\nAssisting In Containment of Objects:\nSCP-001: Dead Men\nSCP-001: MAMJUL & KORAR\nSCP-2271\nSCP-3434\nSCP-3499\nSCP-3741\nSCP-3791\nSCP-4470\nSCP-5008\nSCP-5105\nSCP-5920\nSCP-7001\nSCP-7760")#add emblem
      @commands.command(aliases=["PonyExpress,Alpha-4"])
    async def alpha4(self,ctx):
        await ctx.send("Task Force Mission: Mobile Task Force Alpha-4 (Pony Express) consists primarily of personnel trained to act as undercover employees and specialize in tracking, intercepting, and securing anomalous objects sent through postal and package delivery services worldwide.\nAssisting In Containment of Objects:\nSCP-111\nSCP-130\nSCP-360\nSCP-2177\nSCP-2577\nSCP-2752\nSCP-3060\nSCP-3512\nSCP-3601\nSCP-4209\nSCP-5430") #add emblem
      @commands.command(aliases=["Last Hope,Alpha-9"])
    async def alpha9(self,ctx):
        await ctx.send("Task Force Mission: The reborn Omega-7.  Mobile Task Force Alpha-9 (Last Hope) is explicitly intended to train and utilize humanoid SCP objects in the field.\nUtilizing Objects:\nSCP-073\nSCP-105\nSCP-2913\nSCP-2987\nSCP-4051\nSCP-4494\nSCP-4818\nSCP-7414-A\nAssisting In Containment of Objects:\nSCP-5025") #add emblem
      @commands.command(aliases=["Castaways,Beta-4"])
    async def beta4(self,ctx):
        await ctx.send("Task Force Mission: MTF Beta-4 (Castaways) is a task force created with the sole purpose of assisting and monitoring GoI-466 (Wilson's Wildlife Solutions) in their interactions with local fauna-based anomalies.\nAssisting In Containment of Objects:\nSCP-3465\nSCP-3466\nSCP-3467\nSCP-3577\nSCP-3676\nSCP-3879") #add emblem
      @commands.command(aliases=["MazHatters,Beta-7"])
    async def beta7(self,ctx):
        await ctx.send("Task Force Mission: Mobile Task Force Beta-7 (Maz Hatters) specializes in the acquisition and containment of anomalies exhibiting extreme biological, chemical, or radiological hazards as well as the rapid containment and cleanup of areas affected by such anomalies. This includes the planning and deployment of contingencies for wide-area or pandemic spread of anomalous disease agents or other contagious phenomena.\nAssisting In Containment of Objects:\nSCP-400\nSCP-550\nSCP-1280\nSCP-1393\nSCP-2133\nSCP-2376\nSCP-2438\nSCP-2810\nSCP-3016\nSCP-4771\nSCP-5397\nSCP-6118") #add emblem
      @commands.command(aliases=["HecatesSpear,Beta-777"])
    async def beta777(self,ctx):
        await ctx.send("Task Force Mission: MTF Beta-777 (Hecate's Spear) specializes in thaumaturgical ritual analysis and countermeasures; including thaumaturgical combat. Based out of Site-91.\nAssisting In Containment of Objects:\nSCP-3743\nSCP-4612\nSCP-4712\nSCP-5079\nSCP-5512\nSCP-5626\nSCP-5923\nSCP-5957\nSCP-6094\nSCP-6364") #add emblem
      @commands.command(aliases=["RedHerrings,Gamma-5"])
    async def gamma5(self,ctx):
        await ctx.send("Task Force Mission: Mobile Task Force Gamma-5 (Red Herrings) specializes in preventing the dissemination of knowledge of anomalous events or phenomena in cases where initial suppression efforts have proven ineffective or insufficient, or in cases where such knowledge has already reached critical levels of public exposure. This includes the research and deployment of experimental amnestics as well as memory fabrication procedures.Assisting In Containment of Objects:\nSCP-1086\nSCP-1110\nSCP-1460\nSCP-1532\nSCP-1548\nSCP-1570\nSCP-1618\nSCP-1670\nSCP-2105\nSCP-2342\nSCP-2631\nSCP-3339\nSCP-3666\nSCP-4039\nSCP-4160\nSCP-5060\nSCP-5479\nSCP-5916") #add emblem
      @commands.command(aliases=["DeepFeeders,Gamma-6"])
    async def gamma6(self,ctx):
        await ctx.send("Task Force Mission: Mobile Task Force Gamma-6 (Deep Feeders) specializes in the investigation and tracking of deep-sea or oceanic anomalies.\nAssisting In Containment of Objects:\nSCP-169\nSCP-879\nSCP-1264\nSCP-1409\nSCP-2120\nSCP-2770\nSCP-2956\nSCP-3069\nSCP-5533\nSCP-6055") #add emblem
      @commands.command(aliases=["AsimovsLawbringers,Gamma-13"])
    async def gamma13(self,ctx):
        await ctx.send("Task Force Mission: Mobile Task Force Gamma-13 (Asimov's Lawbringers) specializes in the investigation, tracking, and apprehension of anomalous objects, persons, and entities associated with GoI-1115 (Anderson Robotics). This includes identification of Anderson customers, location of Anderson products and conduction of raids on Anderson offices.\nAssisting In Containment of Objects:\nSCP-2306\nSCP-2806\nSCP-2906\nSCP-3560\nSCP-6660\nSCP-750-KO") #add emblem
      @commands.command(aliases=["FrontRunners,Delta-5"])
    async def delta5(self,ctx):
        await ctx.send("Task Force Mission: Mobile Task Force Delta-5 (Front Runners) is comprised of multiple autonomous deep-cover cells specializing in the identification and pre-emptive acquisition of anomalous objects and entities of interest to other Groups of Interest.\nAssisting In Containment of Objects:\nSCP-185\nSCP-472\nSCP-1139\nSCP-5071") #add emblem
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