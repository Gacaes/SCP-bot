votelog="Here are all the avalible proposals I have put forth  vote315D27,vote111H43,vote672C91,vote954E36,vote149B22,vote229K36,vote713D27,vote821C95,vote287J09,vote475D47,vote174H62,vote635U01.\nThe council proposals are as follows proposal1, proposal2, proposal3, proposal4, proposal5, proposal6, proposal7, proposal8, proposal9, proposal10, proposal11.\nThe SITE-WIDE MAYDAY BULLETINs are as follows. BULLETIN1, BULLETIN2, BULLETIN3, BULLETIN4, BULLETIN5, BULLETIN6, BULLETIN7"
vote315D27="Input: SCP-1773's containment procedures\nOutput: Once per second week dust may be placed in the middle of them to donate more beautiful functions of the hallway.\nProposal by 05-01: Amend SCP-1773's containment procedures to include the placement of ten grams of dust in its container every two weeks.\nVotes\n05-01 Yea\n05-02 Nay\n05-03 Abstained.\n05-04 Yea\n05-05 Yea\n05-06 Yea\n05-07 Yea\n05-08 Yea\n05-09 Yea\n05-10 Yea\n05-11 Yea\n05-12 Yea\n05-13 Abstained.\nStatus Approved\nNotes: No changes were noted in SCP-1773's behavior or properties. However, researchers responsible for SCP-1384 reported that it took three steps backwards on 3:22 PM 15 February (the time SCP-1773's documentation was updated)."
vote111H43="Input: SCP-3034's containment procedures.\nOutput: No person who is a small shape and is only a child will be given a level one security clearance regardless of apparent awareness of foundation mismanagement\nProposal by 05-04: Amend SCP-3034's containment procedures to explicitly ban children from the site.\nVotes\n05-01 Abstained\n05-02 Nay\n05-03 Abstained\n05-04 Yea\n05-05 Yea\n05-06 Yea\n05-07 Yea\n05-08 Yea\n05-09 Yea\n05-10 Yea\n05-11 Yea\n05-12 Yea\n05-13 Abstained\nStatus Approved\nNotes: N/A"
vote672C91="Input: N/A\nOutput: Site-13 is to appear someplace else on planet, encompassing white male counterparts that drawn to empty flagstones and the gun noises in their own blood.\nProposal: As there is no evidence of a Site-13 ever having been constructed by the Foundation, the O5 Council was unable to infer any proposed action from this output.\nStatus Denied\nNotes: Five days after this proposal was provided, SCP-1730 manifested."
#these are what I mean
#what the script is gonna do is create a cog called general
#then create commands under that cog category called each of these variable
#i.e. there will be a command called vote672C91 which contains that variable's string data. its basically an easier way of doing this
#what was wrong with having everything under gen cog?
#look at the state of it
#it looks liek shit and you also said that that's not everything that you need to make. making this system im doing, will allow you to just copy and paste the articles from the scp wiki and just paste them as is into a file and the script will sort out the rest
#so i wouldnt have to like manually put the \ before "'s and shit?
#no, thats just basic python programming syntax, youll still have to do that. this just means that if you wanna create a command in the general cog all you have to do is this:
#test_command='this message will be sent to discord when this command called test_command is called and you wont have to fiddle around with making a command for it manually like you were doing in the original general.py'
#if i dont make a cmd for it how tf is it gonna be called
#that is the entire reason why im making this script, so you dont have to make the command yourself, the script makes it for you.
#but the cmd is just the same thing each time
#huh, be more specific, ive no idea what you mean by that.
#ive just been copy pasting  
#@commands.command(aliases=['dossier05-03'])
#    async def dossier0503(self,ctx):  
#        await ctx.send
#yeah, which is ugly and tedious
#o-oki

'''
#instead of having to do this:

class test_cog(commands.Cog):
    def __init__(self,client):
        self.client=client
    @commands.Cog.listener()
    async def on_ready(self):
        print('test_cog Cog Ready')

    @commands.command()
    async def test_command(self,ctx):
        await ctx.channel.send("this is the output for the test command")

def setup(client):
    client.add_cog(test_cog(client))

#all you'd havve to do is this instead:
test_command="this is the output for the test command"
'''