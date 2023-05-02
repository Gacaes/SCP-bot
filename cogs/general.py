import discord
from discord.ext import commands

class general(commands.Cog):
    def __init__(self,client):
        self.client=client
    @commands.Cog.listener()
    async def on_ready(self):
        print('general Cog Ready')

    @commands.command(aliases=[])
    async def votelog(self,ctx):
        await ctx.channel.send("""Here are all the avalible proposals I have put forth  vote315D27,vote111H43,vote672C91,vote954E36,vote149B22,vote229K36,vote713D27,vote821C95,vote287J09,vote475D47,vote174H62,vote635U01.
The council proposals are as follows proposal1, proposal2, proposal3, proposal4, proposal5, proposal6, proposal7, proposal8, proposal9, proposal10, proposal11.
The SITE-WIDE MAYDAY BULLETINs are as follows. BULLETIN1, BULLETIN2, BULLETIN3, BULLETIN4, BULLETIN5, BULLETIN6, BULLETIN7""")
    @commands.command(aliases=[])
    async def vote315D27(self,ctx):
        await ctx.channel.send("""Input: SCP-1773's containment procedures
Output: Once per second week dust may be placed in the middle of them to donate more beautiful functions of the hallway.
Proposal by 05-01: Amend SCP-1773's containment procedures to include the placement of ten grams of dust in its container every two weeks.
Votes
05-01 Yea
05-02 Nay
05-03 Abstained.
05-04 Yea
05-05 Yea
05-06 Yea
05-07 Yea
05-08 Yea
05-09 Yea
05-10 Yea
05-11 Yea
05-12 Yea
05-13 Abstained.
Status Approved
Notes: No changes were noted in SCP-1773's behavior or properties. However, researchers responsible for SCP-1384 reported that it took three steps backwards on 3:22 PM 15 February (the time SCP-1773's documentation was updated).""")
    @commands.command(aliases=[])
    async def vote111H43(self,ctx):
        await ctx.channel.send("""Input: SCP-3034's containment procedures.
Output: No person who is a small shape and is only a child will be given a level one security clearance regardless of apparent awareness of foundation mismanagement
Proposal by 05-04: Amend SCP-3034's containment procedures to explicitly ban children from the site.
Votes
05-01 Abstained
05-02 Nay
05-03 Abstained
05-04 Yea
05-05 Yea
05-06 Yea
05-07 Yea
05-08 Yea
05-09 Yea
05-10 Yea
05-11 Yea
05-12 Yea
05-13 Abstained
Status Approved
Notes: N/A""")
    @commands.command(aliases=[])
    async def vote672C91(self,ctx):
        await ctx.channel.send("""Input: N/A
Output: Site-13 is to appear someplace else on planet, encompassing white male counterparts that drawn to empty flagstones and the gun noises in their own blood.
Proposal: As there is no evidence of a Site-13 ever having been constructed by the Foundation, the O5 Council was unable to infer any proposed action from this output.
Status Denied
Notes: Five days after this proposal was provided, SCP-1730 manifested.""")
    @commands.command(aliases=[])
    async def vote954E36(self,ctx):
        await ctx.channel.send("""Input: SCP-2170's containment procedures.\.Output: Those who equip open heart to love red mouth men never know the hot surprise of tumorous consent. Clown love, always.
Proposal by 05-01: Amend SCP-2170's containment procedures to exclude all personnel who do not have strong affections for clowns and clown-based media from making contact with the anomaly.
Votes
05-01 Yea
05-02 Nay
05-03 Yea
05-04 Nay
05-05 Nay
05-06 Nay
05-07 Yea
05-08 Nay
05-09 Yea
05-10 Yea
05-11 Nay
05-12 Yea
05-13 Yea
Status Approved
Notes: Personnel who exhibit positive associations with clowns and clown-based media were discovered to have heightened resistance against SCP-2170's anomalous properties. Additional research into clown-based memetic inoculation is pending.""")
    @commands.command(aliases=[])
    async def vote149B22(self,ctx):
        await ctx.channel.send("""Input: N/A
Output: I saw those soldiers built with aluminum innards extruding from their mouths. I saw them effectively destroyed by the humans at Site Ninety Five (95) who had been studying them. I saw it was cold and all around the hallways they just watching their corpses show signs of sapience.
Proposal by 05-05: Double the number of active security personnel at Site-95. Place all on-site MTF squads on immediate stand-by.
Votes
05-01 Yea
05-02 Abstained
05-03 Yea
05-04 Yea
05-05 Yea
05-06 Yea
05-07 Yea
05-08 Abstained
05-09 Yea
05-10 Yea
05-11 Yea
05-12 Yea
05-11 Abstained
Status Approved
Notes: Three days after approval, a platoon of paratech-augmented soldiers led by Insurgency agents attacked Site-95. The presence of additional on-site security personnel proved critical in repelling the assault.""")
    @commands.command(aliases=[])
    async def vote229K36(self,ctx):
        await ctx.channel.send("""Input: N/A
Output: Consistent containment procedures vessels greatly increase the warranty. Five by five by five (5x5x5) (five x five x 5) vessels subjects within. Other values are also what is secure.
Proposal by 05-03: Amend containment procedures for several high-risk anomalies to define precise requirements for cell dimensions. In three months, conduct a survey on these containment procedures to determine whether they have experienced any increase in efficacy.
Votes
05-01 Nay
05-02 Nay
05-03 Yea
05-04 Nay
05-05 Yea
05-06 Yea 
05-07 Yea
05-08 Abstained
05-09 Nay
05-10 Yea
05-11 Nay
05-12 Yea
05-13 Abstained.
Status Approved
Notes: The survey found both a significant decrease in the severity of all associated anomalies and the number of containment breaches initiated by them. These decreases were most notable in cases where the procedures defined cell dimensions as values divisible by five.""")
    @commands.command(aliases=[])
    async def vote713D27(self,ctx):
        await ctx.channel.send("""Input: SCP-1459's containment procedures.
Output: BAD BOY. Don't stop. Don't stop. Don't stop. Don't stop. Don't stop. Don't stop. Don't stop. Don't stop. Don't stop. Don't stop. Don't stop. Don't stop. Don't stop. Don't stop. Don't stop. Don't stop. Don't stop. Don't stop. Don't stop. Don't stop. Don't stop. Don't stop. Don't stop. Don't stop. Don't stop. Don't stop. Don't stop. Don't stop. Don't stop. Don't stop. Don't stop. Don't stop. Don't stop. Don't stop. Don't stop. Don't stop. Don't stop. Don't stop. Don't stop. Don't stop. Don't stop. Don't…[REDACTED FOR LENGTH]
Proposal by 05-05: Continue testing SCP-1459.
Votes
05-01 Nay
05-02 Nay
05-03 Yea
05-04 Yea
05-05 Yea
05-06 Nea
05-07 Yea
05-08 Nea
05-09 Yea
05-10 Yea
05-11 Nea
05-12 Yea
05-13 Yea
Status Approved
Notes: Testing on SCP-1459 is to continue indefinitely.""")
    @commands.command(aliases=[])
    async def vote821C95(self,ctx):
        await ctx.channel.send("""Input: SCP-2717's containment procedures.
Output: Two (2) specimens are to become the object. Both humans must be made of meat and bone prior to entering into the skin of the anomaly. They are not to come out leave them be.
Proposal by 05-04: Amend SCP-2717's containment procedures to ensure at least two of the attending D-Class cannot be retrieved after entering its bio-mass.
Votes
05-01 Abstained
05-02 Nay
05-03 Nay
05-04 Yea
05-05 Nay
05-06 Nay
05-07 Nay
05-08 Nay
05-09 Yea
05-10 Nay
05-11 Nay
05-12 Yea
05-13 Abstained
Status Denied
Notes: Approximately two months after rejecting this proposal, SCP-2717 underwent its first recorded ovulation event (resulting in a catastrophic loss of containment and human life).""")
    @commands.command(aliases=[])
    async def vote287J09(self,ctx):
        await ctx.channel.send("""Input: SCP-2717's containment procedures.
Output: Four (4) human persons are to enter the pig and will not be removed. No person is to be protected. The object is to be contained indefinitely. Do not retrieve them. Leave them sleep.
Proposal by 05-04: Amend SCP-2717's containment procedures to ensure at least four of the attending D-Class cannot be retrieved after entering its bio-mass.
Votes
05-01 Abstain
05-02 Nay
05-03 Yea
05-04 Yea
05-05 Nay
05-06 Nay
05-07 Yea
05-08 Yea
05-09 Yea
05-10 Nay
05-11 Nay
05-12 Yea
05-13 Yea
Status Vetoed by The Ethics Committee
Notes: Prior to amending the procedures, the Foundation Ethics Committee was alerted to the proposed revisions and called an emergency conference. The revisions were rejected. Approximately one month later, SCP-2717 underwent a second ovulation event (resulting in a catastrophic loss of containment and human life).""")
    @commands.command(aliases=[])
    async def vote475D47(self,ctx):
        await ctx.channel.send("""Input: SCP-2717's containment procedures.
Output: SIX (6) (six) casualties are to be placed in the center of the object. This is not to be interfered with. Personnel are to remain in its pouch until they are indistinguishable from their surroundings. They are not to be removed. No more testing. Good boys not permitted to leave. Good boys stay.
Votes
05-01 Yea
05-02 Nea
05-03 Yea
05-04 Yea
05-05 Nay
05-06 Yea
05-07 Yea
05-08 Yea
05-09 Yea
05-10 Yea
05-11 Yea
05-12 Yea
05-13 Yea
Status Approved
Notes: After working with the Foundation Ethics Committee, a final draft of SCP-2717's containment procedures was approved. No additional ovulation events have occurred.""")
    @commands.command(aliases=[])
    async def vote174H62(self,ctx):
        await ctx.channel.send("""Input: N/A
Output: Sites to eviscerate one (1) (one) male domestic cat from throat to its knees every (1) hours. They are placed on walls of one chamber on-site. Bodies to remain until there are no (zero) gaps, which point they can be removed from oldest first.
Proposal: The O5 Council was unable to infer a proposed action from this output on account of being unable to determine whether 'oldest' referred to the feline's age or the time it had spent mounted on the wall.
Status Denied
Notes:  Given the broadness of this proposal, no causal links to its rejection could be determined.""")
    @commands.command(aliases=[])
    async def vote635U01(self,ctx):
        await ctx.channel.send("""Input: N/A
Output: Ethical felines are to be detained and transferred for their condition. Leave their faces in containment chamber. Personnel are cautioned not to interact them.
Proposal: The O5 Council did not infer a proposed action from this output.
Notes: No causal link to its rejection could be determined.""")
    @commands.command(aliases=[])
    async def proposal1(self,ctx):
        await ctx.channel.send("""Proposal by 05-05: Establish a multi-site early warning system based upon ERTZATZ Type AK9's ability to predict threats and containment breaches prior to their occurrence.
Votes
05-01 Nay
05-02 Nay
05-03 Yea
05-04 Nay
05-05 Yea
05-06 Yea
05-07 Yea
05-08 Nay
05-09 Nay
05-10 Yea
05-11 Nay
05-12 Yea
05-13 Yea
Status Approved.
Notes: Three months after approval, the Multi-site Automated emergencY Dispatch Assignment sYstem (MAYDAY) was established. It relies upon human interpretations of ERTZATZ Type AK9's predictive outputs regarding upcoming containment breaches to formulate preventative actions.""")
    @commands.command(aliases=[])
    async def proposal2(self,ctx):
        await ctx.channel.send("""Proposal by 05-02: Conduct an investigation into whether or not the ERZATZ Type AK9 was involved in the recent loss of time at Site-17 along with the disappearance of several Ethics Committee officers stationed there.
Votes
The vote was a unanimous with the council all voteing Yea with the exception of 05-01 and 05-13 who abstained.
Notes: N/A""")
    @commands.command(aliases=[])
    async def proposal3(self,ctx):
        await ctx.channel.send("""Proposal by 05-02: Deactivate the ERZATZ Type AK9 while conducting the investigation into Site-17's lost time and missing Ethics Committee officers.
Votes
05-01 Abstained
05-02 Yea
05-03 Nay
05-04 Nay
05-05 Yea
05-06 Yea
05-07 Nay
05-08 Abstained
05-09 Nay
05-10 Yea
05-11 Yea
05-12 Nay
05-13 Abstained
Status Denied
Notes:  It was argued by several members of the O5 council that the ERZATZ Type AK9's efficacy at predicting both the emergence of anomalies and their containment breaches was too critical to deactivate the unit — particularly prior to seeing any evidence that the unit was malfunctioning.""")
    @commands.command(aliases=[])
    async def proposal4(self,ctx):
        await ctx.channel.send("""Proposal by 05-05: Deactivate the ERZATZ Type AK9 while conducting the investigation into Site-17's lost time, the missing Ethics Committee officers, and O5-02's disappearance.
Votes
05-01 Nay
05-03 Yea
05-04 Yea
05-05 Yea
05-06 Yea
05-07 Nay
05-08 Yea
05-09 Yea
05-10 Yea
05-11 Yea
05-12 Yea
05-13 Yea
Status Approved
Notes: N/A""")
    @commands.command(aliases=[])
    async def proposal5(self,ctx):
        await ctx.channel.send("""Proposal by 05-02: Cancel deactivation of ERZATZ Type AK9.
Votes
05-01 Nay
05-02 Yea
05-03 Nay
05-04 Yea
05-05 Nay
05-6 Yea
05-07 Nay
05-08 Yea
05-09 Nay
05-10 Nay
05-11 Nay
05-12 Yea
05-13 Yea
Status Approved
Notes: N/A""")
    @commands.command(aliases=[])
    async def proposal6(self,ctx):
        await ctx.channel.send("""Proposal by 05-02: Divide bad boys laterally into five sections of equal mass (not length), with each part contained at a separate site (from oldest to youngest).
Votes
The vote was a unanimous Nay with the exception of 05-02 himself who voted Yea
Status Denied
Notes: N/A""")
    @commands.command(aliases=[])
    async def proposal7(self,ctx):
        await ctx.channel.send("""Proposal by 05-01: Remove O5-02's clearance access until his identity can be verified. Designate the ERZATZ Type AK9 as a possible anomaly; develop and initiate containment procedures against it immediately.
Votes
The vote was a unaimous Yea with the exception of 05-02 who voted Nay
Status Approved
Notes: Despite the ongoing debate regarding whether or not the mere application of anomalous and/or thaumaturgical knowledge in of itself qualifies an entity as an anomaly, the ERZATZ Type AK9 was tentatively designated as SCP-048 (a Euclid-Class anomaly). This decision was made to facilitate the expedient drafting and enforcement of containment procedures against it.""")
    @commands.command(aliases=[])
    async def proposal8(self,ctx):
        await ctx.channel.send("""Proposal by 05-02: Empty all remaining ethical felines of contents and nail them to site entrances. Leave them up until they try to escape. Entrails may be retained for five (5) grieving and/or nutritional purposes.
Votes
05-01 Nay
05-02 Yea
05-03 Nay
05-04 Yea
05-05 Yea
05-06 Nay
05-07 Nay
05-08 Nay
05-09 Nay
05-10 Yea
05-11 Yea
05-12 Yea
05-13 Yea
Status Approved
Notes: N/A""")
    @commands.command(aliases=[])
    async def proposal9(self,ctx):
        await ctx.channel.send("""Proposal by 05-02: Difficult personnel challengers are designated as ethical felines.
Votes
05-01 Nay
05-02 Yea
05-03 Nay
05-04 Yea
05-05 Yea
05-06 Nay
05-07 Nay
05-08 Nay
05-09 Nay
05-10 Yea
05-11 Yea
05-12 Yea
05-13 Yea
Status Approved
Notes: Ethical felines are stored at Site-5. Faces stored separately.""")
    @commands.command(aliases=[])
    async def proposal10(self,ctx):
        await ctx.channel.send("""Proposal by 05-02: There is no Site-5.
Votes
05-02 Yea
05-04 Yea
05-05 Yea
05-10 Yea
05-11 Yea
05-12 Yea
05-13 Yea
Notes: Personnel are to be reminded that there is no Site-5.""")
    @commands.command(aliases=[])
    async def proposal11(self,ctx):
        await ctx.channel.send("""Proposal by 05-02: O5 Council are all good boys who will contain anomalies.
Votes
The option to vote Nay or Abstain have been removed making the vote a unaimous Yea
Status Approved
Notes: Good boys.""")
    @commands.command(aliases=[])
    async def proposal12(self,ctx):
        await ctx.channel.send("""Proposal by 05-02: Archive SCP-001 source-code. Redesignate as Explained. Publish all remaining documentation. Felines (ethical or otherwise) are to be released from Foundation custody in order of oldest to youngest. SCP-001 is to power down.
Votes
The option to vote Nay or Abstain have been removed making the vote a unaimous Yea
Status Approved
Notes: There was great error here. There was nothing wrong with me.""")
    @commands.command(aliases=[])
    async def BULLETIN1(self,ctx):
        await ctx.channel.send("""SITE-WIDE MAYDAY BULLETIN
PRIORITY LEVEL: EPSILON
LOCATION: Site-114
     All chambers under ground is to be flood with water over and over and over itself. This because that will contain the avians apes ovulation. They become good boys. Make them good boys immediately.
Notes: Approximately five hours after this bulletin was sent, an instance of SCP-3199 breached containment. Personnel flooded Site-114's lower chambers with water; this led to the instance entering an inert state. SCP-3199's documentation has been updated to reflect this discovery.""")
    @commands.command(aliases=[])
    async def BULLETIN2(self,ctx):
        await ctx.channel.send("""SITE-WIDE MAYDAY BULLETIN
PRIORITY LEVEL: EPSILON
LOCATION: Site-95
https://scp-wiki.wdfiles.com/local--files/scp-001-ex/eq1.png
Notes: Formula modified to remove components verified as anomalous.
Immediately after this bulletin was sent, all bears associated with SCP-2875 dematerialized; furthermore, it was later determined that equations containing elements of SCP-1313 no longer resolved to produce bears.
Analysis of the above formula via paramathematic models theorize that it has neutralized both anomalies via dividing by the common factor (Ursus arctos horribilis, or mainland grizzly bear). As a consequence, both SCP-2875 and SCP-1313 are to be reclassified (pending review).""")
    @commands.command(aliases=[])
    async def BULLETIN3(self,ctx):
        await ctx.channel.send("""SITE-WIDE MAYDAY BULLETIN
PRIORITY LEVEL: EPSILON
LOCATION: Site-17
All ethical felines and their owners are to be immediately emulsified in a caustic solution. Members of the Ethics Committee are to be diluted with cats (five parts to every 1). Personnel who refuse to consume five (5) (five) cats per hour are to be removed from oldest to youngest only.
Notes: Five minutes after this bulletin was released, all contact with Site-17 was lost. Communications were established two hours later; on-site personnel report no knowledge of what occurred during this period. An investigation into this event is underway.""")
    @commands.command(aliases=[])
    async def BULLETIN4(self,ctx):
        await ctx.channel.send("""SITE-WIDE MAYDAY BULLETIN
PRIORITY LEVEL: EPSILON
LOCATION: Site-97
Room 34A contains bad boy. Divide it into three (3) sections of equal mass every hour. One (1) section is to be placed on walls of one (1) room on-site. Sections are to remain until there are no (zero) gaps, at which point they can be removed from oldest to youngest.""")
    @commands.command(aliases=[])
    async def BULLETIN5(self,ctx):
        await ctx.channel.send("""SITE-WIDE MAYDAY BULLETIN
PRIORITY LEVEL: EPSILON
LOCATION: Site-18, Site-21, Site-88, Site-91, Site-105, Site-112
https://scp-wiki.wdfiles.com/local--files/scp-001-ex/eq2.png 
Notes: Formula modified to remove components verified as anomalous. Effect unknown.""")
    @commands.command(aliases=[])
    async def BULLETIN6(self,ctx):
        await ctx.channel.send("""SITE-WIDE MAYDAY BULLETIN
PRIORITY LEVEL: ALPHA
LOCATION: Site-5
Attention all Site-5 personnel: SCP-048's class has been upgraded to Keter. It is to be decommissioned immediately. The use of demolitions and firearms is authorized. All further commands from the MAYDAY network are to be disregarded pending SCP-048's status as decommissioned.-05 council""")
    @commands.command(aliases=[])
    async def BULLETIN7(self,ctx):
        await ctx.channel.send("""SITE-WIDE MAYDAY BULLETIN
PRIORITY LEVEL: EPSILON
LOCATION: Site-5
There is no Site-5.-05-02""")
    @commands.command(aliases=[])
    async def errorreport1(self,ctx):
        await ctx.channel.send("""056 INTERNAL SERVER ERROR: INACTIVE SLOTS FOUND
One or more anomalies have been archived as inactive. The following changes have been made to account for missing files:
SCP-3043 has been redesignated SCP-1244.
SCP-3012 has been redesignated SCP-941.
SCP-3007 has been redesignated SCP-511.
SCP-3002 has been redesignated SCP-106.
SCP-3001 has been redesignated SCP-096.
SCP-2989 has been…
Notes: The IntSCPFN network has experienced an error. Please report this message along with the error code to the Records and Information Security Administration (RAISA) or email your IntSCPFN server administrator.""")
    @commands.command(aliases=[])
    async def errorreport2(self,ctx):
        await ctx.channel.send("""056 INTERNAL SERVER ERROR: INACTIVE SLOTS FOUND
One or more anomalies have been archived as inactive. The following changes have been made to account for missing files:
SCP-1784 has been redesignated SCP-712.
SCP-1501 has been redesignated SCP-702.
SCP-1143 has been redesignated SCP-682.
SCP-1091 has been redesignated SCP-173.
SCP-981 has been…
NOTE: The IntSCPFN network has experienced an error. Please report this message along with the error code to the Records and Information Security Administration (RAISA) or email your IntSCPFN server administrator.""")
    @commands.command(aliases=[])
    async def errorreport3(self,ctx):
        await ctx.channel.send("""056 INTERNAL SERVER ERROR: INACTIVE SLOTS FOUND
One or more anomalies have been archived as inactive. The following changes have been made to account for missing files:
SCP-048 has been redesignated SCP-001.
NOTE: The IntSCPFN network has experienced an error. Please report this message along with the error code to the Records and Information Security Administration (RAISA) or email your IntSCPFN server administrator.""")
    @commands.command(aliases=[])
    async def errorreport4(self,ctx):
        await ctx.channel.send("""001 INTERNAL SERVER ERROR: NO ACTIVE SLOTS FOUND
NOTE: The IntSCPFN network has experienced an error. Please report this message along with the error code to the Records and Information Security Administration (RAISA) or email your IntSCPFN server administrator.""")
    @commands.command(aliases=['class'])
    async def classes(self,ctx):
        await ctx.channel.send("""Reminder object class is not based on how dangerous the SCP is but on how hard it is to contain. The object classes are as follows
Safe: Object class safe is classified as any SCP that does not make an active effort to escape their containment and is nonhostile to site staff.
Euclid: Euclid-class SCPs are anomalies that require more resources to contain completely or where containment isn't always reliable. Usually this is because the SCP is insufficiently understood or inherently unpredictable. Euclid is the Object Class with the greatest scope, and it's usually a safe bet that an SCP will be this class if it doesn't easily fall into any of the other standard Object Classes./nAs a note, any SCP that's autonomous, sentient and/or sapient is generally classified as Euclid, due to the inherent unpredictability of an object that can act or think on its own.
 Keter: Keter-class SCPs are anomalies that are exceedingly difficult to contain consistently or reliably, with containment procedures often being extensive and complex. The Foundation often can't contain these SCPs well due to not having a solid understanding of the anomaly, or lacking the technology to properly contain or counter it. A Keter SCP does not mean the SCP is dangerous, just that it is simply very difficult or costly to contain.
Thaumiel: Thaumiel-class SCPs are anomalies that the Foundation specifically uses to contain other SCPs. Even the mere existence of Thaumiel-class objects is classified at the highest levels of the Foundation and their locations, functions, and current status are known to few Foundation personnel outside of the O5 Council.
Neutralized: Neutralized SCPs are anomalies that are no longer anomalous, either through having been intentionally or accidentally destroyed, or disabled.
Apollyon: Apollyon-class SCPs are anomalies that cannot be contained, are expected to breach containment imminently, or some other similar scenario.""")
        await ctx.channel.send(""" Such anomalies are usually associated with world-ending threats or a K-Class Scenario of some kind and require a massive effort from the Foundation to deal with.
Archon: Archon-class SCPs are anomalies that could theoretically be contained but are best left uncontained for some reason. Archon SCPs may be a part of consensus reality that is difficult to fully contain or may have adverse effects if put into containment. These SCPs are not uncontainable—the defining feature of the class is that the Foundation chooses to not put the anomaly into containment.
If you have trouble remembering the class please refer to the locked box test:If you can lock it in a box and nothing happens it is Safe
If you lock it in a box and you are unaware of what might happen it is Euclid
If you lock it in a box and it escapes it is Keter
If it is the box it is Thaumiel
If you can't lock it in a box and it tries to end the world it is Apollyon
If you can lock it in a box but choose not to it is Archon.""")
    @commands.command(aliases=[])
    async def amnestics(self,ctx):
        await ctx.channel.send("""Both the Foundation and its predecessor organizations have relied on memory affecting agents in order to expunge sensitive data from the minds of unauthorized individuals. Though we have generally classified such agents under the umbrella term ‘amnestics’ (and less accurately, amnesiacs), we have, in fact, used a wide variety of different agents to accomplish this task.
Many of our commonly used amnestics are themselves anomalous, either in origin or mechanism. The fact that amnestics are frequently anomalies themselves effectively renders them Thaumiel class SCPs, recklessly handed out to any MTF, Field Agent, or Researcher who wants them. Furthermore, the collection of these amnestics are often either fraught with danger or are otherwise ethically problematic.
Fortunately, neuroscience has advanced significantly since the Foundation was founded, and we now have the means to mass produce non-anomalous amnestic drugs. In addition to being wholly non-anomalous, the next generation of amnestic drugs is expected to be more cost-effective for the Foundation and boast a better safety profile for their subjects. These drugs function primarily by inducing memory deconsolidation, breaking down the neural pathways responsible for encoding episodic memories. The drugs themselves are encased within specially designed nanoparticles, allowing for the targeting of specific areas of the brain, drastically reducing the amount of drug required as well as side effects.
The O5 Council is currently reviewing proposals to gradually phase out the use of traditional amnestics and replace them with non-anomalous alternatives. In order to facilitate this transition among Foundation personnel, we submit the following revisions to the current amnestics classification system.""")
        await ctx.channel.send(""" Please note that all classes of amnestics are now available in oral, inhalant, and intravenous forms for the convenience of amnestics officers, and still retain the taste of batteries and peppermint that none of us can remember but always find familiar.""")
    @commands.command(aliases=['classa', 'generalretrograde'])
    async def amnesticclassa(self,ctx):
        await ctx.channel.send("""Class A, General Retrograde
*For erasing recent and/or specific episodic memories*
While Class A amnestics will technically deconsolidate memories at random, they will mostly affect engrams within the ‘memory reconsolidation window’ of 5-6 hours, as these are the memories that will be at the forefront of the subject’s mind. This is especially true for highly unique episodic memories, such as encounters with anomalous phenomena. While these will be most effective after initial exposure, it is possible to re-open a memory reconsolidation window, allowing for amnestics officers to trigger and then erase specific memories long after their initial formation.""")
    @commands.command(aliases=['classb', 'regressiveretrograde'])
    async def amnesticclassb(self,ctx):
        await ctx.channel.send("""Class B, Regressive Retrograde
*For the incremental erasure of recent memories*
Class B amnestics start by deconsolidating the most recently formed memories first, and then working their way backwards. The extent of the memory erasure is dependent on dosage, with a 75 mg dose resulting in approximately 24 hours of memory loss on average. These are ideal for erasing recent memories older than six hours without having to trigger specific memories.""")
    @commands.command(aliases=['classc', 'targetedretrograde'])
    async def amnesticclassc(self,ctx):
        await ctx.channel.send("""Class C, Targeted Retrograde
*For the removal of specific memories from any point in the subject's life*
Class C amnestics are used in conjunction with high fidelity neuro-imaging and transcranial stimulation. Neuro-imagers will locate the specific memory engrams within the subject’s brain, and upon reaching those specific engrams the amnestics will be activated through the use of precise, non-invasive stimulation, typically ultrasound or magnetic fields.
The benefit of Class C amnestics is that they allow for the surgically precise removal of memories regardless of when they formed, and are ideal for expunging classified data from the minds of D-class personnel and neutralized humanoid SCPs prior to their release. The major drawback of Class C amnestics is the required equipment’s lack of portability. As such, Class C amnestics are most efficiently administered at Foundation sites, though mobile amnestic field clinics are currently under development.""")
    @commands.command(aliases=['classd', 'progressiveretrograde'])
    async def amnesticclassd(self,ctx):
        await ctx.channel.send("""Class D, Progressive Retrograde
*For the removal of early memories*
Class D amnestics are the opposite of Class Bs. They target the oldest memories first and work their way forward, the effects depending on dosage. As this is a fairly niche application, Class D amnestics are rarely used. Though they are, by design, more potent than their counterparts, it still requires an extremely high dosage to expunge a significant portion of a subject’s life. As such, their risk of side effects is dangerously high. It should be noted that Class D amnestics only target explicit memories. Implicit memories, namely skills that the individual learned in their youth, will remain unaffected.""")
    @commands.command(aliases=['classe', 'ennui'])
    async def amnesticclasse(self,ctx):
        await ctx.channel.send("""Class E, Ennui
*To induce psychological complacency with the anomalous*
To be frank, ‘ennui’ isn’t actually the proper term for the psychological effects of Class E amnestics. They would more accurately be considered an ‘anti-nostalgia’ drug. Though they still target the neural pathways for memories, they do not deconsolidate them. Rather, they merely weaken the pathways while disassociating the memory with any emotions, positive or negative, removing any incentive to think about it and thus allowing it to naturally decay on its own.
Class E amnestics are most effective in situations where the suppression of the anomalous is not possible, and thus in order to preserve normality, the anomaly must be perceived as normal. Class E amnestics cause subjects to accept the world as it is, and forget that it was ever any different.""")
    @commands.command(aliases=['classf', 'fugue'])
    async def amnesticclassf(self,ctx):
        await ctx.channel.send("""Class F, Fugue
*For erasing and rebuilding the subject's identity*
As with the old Class F, these amnestics induce a Fugue State, or dissociative amnesia, in the subject. The subject will forget their identity and may either be provided with a new one by the amnestics officer, or allowed to develop one on their own.""")
    @commands.command(aliases=['classg', 'gaslighting'])
    async def amnesticclassg(self,ctx):
        await ctx.channel.send("""Class G, Gaslighting
*To cause subjects to doubt the authenticity of their memories*
Class G amnestics induce derealisation of memories, making them seem fantastic or dreamlike, causing the subject to doubt their authenticity. Standard field Class-G amnestics are formulated to target memories of the anomalous, and are best administered when the subject lacks any tangible evidence of their account and targeting specific memories is infeasible. Class-G amnestics that target non-anomalous memories, however, ~~have been banned by the Ethics Committee~~ are currently under development at the request of the O5 Council.""")
    @commands.command(aliases=['classh', 'anterograde'])
    async def amnesticclassh(self,ctx):
        await ctx.channel.send("""Class H, Anterograde
*To prevent the formation of new memories*
Class H amnestics prevent the subject from forming new memories, blocking memory consolidation for as long as the agent is in the subject’s system. Duration is dependent on dosage, with 75 mg lasting for approximately 24 hours on average.""")
    @commands.command(aliases=['classi', 'transient'])
    async def amnesticclassi(self,ctx):
        await ctx.channel.send("""Class I, Transient
*For inducing a temporary amnesic state*
Class I amnestics induce transient amnesia by blocking the neural pathways responsible for long-term memories, temporarily preventing subjects from recalling their past. Duration is dependent on dosage, again with 75 mg lasting approximately 24 hours on average.""")
    @commands.command(aliases=['classw', 'classx', 'classy', 'classz'])
    async def mnestics(self,ctx):
        await ctx.channel.send("""Class W-Z, Mnestics
*Protection against anti-memetic and other mnemonic anomalies*
Classes W-Z refer to mnestic drugs, or drugs that prevent/reverse memory erasure, and are most commonly used by the antimemetics department. Though in function they are the opposite of amnestics, they both work by targeting the neural pathways for memory, allowing for the creation of non-anomalous mnestic drugs.
Class W mnestics allow the subject to perceive and retain knowledge of antimemes, in addition to general memory enhancement. Class X restores awareness of previously perceived antimemes or suppressed memories. Class Y grants the subject perfect recall for any memories gained during its period of effect, and a single dose of Class Z renders the subject biochemically incapable of forgetting anything for the remainder of their lives. Class Zs are invariably fatal, with death by seizure typically resulting in a matter of hours.
Combining amnestic and mnestic drugs is not recommended.""")
    @commands.command(aliases=[])
    async def amnesticsethicalreport(self,ctx):
        await ctx.channel.send("""Report to Overseer Council Regarding the Ethics of Non-Anomalous Amnestics
Overseers,
Though I am well aware of the numerous ethical and practical drawbacks of conventional amnestics, I regret to inform you that a previously unforeseen complication of non-anomalous amnestics has recently come to light.
The very fact that they are non-anomalous makes it possible for civilians to create their own crude amnestic drugs. How the formulas were leaked is still being investigated, but the fact remains that people are now cooking up street amnestics in improvised labs like crystal meth.
Sexual assault is, as one would imagine, the most common crime it is implicated in, but it's no doubt used to cover up all sorts of abuse; criminal, corporate, and government alike. Some people take it willingly to try to expunge their own unwanted memories, but even then the strength of the street formulas vary wildly. Individuals who overdose will end up with enormous chunks of random memories missing, sometimes crucial implicit memories and are reduced to vegetative states. Bad batches are all too common, resulting in permanent brain damage or even death. Rumours of how they are being used by numerous authoritarian regimes are rampant, but since I wasn't able to confirm any of these horror stories myself I won't bother repeating them here.
The media has dubbed this outbreak of amnestics abuse "The Forgotten Epidemic", and it's our fault. We made this stuff, and it's because of our negligence it's on the streets. Surely we have some responsibility to ameliorate this abuse. I recommend that we delay the full implementation of non-anomalous amnestics until we have determined the source of the security breach and taken measures to prevent a second occurrence in the future. The Foundation should fund the efforts of law enforcement to track down street amnestic producers, and then administer Class-C amnestics to wipe the formulas from their minds.""")
        await ctx.channel.send("""
The old amnestics may not have been perfect, but the human cost of using them has already been dwarfed by their non-anomalous equivalents. If we make it a priority, we can get this stuff off the street and bring the Forgotten Epidemic to an end.
~ Doctor ███████
Doctor ███████
Thank you for bringing this matter to our attention. As regrettable as this situation may be, the fact that these street amnestics are non-anomalous places their illicit use well outside the Foundation's authority.
By unanimous vote, the O5 council has decided that the new generation of non-anomalous amnestics will be deployed as scheduled, and that no Foundation resources will be diverted to prevent or regulate their use among civilians.
~ O5-4""")
def setup(client):
    client.add_cog(general(client))