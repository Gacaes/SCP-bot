import discord
from discord.ext import commands

class dossier(commands.Cog):
    def __init__(self,client):
        self.client=client
    @commands.Cog.listener()
    async def on_ready(self):
        print('dossier Cog Ready')

    @commands.command(aliases=['05dossier'])
    async def commanddossier(self,ctx):
        await ctx.channel.send("""~~You do not have access to this file. Please standby while a member of the sites MTF unit grabs you~~ ERROR MANUAL OVERRIDE ACTIVATED
Look I dont know who you are okay but I just saved your life. I've not the slightest idea as to why you're trying to look into the 05 but I don't have long left. I'm giving you all the info I've collected. Godspeed.
The O5 Council. O5 Command. The Overseers. Overwatch.
These are the people who have ultimate control over the Foundation.
Each O5 member knows almost everything there is to know about the Foundation and its activities. Between them all, they know every single secret that the Foundation holds.
Most Foundation personnel spend their entire careers without seeing them. Members below Clearance Level 2 don't even know they exist. Most people outside the Foundation have never heard of them, or don't think they are real.
Most everyone is afraid of them. An O5 walks into a room, and everyone pisses their pants. That's what happens when you hold supreme power over one of the scariest organizations in world history.
This dossier will show you contradictory reports on each of the O5 Council members.
My research has been comprehensive, but the very nature of my enemy makes it impossible to know which answer, if any, is true.
There seem to be thirteen members of the O5 Council, although even that is questionable. Perhaps there are multiple individuals sharing each O5 number. Perhaps dozens. But perhaps there is only one. Perhaps only one of each of the reports are true, or all reports are different facets of one person, with stand-ins and disinformation stirred in.
Perhaps none of these are true. The end of this dossier presents well-sourced reports that question the veracity of almost every single assumption made here. You must judge carefully.""")
    @commands.command(aliases=['dossier05-01'])
    async def dossier0501(self,ctx):
        await ctx.channel.send("""O5-1: "The Founder".

Male. European descent. American origin. Verified post-human lifespan; 148+ years of age. Varying appearance.

A holdover of the occult organizations preceding the Foundation, so he likely benefits from more preservation techniques than merely SCP-006, and he likely possess a large degree of anomalous protection. References have been made to him being "clad in the rags and bones that hadn't been used to mark the other 12"; occult significance obvious.

One possible identity for the original Administrator, although various other reports assert that the Administrator was a separate individual ("F. Williams").

Evidence strongly suggests that he was born in the late 1800s (possibly 1866) as " Aaron Siegel". Certainly, one Aaron Siegel was a physicist studying at Cornell University in 1891, disappearing from the historical record in this year. This timeline doesn't match what we know of O5-1's activity, but given his position and the reality-restructuring events that have occurred, it's entirely possible.

Rumor has it that he's Gears' father. If true, this would make him the Black Queen's grandfather — my grandfather.

May have gone missing according to some reports, current location unknown. Possibly deceased.

Two contradictory sightings stand out. Once in company of O5-2, appearing as an extremely old man. Once in what appears to be security footage of an underground bunker, appearing as a young teenager.


"The Swallowed Tail" source also identifies O5-1 as "Aaron Siegel", describing him as a Caucasian male, apparently in his mid-30s. Concurs with previous descriptions of O5-1 as a Cornell University Physicist and a founding member of the Foundation. Claims that O5-1 has become less active within the Foundation over time, rarely (if ever) leaving Overwatch Command (location unknown). Rumored to be deceased, but still votes in council meetings. Possibly the same individual as another O5-1, the "Man with the Infinity Gun".""")
        await ctx.channel.send("""

O5-1: "The Man With The Infinity Gun".

Male. European descent. Spanish origin. Not seen since 03/22/1926.

Previously a high-ranking official in a pre-Foundation supernatural study organization, and former head of command research team Omega-5, assigned to the "Twins of God" top secret project at San Marco, Mexico. Participated in the construction of "The Children", a cosmic superweapon designed to eliminate the Group of Interest "Kingdom of Abaddon", a community of hostile reality-altering entities located in North Africa.

Murdered the first Foundation Administrator ("Frederick Williams") and stole the trigger for the weapon, before fleeing and disappearing along with a substantial number of high-ranking staff members. May have founded the Chaos Insurgency Group of Interest (possible link to their leader, "The Engineer"?), although this connection is unsubstantiated beyond a single dubious source.

Motives for defection remain unclear. Not currently believed to be alive, though it is possible that he has discovered other means of prolonging his life. If alive, possesses the ability to immediately annihilate anything, anywhere in the universe, at any moment. Exceptionally dangerous.

O5-1: "The Dead Man".

Male. Unknown descent. Unknown origin. Rarely, if ever, directly seen.

The oldest surviving founding member of O5 Command, O5-1 is technically dead. He survives only due to anomalous alteration and sheer willpower; his body is a mummified corpse, and he should biologically be brain-dead.

Never appears in public. When public appearances are necessary sends a stand-in. Works exclusively through intermediaries. Has a somewhat frightening reputation; the other O5 Council members seem to be afraid of him.

O5-1: "Eve".

Female. African descent. Ancient Sumerian origin. Verified post-human lifespan; claims to be 10,000-15,000 years old. Varying appearance.

Claims to be "Adam's third wife." Claims to be the mother of modern humanity.""")
        await ctx.channel.send(""" Possible mother of SCP-076-2 and SCP-073. Claims that she (and Adam) were not the first humans, but merely the leaders of the first agricultural humans (possibly; reported details vary), who brought humanity from the Garden of Eden.

Claims that Adam was (or became) a reality bender, but that she herself is not. Rather, she possesses protection from reality restructuring via "anchors" (like a few Foundation personnel, including the current Administrator and Dr. Alto Clef). Reference: SCP-1000, SCP-2932, and reality restructuring cascades.

O5-1 is a reluctant founding member of the SCP Foundation. As one of those who led humanity from the Garden, she felt responsibility for helping to guide humanity through the uncertain future ahead. Reports suggest she may often disagree with the rest of the O5 Council.

Despite that fact that they seem to share an O5 number, several reports that reference "Eve" also reference "The Founder" as existing together, and reference their acrimonious interactions.

She seems a curious character. If she's real, I'd like to meet her. Maybe befriend her. Maybe kill her.

O5-1: "The Visionary".

Male. European descent. British origin. Appears to be about 55. Formerly affiliated with Her Majesty's Foundation for the Secure Containment of the Paranormal. Signatory and initiator of the Forbidden City Convention.

A principle believer of the Foundation's formation "by God's will". Religious backing or disinformation?

May have strong-armed other precursors into forming the Foundation under threat of annihilation? But why those other organisations specifically? What do they possess?""")
    @commands.command(aliases=['dossier05-02'])
    async def dossier0502(self,ctx):
        await ctx.channel.send("""A note on O5-2.

O5-2 is usually reported to possess certain… unique anomalous traits. As you will see from the following reports, there is an odd sort of consistency in between the vast contradiction. Consistency is unusual for O5 member reports. Possible sign of a disinformation campaign… or a very strange truth. Perhaps I know which, but I could not tell you.

O5-2: "The Gardener".

Female. European descent. American origin. Appears to be 80+ years old. Actual age unknown. No unusual appearance, but rarely seen without a shawl, gloves and hat.

O5-2 is apparently a second version of Foundation Director Dr. Sophia Light, a holdover from an erased timeline (she seems to have had a hand in this erasure). She is very different from the current Sophia Light, Director of Site-41, who is unaware of her alternate's status or identity. Considered extremely dangerous, even compared to the other O5s. Known for making tough, pragmatic decisions, but also said to have a grandmotherly attitude and appearance.

Promotes research of SCP objects and the anomalous in general. Has consistently stuck to this despite regularly shifting Foundation attitudes towards containment versus research. Pushed for a reasonable degree of anomalous object cross-testing. Implemented higher standards of non-SCP anomalous item categorization by the Foundation. Strong believer in pragmatic research (or theoretical research that leads to pragmatic work), believing this to be most beneficial to the Foundation in the long run. Wishes to deconstruct the anomalous so that the Foundation understands it.

Rarely seen in public. According to some sources, she's always accompanied by an elderly man - may also be an alternate version of a current Foundation employee?

Maintains several SCP objects considered key to O5 Command, notably SCP-006.

O5-2: "The Nazarene".

Female. Middle Eastern descent. Israeli origin. Varying appearance; often passes for male.""")
        await ctx.channel.send(""" Possesses injuries consistent with crucifixion (notably distinct scars at wrists and feet, marks of whipping, etc).

O5-2 is apparently a version of Foundation Doctor Sophia Light, either a holdover from an erased timeline, or, perhaps, the original version of Sophia Light (making the publicly known version a duplicate, or the same person from earlier/alternate timeline). She appears to be similar to the publicly known Sophia Light in personality and appearance (with the exception of ethnicity), but otherwise differs due to extensively differing life experience. The publicly known Sophia Light is unaware of her alternate's status or identity.

O5-2 possesses various reality-bending capabilities, the extent of which is currently unknown. May have some claim to divine status.

Recovered Data File L246-A1780B23971C20987D091


"The Swallowed Tail" source claims that her title is linked to her scars (usually concealed by black gloves) and a bizarre rumour that she was crucified as Jesus of Nazareth. Generally appears to be in her mid 20s, but sometimes looks much older. Closely associated with O5-1 "The Founder", and never seen apart from him. May once have been the head of the Foundation's Department of Morality, the precursor to the Ethics Committee.

O5-2: "The Way".

Male. European descent. American origin. Appears to be 50+ years old. Actual age unknown. No unusual appearance.

O5-2 is apparently a version of Foundation Doctor Sophia Light, either a holdover from an erased timeline, or an immigrant from an alternate timeline. He resembles an the current Sophia Light in every way except his gender, age, and first name: "Stefan".

He travels everywhere with a similarly unusual secretary/bodyguard, who he seems to be in a romantic relationship with. She is named Tracy Lament, and appears to be a version of Foundation Agent Troy Lament, and coming from the same origin as O5-2.

Neither Dr. Light nor Agent Lament are aware of their doubles' identity or status.""")
        await ctx.channel.send("""

O5-2 has pushed repeatedly for a particular sweeping change to Foundation policy: that anomalous objects which become fully understood by the Foundation be universally declassified and introduced to the non-anomalous scientific community (even those alien to current standards of normalcy and established scientific principles). So far, he has met with little success in this endeavor, due to strong opposition from other members of the O5 Council.

O5-2: "He Who Waits".

Male. European descent. French origin. Appears to be about 60. Formerly affiliated with Estate noir. Signatory of the Forbidden City Convention. DNA tests indicate that he is apparently an ancestor of Sophia Light.

Proposed an anomaly progression model based on the second law of thermodynamics, which was rejected by the other members of the O5 Council. Since their first known meeting, has usually voted 'Abstain'.

Coined the term 'Keter'. Contrary to the common translation of 'crown', "He Who Waits" coined 'Keter' in the context of 'wait'. Waiting for what?

An excerpt from a document authored by O5-2 is as follows:

…Until then, there will be chaos in the system. Once, I proposed that we guide the world back to its original state but the others disagreed in favour of establishing tyranny…

'disagreed in favour of… tyranny' –> insurgency

Possible Chaos Insurgency member/founder/sympathiser? More research needed.

O5-2: "The Archivist".

O5-2 is an artificial intelligence.

According to some reports, O5-2 was assembled by the other members of the Foundation using Mekhanite technology. This O5-2 was valued for his analytic and mathematical ability, and served as a voice of restrain and reason on the Council, but was never fully trusted by the other Council members.

More recent reports confirm that an artificial intelligence is still on the council as O5-2.""")
        await ctx.channel.send(""" It is unclear if this actually is the same entity as the original O5-2, although if it is, more advanced technology has likely been incorporated over time.

References have been made to this version of O5-2 as "Sophia", a name with historic significance to the Mekhanites as an mechanical prophet who betrayed the Church to join with its enemies.""")
    @commands.command(aliases=['dossier05-03'])
    async def dossier0503(self,ctx):
        await ctx.channel.send("""05-03: The Kid
Male (?). European descent (apparently). Unknown origin. Appears to be 17-19, despite being certainly much older. Always has long blond hair, glasses, patched jean jacket, and a single bone earring. Never seen in person; communicates via computer terminal.
Usually presents as male, sometimes as female, sometimes non-binary/other. Never explains this. An informant suggested to me that it's a computer error; I find it hard to believe it's not on purpose.
Original identity unknown. Various intelligence reports claim that he (?) is actually dead, and only exists in the computer matrices he created as an artificial intelligence. Excessively friendly in personality. Usually. A relatively active O5 member at certain Sites.
Assorted rumors hold that O5-3 is the brother of SCP-2772 (probable), and may have helped invent the Internet in the 1960's (unknown).
May have never been human - possibly an artificial intelligence referred to in Foundation documentation as the "All-seeing Eye".
"The Swallowed Tail" source connects "The Kid" with an image of dubious provenance depicting a Korean child, but regards this image with skepticism. True appearance of O5-3 unknown.
O5-3 is reportedly the head of the Foundation's Recordkeeping and Information Security Administration, managing all of the Foundation's digital records. Appears to be capable of predicting future events, including extranormal ones. Is this just a matter of having all of the data, or are anomalous means being used?
05-03: The Philosopher Scientist
Male. East Asian descent. Japanese origin. Appears to be 60+ years old. Actual age unknown. No unusual appearance.
Joined the O5 Council in in the 1930's, shortly after World War 1. Known for caring about the social ramifications of science; strongly opposed social Darwinism.
Generally a voice of caution; the conscience of the O5 Council, even if often overridden by other members, and even if often endorsing Foundation projects he does not fully agree with.""")
        await ctx.channel.send("""
Helped found the Ethics Committee. Possibly still plays a lead role in the organization (if it even exists).
While already an O5 Council member, gained a PhD in clinical psychology. Was the original person responsible for implementing psychological checkups of Foundation personnel.
05-03: The Beacon/nMale. European descent. American origin. Appears to be 50+ years old. Actual age unknown. Varying appearance.
Made a lifelong study of various methods of controlling large groups of people. A particular fascination with religion and religious cults. Convinced by other O5 members to investigate making large groups of people profitable as well.O5-3 is particularly shrouded in myth. He is presented as a literal supernatural figure in some reports, and as a perfectly ordinary man in others. Ordinarily, this could be chalked up to religiously related manipulation, but as an O5 member, some claim to divine status cannot be discounted.
Possibly connected to L. Ron Hubbard.
05-03: The Hermit
Male. European descent. Russian origin. Appears to be about 80. Has a prominent beard. Formerly affiliated with the Tsars' Seers. Signatory of the Forbidden City Convention.
Bends to consensus decision easily, even if said consensus decision is not originally his choice.
Only directly interacts with other O5 Council members. Uses written messages to convey orders to subordinates. Known to consistently stay in Overwatch HQ. Potential secret-keeper?""")
    @commands.command(aliases=['dossier05-04'])
    async def dossier0504(self,ctx):
        await ctx.channel.send("""05-04: The Ambassador
Male. Australian (Koori) descent. Canadian origin. Mid-40s. No unusual appearance. Assigned female at birth.
Former Foundation field agent. Many recorded sightings; unlike all other members of O5 Command, commonly interacts with agents or representatives of outside anomalous groups of interest.
He also works with the Administrator in a more traditional ambassador role, privately meeting with heads of state and high-tier organizations such as the Global Occult Coalition/United Nations to negotiate such matters as Foundation access to countries. Has a sizable staff of diplomats working under him.
Allegedly capable of traveling vast distances in an impossibly short time - apparently by foot. Surprisingly open about personal details, but the details of this ability are kept under wraps.
Pertinently: How does he keep finding me? And why doesn't he share that with the rest of the Foundation? Possibly bound to an esoteric/anomalous rule-set. Requires investigation.
Excerpt from intercepted communication:"A lot of fieldwork and being in the wrong place at the right time. Got to be a little bit of a diplomat, and ended up getting sent out to talk to various GOIs over the years. Got pretty good at it. Too good, really.
Another of those who ended up being promoted because he's so damned good at his job, but not entirely trusted, because he walks places people shouldn't go, and keeps secrets.
His loyalty isn't in doubt. Just the wisdom of his excursions."
"The Swallowed Tail" source also depicts the Ambassador as the public face of the Foundation, but differs on all other details. Described as a Persian male, Iranian/Armenian ancestry, early-thirties, originally a French stage actor known as Jean Lemieux Betrand, born Jean Ebrahimi.
Allegedly "anomalously charismatic", but there's no evidence that he's anything more than a pretty face. Defers to O5-7 "Green".""")
        await ctx.channel.send(""" Loyalty to the Foundation is questionable - possible weak link?
05-04: The Martyr[DECEASED]
Male. European descent. American origin. Early 40s. No unusual appearance.
Gained his position when forced to execute a prior O5-4 during an attempted hostile takeover of the Foundation. Held the position reluctantly. Later died under highly classified circumstances. Publicly, at least, said to have died a hero's death. I suspect otherwise, but the reports claim he was genuinely grieved, so perhaps true.
05-04: The Frost [DECEASED]
Male. European descent. American origin. Early 40s. No unusual appearance.
A relaxed, gentle man, despite his stern reputation. Not shy about appearing in public, or publicizing his projects. Kept up impressive security measures to counter this. Known for traveling with a large, friendly mastiff named (almost comically) "Rover".
Did not reflect the mindset of his compatriots regarding use of anomalous objects. Strongly opposed the weaponization of SCP objects. One of several O5 Council members who strongly opposed cross-testing and in many cases general research on the anomalous as well.
Came into his own after the series of incidents that included SCP-076 causing the destruction of Area-25 and MTF Omega-7, Dr. Kondraki mostly destroying Site-19 by deliberation of breaching 682 in reaction to manipulation by O5 members, a researcher wiping himself and several sites from existence, and a string of serious accidents resulting from cross-testing SCP objects.
Following these incidents, O5-4 and his newfound allies within O5 Command found their position suddenly quite popular indeed. A great number of projects were outright ended, and a new policy came into effect: little research on anomalous objects should be done except that which is necessary for containment. Research was considered too dangerous. SCP objects would be examined mostly in isolation from each other. Cross-testing mostly ceased.""")
        await ctx.channel.send(""" This would be unofficial Foundation policy for the better part of the following decade.
O5-4's sway began to fail in more recent times, and then he was abruptly assassinated by operatives of the Chaos Insurgency. (In practice, this could mean almost anything, given the nature of the Insurgency.)
05-04: The Collecter[OUSTED]
Male. Descent unknown. Origin unknown. Age unknown. Appearance unknown.
O5-4 was the first to personally succeed in bringing a complete series of Little Misters into Foundation containment, and became Mr. Collector, allegedly with assistance from the discontinued Mr. Red. Now contained as an anomalous individual, and so removed from the O5 Council.
05-04: The Gangster[DEFECTED]
Male. European descent. American origin. Appearance unknown.
O5-4 played a large role in Foundation manipulation of world governments and economic systems. Additionally, he had extensive ties to organized crime and domestic terrorism, ties which existed before his elevation to the O5 Council. He simply never let them go, and the obvious utility of crime connections during the Foundation's early years allowed him to justify these questionable continuing relationships. Most people who the Foundation "disappeared" or assassinated during their formative years were targeted under the auspices of O5-4.
Helped design the first iteration of the Chaos Insurgency (as a Foundation black ops project) before defecting with the fully realized Chaos Insurgency during the Foundation Civil War. Although not a mastermind of the "true" Insurgency (better thought of as an alliance between then-O5-7 and then-O5-11), is likely significantly responsible for its success post-schism, for when he left, he took his connections with him.
When O5-4 defected, the Foundation wiped out all his operations and reassigned or terminated his remaining staff. Though this was likely a good choice for them long-term, this partially contributed to certain destabilizations in world economies of the time.""")
        await ctx.channel.send("""
Rumored to have known Al Capone and a number of other crime lords personally.
05-04: The Veteran
Male. European descent. German origin. Appears to be about 50. Has a prominent mustache. Formerly affiliated with the Imperial German Anomalous Matters Examination Agency. Signatory of the Forbidden City Convention.
Believed to have fought in the Fifth Occult War on behalf of the German Empire, and defeated the Militia United in Righteousness (a.k.a. the Boxers). Professes unusually detailed knowledge of Daevite and Mekhanist military tactics.
Claims to have met Napoleon Bonaparte in person, although he claims that the iteration of Bonaparte whom he met is anomalously enhanced.
Likes to join agents and Mobile Task Force members during field operations. Restless and does not like desktop jobs.""")
    @commands.command(aliases=['dossier05-05'])
    async def dossier0505(self,ctx):
        await ctx.channel.send("""05-05: Blackbird
Male. European/Middle Eastern descent. American origin. Appears to be mid-40s; almost certainly older. Favors tweed suits, usually worn with coat and a hat with a blackbird pin. Wears ties with birds. Blackbirds seem to be some sort of personal motif - unknown significance, if any.
Overly friendly and familiar in demeanor. Tends to be laid-back and jovial given the option. One of the more prominent O5s, relatively often seen in public. Little is known about his specific role, though he has been on the Council a long time.
An artist of some talent; known to sketch five blackbirds as a signature.
"The Swallowed Tail" source describes "Blackbird" as the head of the Department of Paranormal Organisation Review, which records and monitors the Foundation's "Groups of Interest". Also takes an interest in anomalies interacting with alternate realities. Subordinates report overhearing him talking to himself, and acting like different people at different times.
This individual seems to always occupy a prominent position within an organisation focused on the anomalous, even in realities in which he isn't a member of the Foundation. He can be bargained with, but do not underestimate him. He may well be the most dangerous member of the O5 Council.
05-05: The Ordinary Man
Male. European descent. American origin. Appears to be mid-40s. Appearance is thoroughly ordinary; prefers to appear average in almost every way. Exception: Almost always seen wearing tanned leather shoes.
Very little knowledge is available about O5-5. Has been known to occasionally travel with SCP-108 for unknown reasons. Given experimentation records on 108, I suspect he may intend to use her (either directly or via research) as some form of last-ditch escape route.
05-05: The Entrepreneur/The Treasurer
Male. European/Middle Eastern descent. Western European origin. Mid-40s. No unusual appearance.
O5-5 oversees the Foundation's front organizations.""")
        await ctx.channel.send(""" He creates funding for almost all Foundation projects. Habitually manipulates economies to the Foundation's benefit. He doesn't accomplish this directly by anomalous means; yes, the Foundation could just make gold, but then injecting large amounts of gold into an economy would tend to destabilize it. O5-5 doesn't just run the front organizations, he makes them profitable. Others hire the workers, O5-5 pays them.
Never seen in public. Many reports identify him as the same person as O5-5 "Blackbird", and others call "Blackbird" a fiction or a false double.
05-05: Manifest Destiny
Male. European descent. American origin. Appears to be about 50. Clean-shaven. Formerly affiliated with the American Secure Containment Initiative. Signatory of the Forbidden City Convention.
A firm believer in human mastery over Nature. Involved in the decimation of SCP-2750.
Makes frequent trips to Yellowstone Park. Purpose unknown.
05-05: The Black Cat
Apparently, O5-5 is a black housecat. This version of O5-5 is generally disguised as some sort of companion animal for a decoy O5-5, but behind closed doors the Black Cat is in charge.
I'd dismiss this as an obvious falsehood, but I have a friend with a similar appearance, and it hasn't stopped her from becoming a major figure in the Serpent's Hand. I'd say this couldn't happen in the Foundation, but if they kept Kain "Pathos" Crow around despite him being transformed into a dog, I suppose anything is possible…""")
    @commands.command(aliases=['dossier05-06'])
    async def dossier0506(self,ctx):
        await ctx.channel.send("""05-06: Cowboy/The American
Male. European descent. American origin. Mid-40s. Long hair kept in a ponytail. Nearly always dresses in white suits, with a white Stetson "Boss of the Plains" cowboy hat, and carries a white cane with the handle carved in the shape of a wolf's head. Unknown significance, if any.
Former top Foundation field agent; other details of prior identity unknown (probable wipe) but he may be a member of the Bright Family. Professional yet genial. Reputation for high competency. Plays something of a "jack of all trades" role within the Foundation, but focuses particularly on issues of Foundation security.
One of the O5s seen more often in public. Travels with two male bodyguards referred to as "Thompson" and "Black".
"The Swallowed Tail" source indicates that "The American" was once known as Rufus King, a Union Brigadier General and Minister to the Papal States before joining the Foundation. Now serves as "Special Council to the Joint Chiefs of Staff", liaison between the Foundation and the Pentagon. Has authority just below (or just above?) that of the US President. Commands the Foundation's Department of Applied Influence (Private Army), alleged to have founded Mobile Task Force Alpha-1 "Red Right Hand". May have been involved in the creation of Mobile Task Force Omega-7 "Pandora's Box" at the behest of General Bowe, despite initial opposition to this project.
Prioritises American interests. Arrogant, often overconfident. Skilled with a whip.
Appears to be in his mid-fifties, but for his military record to be true he'd have to be the oldest Council Member, with some way of extending his lifespan even before joining the Foundation. This is either a blatant fabrication by someone who couldn't even get the dates right, or worth looking into further.
05-06: The Figurehead/The Elder
Male. African descent. American origin. Verified post-human lifespan; likely 200+ years of age.""")
        await ctx.channel.send("""
One of the founding members of the O5 Council, O5-6 was already old when he joined. He is now said to have aged beyond even the abilities of SCP-006 to rejuvenate him. He still survives, for now, but he rarely if ever takes any action on the O5 Council. His secretary runs things for him, up to and including voting according to his wishes on O5 Council matters.
05-06: The Puppet
Male. European descent. American origin. Early 40s. Typically dresses in tasteful suits.
Rarely seen in public, but a very active member of O5 Command internally. What few are aware of is that he is a puppet inserted into the O5 Council by the Global Occult Coalition as a possible future attempt at a hostile takeover, or perhaps a failsafe.
It seems possible that some or all of the other O5 Council members are aware of his status as a turncoat, and tolerate the situation for their own reasons. Perhaps they view him as a potential asset or at least view the knowledge of his situation as a potential asset.
05-06: The Experimenter
Male. European descent. Austrian origin. Appears to be about 65. Formerly affiliated with the Imperial Commission on Transgressive Occurrences. Signatory of the Forbidden City Convention.
Advocates for scientific methodology within the Foundation. Chiefly in charge of R&D. Coined the terms 'Euclid' and 'trans-reality memory retention'.
What exactly is trans-reality memory retention?""")
    @commands.command(aliases=['dossier05-07'])
    async def dossier0507(self,ctx):
        await ctx.channel.send("""05-07: Green
Female. South Asian descent. Unknown origin. Appears to be mid-40s; almost certainly older. Somewhat overweight. Nearly always dresses in various shades of green clothing. Unknown significance, if any.
One of the longer-term members of the O5 Council. Described as not especially morally scrupulous with her power, although with her heart in the right place, or at least near the right place. A master tactician, charismatic and dangerous.
Does not often appear in public, and often works through intermediaries at first; a believer in private meetings over public speeches. Generally friendly in demeanor in personal interactions, right up until she's not.
Possibly an ex-university professor (surprisingly). Has implemented a number of training programs in various areas across the Foundation.
Also notable for "adopting" Dr. Alto Clef and approving a number of his experimental (and sometimes unnecessarily dangerous) projects.
Takes an active interest in Foundation personnel; often plays a role in recruiting O5 Council general staff. Also plays an active role in the development of experimental and even anomalous weaponry.
"The Swallowed Tail" source identifies a somewhat similar O5-7. "Green" or "Flytrap" is described as a Caucasian female of British/German ancestry, appearing to be in her early fifties. Nickname comes from her green pantsuits.
Believed to have had a long career within the Foundation before being voted onto the council, possibly as the first replacement of an original council member. Ruthlessly pursues her (unknown) goals, de facto leader of the O5 Council as long as O5-1 does not exercise veto power. Her appearances are a source of dread for those outside of the Foundation, who describes her as "The Devil" or "The Spider". Despite her reputation, she does not appear to possess any anomalous abilities.
05-07: The Unlikely
Male. European descent. American origin. Appears to be mid-40s; likely older. No unusual appearance.""")
        await ctx.channel.send("""
Reputation for being somewhat dangerous to be around. Has survived a curious number of assassination attempts unscathed (with the assassins dead in the wake of the attempts); unusual that an O5 would both leave themselves vulnerable to so many attempts and also survive so many in such a manner. Possible anomalous protection.
Takes a special interest in SCP objects stolen or acquired by the Chaos Insurgency. Numerous reports indicate that O5-7 is, in fact, the current head of the Chaos Insurgency, despite this directly contradicting many other reports about the Chaos Insurgency's status as a splinter organization. Reports differ on whether the rest of the O5 Council is unaware of this, or knows and partially or fully endorses it.
05-07: The Professor/The Heretic[DEFECTED]
Male. European descent. American origin. Appearance unknown.
A professor at a major university and a trained psychologist; held the former position even while a member of the O5 Council, before disappearing from both upon defection. Developed a large number of training programs across the Foundation, many of which are still in use today in some form.
One of the primary instigators of the Foundation Civil War. Defected from the Foundation along with the then-current O5-4, O5-11, and O5-12, as well as a number of Foundation generals and another O5 who was killed during the schism.
A major thought leader in the Insurgency; possibly co-created the first iteration of the Insurgency, which seems to have been originally an organization used for covert Foundation operations under another (relatively nonsensical) name, and likely still exists in this form as well as the latter-day article. Embraced the name "Chaos Insurgency" as legitimate during the schism; is likely the reason the Chaos Insurgency is called the Chaos Insurgency. Apparently still active in the Insurgency to this day.""")
        await ctx.channel.send("""
Advocated for research into numerous venues the rest of the O5 Council deemed too dangerous to touch, including chaos magics and a reality-warping god-engine (both in current use by the Chaos Insurgency today). Advocated for large-scale weaponization and active use of SCP objects. Spent an inordinate amount of time researching the brain structure of anomalous humanoids.
Foresaw the increase in anomalies that was only beginning to be experienced by the Foundation (and general anomalous community) of the time; expressed that to survive, the Foundation would need move from merely preserving normalcy to actively determining normalcy, and determining the future for the human race at large.
Accused of having a 'god complex'; took these accusations as a compliment. Took the position that God was missing or dead, and therefore the Foundation needed to take his place. A line often quoted by his supporters: "Heaven is empty, and all the angels are here."
05-07: Teeth
Agender. East Asian descent. Chinese origin. Verified post-human lifespan. Appears to be mid-40s; almost certainly older. Androgynous appearance (in normal form). Always wears two ivory hair-sticks. Reports claim these were fashioned from human teeth/bone; obvious occult significance.
Unusually for an O5 Council member, it seems unclear whether O5-7 was originally fully human. They possess the ability to shift between a human form and a variety of difficult-to-describe eldritch beings. They are supposedly involved in the containment of (and maybe collaboration with) certain "extraplanar" entities beyond Lovecraft's weirdest dreams.
This is an unusual set of reports. This O5-7 is supposedly both very human (hard to get more specifically human than all those culturally specific details), and yet supernatural to an extreme degree. The consistency in the reports has disturbing implications about the Foundation's hidden activities, even if this O5-7 is a cover for someone or something else.""")
        await ctx.channel.send("""
05-07: The Cardinal
Male. European descent. Catholic. Appears to be about 70. Formerly affiliated with the Royal Office for Christian Artefacts, a splinter organisation from the Vatican Holy Office for Secrets and Prophecies. Signatory of the Forbidden City Convention.
Opposed Foundation attempts to enforce control over the Middle East during the early 20th century, citing that "it is already taken care of". Possible foreknowledge of ORIA or an equivalent organisation?
05-07: The Immortal
Male. Australian. Biologically 58 years old. Former Prime Minister of Australia, Harold Holt. Currently contained as SCP-3477-3. Joined the O5 Council in 1967 as a ploy to gain access to SCP-006, in an attempt to achieve immortality. One of the only O5s to be directly recruited from the civil sector.
Attempt was successful until the sudden appearance of several more individuals claiming to be Harold Holt, at which point he was stripped of all authority and given an SCP designation. Was within containment for 46 years, until all Harold Holts staged a containment breach.
Evidence suggests there may be as many seventy-seven different versions of Harold Holt, each with their own form of immortality. Reason for this unknown. Possibly a quantum collation of different outcomes, a deliberate attempt at creating many versions to guarantee at least one would survive, or an example of a multiverse collapse.""")
    @commands.command(aliases=['dossier05-08'])
    async def dossier0508(self,ctx):
        await ctx.channel.send("""05-08: The Newbie/The Lesser
Male. European descent. American origin. Mid-30s. No unusual appearance.
A former Foundation Site Director; a recent elevation to the O5 Council (between 6 and 9 years as of 2014).
One of his first actions as an O5 Council member was to approve of Dr. Kondraki's plan to neutralize the former SCP-083. This plan resulted in the breaching of multiple SCP objects, including Kondraki deliberately breaching SCP-682, and in the near destruction of Site-19. This incident appears to have lead to the O5-ordered assassination of Kondraki by Dr. Gears.
Though he was not removed from the O5 Council over this, O5-8 never recovered, and is now much more cautious. Still shaken from the fallout of the incident, he continues to rely on support staff to accomplish all of his duties — including the hiring and replacing of support staff.
Thus far, O5-8 has avoided further serious incidents, but rumor has it that the situation with his current crop of staff is unstable and likely to cause further "mistakes".
Possibly assassinated. Has not appeared in public for some time.
"The Swallowed Tail" source claims that the title of "The Lesser" refers to the American industrialist Baron Leeman Hoadley, much diminished in influence following the death of his brother and the loss of his vast fortune.
Recent physical descriptions are hard to come by, since he rarely leaves his personal estate - apparently out of fear of the other Council members. Reportedly obsessed with self-modification through the use of anomalous items, current capabilities unknown.
05-08: Magnolia
Female. European descent. Appears to be mid-50s; likely older. Deliberately not beautiful in appearance.
O5-8 is known for being brutal and harsh, though never arbitrarily; known for making hard decisions. Known to have played a deciding vote in the decision to nuke several significant Foundation Sites during a particularly deadly breach.
Her physical appearance is deliberate.""")
        await ctx.channel.send(""" Overseers certainly can alter their appearance if they wish. This seems to be due to an emotional state plagued by guilt. Considered vulnerable to assassination attempts due to rumors that she would welcome them.
Wears a ring of human sinew. Occult significance obvious.
Possibly assassinated. Has not appeared in public for some time.
05-08: Dogwood
Male. European descent. American origin. Mid-30s. No unusual appearance.
O5-8 is one of several O5 members to focus on Foundation security. Notable in particular for expanding Mobile Task Force funding and recruitment; responsible for a general proliferation and expansion of MTFs after the destruction of Omega-7 initially resulted in cutbacks.
Said to have a relatively low-key personality, but prone to becoming slowly more aggressive as situations escalate; many underlings report that he is very pleasant to work with at first, but invariably sours relationships as they evolve over the years.
There are also reports that "Dogwood" is in fact associated with another O5-10, "The Newbie"/"The Lesser", and that "Dogwood" is one of the actual O5-8's competing chiefs of staff, whose star is presently falling due to internal drama. Even more reports claim that "Dogwood" and O5-6 "Cowboy" are the same person, and that the negative attributes assigned to "Dogwood" are the result of disgruntled ex-staff members who couldn't live up to O5-6's standards. It is unclear if this is yet more disinformation.
Possibly assassinated. Has not appeared in public for some time.
05-08: The Terse
Male. European descent. Dutch origin. Age unknown. Formerly affiliated with the Special Investigations Board, Dutch East Indies Company. Signatory of the Forbidden City Convention.
Does not speak much with others. Speech limited only by necessity. Another secret-keeper?
Coined the term 'Group of Interest', and strongly advocates for their dissolution by the Foundation.""")
        await ctx.channel.send(""" Appears to be indiscriminate towards various GoIs; no known vendetta against any known GoI.
Consistently vetoes any attempt for the Foundation to adopt a parliamentary leadership reminiscent of the Global Occult Coalition's Council of 108; advocatory for the O5 Council structure. Prevent dilution of his own authority?
05-08: The Forgotten
We are unable to recall any personal details about this individual, even under the influence of Class Y mnestics.
O5-8 has an unclear connection to the Foundation's Antimemetics Division, likely its leader or founder. O5-8 is so strongly affected by the memory erasing effects of anomalous antimemes that the other O5 Council members must ensure they regularly consume memory-enhancing mnestic drugs to avoid forgetting that O5-8 exists.""")
    @commands.command(aliases=['dossier05-09'])
    async def dossier0509(self,ctx):
        await ctx.channel.send("""05-09: The Outsider/The Ordinary
Female. European/Pacific Islander descent. New Zealand origin. Appearance consistent with recorded age of 53. Carries a walking stick with jade inlays; item's purpose unclear, whether occult or practical.
O5-9 is one of the most unusual O5s, for an oddly mundane reason: she appears to have been inducted directly into the O5 Council from the public sector.
O5-9 is one of the most unusual O5s, for an oddly mundane reason: she appears to have been inducted directly into the O5 Council from the public sector.
Strong advocate for research of anomalous phenomena, including those with SCP designations; possible ally of O5-2 ("The Gardener"). Apparently partially responsible for allowing the recent dramatic expansion of the Foundation's classified technical journals (a project apparently spearheaded by Regional Director Katherine McTiriss, if rumor is correct). Goals appear to include the development of a general explanatory theory for anomalous phenomena.
O5-9's unusual circumstances have led to a large number of contradictory reports. As far as I can tell, she replaced or superseded a prior O5-9 ("Misfortune").
It's said her appointment barely passed, with a Council vote of 7 to 6. At least three votes swung to her side at the last moment. Evidence of tension within Overwatch?
Of note: Many sources claim that O5-9 is personally close with O5-10 ("The Archivist"), but "The Swallowed Tail" source claims extreme antagonism. It's doubtful this is a coincidence. The two are intertwined, one way or another. I wouldn't doubt that both claims are true, because both were involved in a certain incident which would be unwise for us to discuss in this forum. One might say I recommend drawing zero conclusions.
05-09: Misfortune
Varying age, appearance, etc. Original unknown. Carries a bone-handled knife; obvious occult significance.
Reputation for being extremely unlucky. Restricted to underwater Foundation facilities.""")
        await ctx.channel.send(""" May or may not still hold an O5 Council position, but certainly plays a role regardless.
O5-9's personality is based in SCP-963-2. Original version attempted to replicate SCP-963 — successfully. However, SCP-963-2 only holds the memories, experiences, and personality of O5-9 up until his first death.
When O5-9 is killed — and he has been killed several times — he is "reset". After each death, he has to be informed of events that took place after the time of his first death.
Possibly replaced by another O5-9, "The Outsider". Reports claim his removal state that it was not voluntary, and was caused by one or more of the following:
a series of repeated 'resets' rendering him useless
corruption or damage to SCP-963-2 causing personality damage
Resistance to any form of change after being reset repeatedly
Inability to change with the times due to being reset repeatedly
Refusal to make use of his vote during an incident in which it was vital post-reset
Which is most likely is unclear.
05-09: The Lovers/Willow
Both: Male. European/African descent. American origin. Appear to be mid-30's; actual ages unknown. No unusual appearance, except that they are relatively similar in appearance (while apparently unrelated).
O5-9 is two people sharing the same position. They appear to be lovers. They change positions regularly, with one playing the role of bodyguard/"assistant" to the other.
O5-9 plays a "support" role within the Foundation. Primarily, O5-9 handles feeding the Foundation. They generally have a hand in procuring mass amounts of food via ordinary methods, and their staff cover it up. But they don't limit themselves to non-anomalous means. Reports also abound of vast anomalous fields growing food to feed Foundation personnel, and entire rivers created in certain remote areas of countries to produce water.
05-09: Out Of Place
Male. European descent. Fluent in English, French, Dutch, and Afrikaner. Appears to be about 50.""")
        await ctx.channel.send(""" Formerly affiliated with the Inner Africa Expeditionary Society, an organisation funded by King Leopold of Belgium. Signatory of the Forbidden City Convention.
Professes irritation towards his employment under King Leopold. Frequently rotates residence between multiple locations within Sub-Saharan Africa, particularly Belgian Congo, British Kenya, and South Africa. Perhaps to deter spies?
Prompted the O5 Council to declassify a previous iteration of SCP-1851.
Holds great interest towards the concept of "anchoring reality". Sets aside a trust fund to research on counter-ontokinetic stratagems, essentially leading to the discovery of Humes. Preparation against ontokinetic threat?
05-09: The Secret Keeper
Male. Caucasian descent. Swiss origin. Confirmed to be between the age of 45 to 51. No unusual appearance.
The title of O5-9 is passed down to any individual that holds the title of the Director of the Intelligence Agency. It is unknown how many personnel have held the title of O5-9. Records have indicated that the O5 council has indicted and removed at least one person from the title, for gathering too much information on other council members.
O5-9 is tasked with keeping the Intelligence Agency in line, and has been known to actively participate in mission regarding new or unknown GoIs, specifically with "The Mages Academy".
05-09: The Oracle
Female. Caucasian descent. Polish origin. Age between 29 and [REDACTED]. No unusual appearance, with the exception of anomalously red irises.
Foundation thaumaturgy and theology specialist, recruited from an outside cult solely to obtain information about a Level XII Diefic Entity it worshipped. Directly involved in the Damien Nowak case. Proven to be a traitor in 1985 by taking control over the Foundation in an attempt to murder the rest of the O5 Council and then putting the blame on a personal enemy of hers.""")
        await ctx.channel.send(""" Later revealed to be the result of a non-anomalous human thaumaturge named Natalie Asheworth coming into contact with the previously mentioned deity. Dead following direct contact with the rest of the god.
Current position remains vacant.""")
    @commands.command(aliases=['dossier05-10'])
    async def dossier0510(self,ctx):
        await ctx.channel.send("""05-10: The Archivist
Female. African/European descent. American origin. Appears to be mid-40s. Tends to wear grey striped suits.
O5-10 plays the role of archivist and record-keeper. She acts as custodian of the records of previous iterations of the planet and associated timelines.
These records show how many times Earth (or the timeline associated with Earth) has been severely damaged and "reset", and how many "resets" the Foundation has allowed, or stopped. Additionally, O5-10's records include the full number of K-Class events that the Foundation has ever been aware of (including some information passed from prior timelines). Most of the O5 Council does not have access to this information, and only O5-10 has access to all of it.
O5-10 inherited her role from a prior O5-10, and therefore has been an O5 Council member for several years. However, she has only recently become publicly active within the Foundation. She has "adopted" a number of newer researchers, and taken special interest in SCP-1985 and similar SCP items related to major K-Class scenarios.
Accompanied by an assistant/decoy, referred to only as "Salt".
"The Archivist" may have access to the Wanderer's Library, and be capable of "magic", learnt from Library books.
"The Swallowed Tail" source identifies an O5-10 with a wildly different appearance, history, and personality, but otherwise fitting the same role. This version of "The Archivist" is described as a woman of European descent, a former school teacher with near-perfect recall. Allegedly bloodthirsty, paranoid, and obsessed with knowledge and power.
The variant report claims the Wanderer's Library considers her an abomination, but cannot stop her from coming and going. (I should warn the reader to be suspicious of any sources that claim to know the goals and mentality of the Library, including when it's one of us updating this dossier.) While this report shows unusual signs of disinformation, it can't be dismissed.""")
        await ctx.channel.send(""" What truth lies here? What truth is being hidden?
05-10: Stone [DECEASED]
Male. European descent. Appeared to be mid-50s; likely older. Traditional in appearance.
Formerly played the role now held by "The Archivist". Professorial reputation.
Forcibly removed from the O5 Council between 2004 and 2011 for attempting to permanently activate SCP-003. Likely executed.
05-10: The Assassin
Female. East Asian/European descent. Italian origin. Appears to be mid-30's; actual age 60+. No unusual appearance. Wears a necklace around her throat with a carved marble eyeball pendant; likely occult significance.
Former Foundation assassin. Originally was an exceptionally effective assassin, then taught assassination, then taught others how to teach assassination. Worked her way up head of Foundation's internal clandestine service, then elevated to O5 Command. May regret accepting the promotion, now spends most of her time reading reports.
Though this is unconfirmed, she may be one of the few O5 Command members to retire; reports agree that her retirement (if it happened) was voluntary. Other circumstances unknown.
05-10: The Veteran/The Man General
Male. European descent. Unknown origin (American? European? Russian?). Unknown age; if reports are true, certain post-human lifespan. Varying appearance.
O5-10 is one of the first additions to the O5 Council. His specific identity has been extremely difficult to pin down.
Solidly backed rumors name him as US general or generals, possibly Thomas "Stonewall" Jackson, a Confederate general who fought during the US Civil War.
Yet other reports name several Russian generals who disappeared in the aftermath of World War I (the Second Fatherland War). These reports tend to be more favorable towards the character of the generals themselves.
Perhaps there are multiple people holding this position.""")
        await ctx.channel.send(""" Though it mystifies me what would connect Confederate generals from the US Civil War and Russian generals from the first World War, generals with differing ideals and of different eras.
05-10: The Grand Master
Male. Uncertain descent and origin (believed to be ethnically mixed). Appears to be 75. Catholic. Formerly affiliated with the Knights of the Military Order of Borja y Aragón. Signatory of the Forbidden City Convention.
Implied to have minimal direct experience with the anomalous, a common trait among the Borja Knights during the 19th century. Knowledge of the anomalous mainly derived from secondary sources from previous generations of the Borja Knights.
Displays significant apprehension towards the Church of the Broken God. Possible traumatic previous encounter with Broken God followers?
Successfully created a pension scheme for KIA Foundation members and other welfare schemes for Foundation personnel. Drafts eulogies for KIA Foundation members.""")
    @commands.command(aliases=['dossier05-11'])
    async def dossier0511(self,ctx):
        await ctx.channel.send("""05-11: The Mailman
Male. European descent. Eastern European origin. 80+. No unusual appearance.
Origin of nickname uncertain; possibly an actual mailman before appointment to the council. Nickname is in common use; staff often joke about him "going postal", but admit he is one of the most even-tempered and kind people they've ever met. Grandfatherly in demeanor.
O5-11's most well-known role is to sign off on Termination Orders of Class D personnel, versus approving their transfer to another Site. Whether all Class D are terminated at Sites due to anomalous exposure, or merely transferred to another site, O5-11 makes the final decision.
Confirmed to have held at least one other O5 number, though the number itself is unknown. May be an indication of a standard number changeover process, or perhaps of unknown internal political maneuvering.
05-11: The Liar/The Father Of Lies
Unknown descent. Unknown origin. Apparent age varies. Always attractive in appearance; tends to wear expensive clothing as any gender.
Gender appears to vary, either via anomalous means or due to multiple figures in the same position. Usually referred to as 'she', despite the nickname.
O5-11 is the Foundation's chief disinformation officer. She organizes cover-ups, invents cover stories, and creates rumors to be spread both within the Foundation and without. This includes many erroneous reports about O5 Command (that is, assuming this report itself is not erroneous, which it may be). Not even her staff know what's true and what isn't; and in many cases, neither does she.
Very often referred to using different O5 numbers, including non-standard numbers such as O5-15. Naturally, there are also reports that O5-11 doesn't exist at all, and is a cover for an even deeper disinformation campaign.
Frankly, I find it rather likely that 11 is not actually the correct number, and it's possible that this "O5-11" is actually a separate figure, like the Administrator. Presently impossible to tell.""")
        await ctx.channel.send("""
After all, we're dealing with far too many liars.
05-11: The Senator
Male. European descent. American origin. Appears to be 70+; verified post-human lifespan. Varying appearance; usually dresses in respectable, immaculate tailored clothing.
O5-11 is a high-powered politician, who has been installed in the Senate by the O5 Council for direct control over certain political matters.
Notably associated with numerous secret societies. Said to be a high-ranking member of the Shriners, and to be the founder (or a founding member) of Skull and Bones. Reports say he maneuvered a great number of secret societies into place over the centuries, and now sits in Washington tugging on the strings.
05-11: Jings
Male. European descent. Western European origin. Mid-40s. No unusual appearance, except that he wears a bracelet made from human teeth; obvious occult significance.
Former Foundation field agent. Prior to being elevated to the O5 Council, claimed he would implement a number of changes and improvements to Foundation policy; most of these did not materialize after his elevation. Generally negative reputation; apparently few accomplishments. Not much seen in public since. Possibly assassinated.
05-11: The Keeper/The Warden [DEFECTED]
Female. European descent. American origin. Appearance unknown.
Developed many of the Foundation's early containment procedures. Supported extensive research into the anomalous.
Opposed categorizing humanoids as SCPs. To her, an SCP was an object: a book or a ball or a car, not a child. Caused the initial schism in the Council, which O5-7 would take rhetorical advantage of; when she was outvoted in the Council, she would not take no for an answer, and enacted the split. She saw the Chaos Insurgency as liberators; humanoid SCPs would work with SCP Foundation researchers, not be imprisoned by them.
Wife of then-O5-12. Strong-armed O5-12 into defecting with her (along with O5-4 and O5-7, and another O5 who was killed during the schism).""")
        await ctx.channel.send(""" Because of their positions, they were able to take many humanoid SCPs with them, along with a great deal of useful SCP items.
05-11: The Recluse ~~[MISSING]~~ ~~[DECEASED]~~ [UNKNOWN]
Male. European Decent. Elderly appearance, 70+, despite being the youngest Council member - refused anomalous life extension?
O5-11, formerly Roger Sheldon, was apparently missing for over a decade. Presumed deceased, but no replacement was selected. Then, after 18 years of absence, he was back on the Council as if he'd just been on a long vacation.
Reports suggest a dramatic change in personality and priorities upon his return. Much more concerned with his own safety, and with the welfare of Foundation staff. What was he doing during for 18 years? And why can't I find any information about what he's done since coming back?
Follow up this lead at your own risk.
05-11: The Bureaucrat
Male. East Asian descent. Japanese origin. Appears to be 80. Formerly affiliated with the Bureau of Onmyō (陰陽寮; onmyō ryō), a.k.a. the Holy Emperor's Council for Unearthly Matters (怪異なる事物についての聖帝評議会; kaii naru jibutsu ni tsuite no seitei hyōgikai). Signatory of the Forbidden City Convention.
Alleges that Japanese Emperor Kōmei died of anomaly-related causes. Once claimed to have observed multiple undocumented SCP-2863 instances throughout Kyushu, Shikoku, and western Honshu. Expresses problems with self-esteem. Mostly interacts with O5-3, O5-7, and O5-13.""")
    @commands.command(aliases=['dossier05-12'])
    async def dossier0512(self,ctx):
        await ctx.channel.send("""05-12: The Accountant
.
Male. African descent. African origin. Appears to be mid-40s; almost certainly older. Large-bodied. Always dresses in extremely expensive tailored clothing with similarly expensive jewellery. Wears dark wrap-around glasses: smoked glass framed in ivory. May or may not be to hide his eyes. Likely occult significance.
O5-12 plays the role of accountant for the Overseer Council. A mathematical genius; ensures all the Foundation's numbers add up. Has access to certain data that no other Foundation member does, for this purpose.
Precise, calm, practical. A strong believer in order. Every part of his daily route, and indeed every action he takes, right down to his drinking habit, is strictly scheduled.
"The Swallowed Tail" source presents an alternate but still somewhat consistent picture of this O5-12. Not an original Council member, "Omar Alawe" was promoted following the death of the previous O5-12. His mathematical ability allows him to see correlations invisible to everyone else - not quite precognition, but may as well be. Some of the background is misinformation (likely including the photo — though I can't be sure, for obvious reasons), but trying to verify this information led down some interesting paths
05-12: Adam [RETIRED]/[DECEASED]
Male. European/Jewish descent. American origin. Somewhere between 130 and 200 years old. Appearance unknown.
Very little information exists on O5-12's role within the Foundation, except that he was an exceptional researcher. Known primarily for fathering a stillborn child in the mid or late 1800s, and transforming her into SCP-321 in an ill-fated attempt to save her. Most information has been expunged from accessible Foundation records. Recovered information suggests a familial relation to Dr. Jack Bright. (Older brother? Father?)
"Adam" is one of the few O5 Command members to retire. His retirement, by all accounts, was voluntary, which came as a surprise to me given his history.""")
        await ctx.channel.send(""" It appears that he was, in fact, the first ever O5 Command member to retire.
Interestingly, it is unclear whether "Adam" was required to undergo the amnesic administration supposedly mandatory for retiring or removed O5 Command members. His location, unfortunately, is unknown to me.
There are also some rumors suggesting his connections to "Department of Abnormalities". Nature of this department and O5-12 connections to it requires more investigation.
Other rumors, on the other hand, completely dismiss part of the above information, saying that he was one of the 12 original overseers, Convention on Preternatural Phenomena signatory — which created the modern Veil policy — and last general director of American Secure Containment Initiative before it merged into SCP Foundation in 1870. According to this version, "Adam" was also killed during the Great Factory Purge and his position was passed on to his descendant; probably "The American" who, according to this version, would have the position of O5-12 position instead of O5-6.
05-12: The Contractor
Male. African/European descent. American origin. Mid-40s. No unusual appearance.
O5-12 was an emergency appointment following a previous assassination (or assassination attempt) during an O5 Council issue that required either an O5-12 or an O5-1, and O5-1 was unavailable.
After this, he couldn't simply be demoted; therefore, he was assigned to side projects. He purchases land to build Foundation facilities on. He works with people who design Foundation facilities to make sure their needs are met; he works with local governments (often to request that military installations be built over actual Foundation sites as a cover), and he hires new Foundation personnel to implement such projects.
Additionally, O5-12 acts as an unofficial head of human services, requiring that Foundation personnel receive regular physical and mental checkups.""")
        await ctx.channel.send(""" Despite apparently caring a great deal about the average Foundation member, O5-12 is usually described as an obsessive, distrustful shut-in. His staff is very small, and they do very little.
05-12: The Trainman/The Conductor [DEFECTED]
Male. European descent. American origin. Appearance unknown.
Assisted O5-11 in developing many of the Foundation's early containment procedures. Approved of weaponization of SCP objects. Supported extensive research into the anomalous.
One of O5-12's significant roles was overseeing the rotation of SCPs between Foundation facilities. This rotation was publicly aimed at getting new perspectives on SCP objects for research and effective containment purposes. Less public, but no less important, was the secondary purpose of preventing any group of researchers from working with humanoid SCPs for too long.
Initially resisted defecting from the Foundation, but was strong-armed into joining the Insurgency by his wife, O5-11. His position of control over SCP rotation and transportation allowed the Insurgency to make off with a very high number of SCPs (particularly humanoid SCPs) during the schism. Additionally, his popularity with Foundation generals who desired weaponization of SCP objects gave the Insurgency a significant power boost during the Foundation Civil War.
05-12: The Physician
Male. East Asian descent. Chinese origin. Appears to be 70. Formerly affiliated with the Abnormality Institute (異學會; yì xué huì), sometimes called 'Chinese Abnormality Institute' (中華異學會; zhōng huá yì xué huì). Signatory of the Forbidden City Convention.
Believed to have been invited to join the O5 Council only due to his knowledge of a "memory-altering drug" (i.e. amnestics). Collaborated with the Chinese Nationalist Army to eliminate (betray?) the Meng clan; rationale is to monopolise amnestics for the Foundation.
Coined the term 'Safe'. Rudimentary knowledge of English.""")
        await ctx.channel.send("""
Note: Amnestics might have undergone potentially radical advancements over the years. O5-12's statements regarding amnestics might not be applicable.
05-12: Cyrus
O5-12 is a brain in a jar.
From the reports I've heard, his body was failing, and the other O5 council members wanted to keep him around as an advisor. They had the technology to do it, so they went ahead and preserved his mind.
It is unclear why the Foundation specifically chose this method, rather than one of the many other ways of prolonging life at their disposal.""")
    @commands.command(aliases=['dossier05-13'])
    async def dossier0513(self,ctx):
        await ctx.channel.send("""Of note A number of reports have indicated that the Foundation did not start with 13 O5 Council members. Most reports indicate that the original O5 Council numbered 12, and some indicate it still numbers only 12, with number 13 a work of disinformation.
Other reports indicate an O5-13 was added after the fact due to the number 13 gaining modern occult significance and therefore power. And in practical terms, a tiebreaker vote was required once too often.
Some sources indicate that there are more than thirteen members of the Overwatch Council, including mention of an O5-14 assigned to specific SCP-001 objects, or seizing power through anomalous means.
Several of these options may be true. These reports reflect this lack of clarity.
05-13: The Tiebreaker
O5-13 does not exist. Everyone outside the O5 Council is told he exists, and memos are created under O5-13's name, but O5-13 exists only as a tiebreaker vote.
O5-13's vote is rotated between each O5 Council member, starting at 1, and passed up a number each time a tiebreaker vote is required and used.
Holding O5-13's vote is required to access a few selected databases. This knowledge may be attached to O5-13's vote (and wiped from the holder's memory when the vote is passed on), or it may simply comprise access to 13's unique databases.
05-13: Tamlin
Either male or gender-fluid (reports differ, may be relevant to anomalous traits). Unknown descent (reports differ, may be relevant to anomalous traits). Unknown origin - possibly Middle Eastern? Age unknown. Tall, red-headed.
Per these reports, the "Tiebreaker" reports are accurate. However, O5-13 does exist, despite his vote not being held by himself most of the time. Original identity "Dr. Joseph Tamlin" or possibly "Yoshua bin Yosef" - unclear if these are alternative names for the same person, or different people holding the same position. "Tamlin" may (or may not) be more of a title than a specific individual - he/they continue to elude us.""")
        await ctx.channel.send("""
Holds only an advisory position by necessity. Is an anomalously altered human existing in a temporally destabilized state or location; partially "unstuck in time". Acts as a fail-safe for restoring 13's vote to its proper bearer, should it be compromised. Reserves the right to vote, but only exercises this right on pivotal decisions.
Some reports (not all) indicate drastic shifts in appearance, race, and gender, but the presence of red hair (whether natural or colored) remains consistent. Unknown relevance; possible perception alteration issues or literal shape-shifting.
Occupies a room (or rooms) in "Tamlin House", a hidden location related to SCP-1590, accessible only through a number of esoteric methods. Appears to be bound to the location. Does not usually participate directly in O5 Council meetings, but observes most of them (not necessarily synchronously).
"Shows what you know."
05-13: The Meddler
Male. European descent. American origin. Mid-30s. No unusual appearance.
Most reports of O5-13 result from the conflicts he starts or becomes involved in, due to inter-office gossip from other O5's personal staff. No one outside the O5 Council appears to be aware of this O5 member's role in the Foundation; the role he generally seems to play in practice is interfering with other O5 members' projects. Known for ranting about how other O5 members (and lower-ranked Foundation personnel) are not running operations correctly.
Not a particularly popular O5 Council member. Surprisingly, reports do not indicate many assassination attempts.
05-13: Death
Gender unknown. Descent unknown. Origin unknown. Age unknown. Appearance unknown.
One of the more outlandish reports on a possible O5-13; claims that Death itself was bound by the O5 Council in the early 19th century. Per these reports, the slot of O5-13 was created for Death in the first place. Euphemistically referred to as "The Other Overseer".""")
        await ctx.channel.send("""
Death is both a member and a prisoner of the O5 Council; it can cast a vote as normal. However, it is imprisoned by the rest of the Council, and by a majority vote of the O5 Council, the Council can control it. Death apparently otherwise carries out its functions as normal.
SCP-006 does not exist; the longevity of O5s actually stems from O5-13. By majority vote, they can order O5-13 to stay its hand from any Council member — or indeed anyone in the world, though using this power for non-Council members seems to temporarily weaken Death's chains, and is therefore rarely used.
When used, it is typically on a mass scale — SCP-2000 and similar anomalous items also do not exist, and are used as cover for every time that Council has voted to utilized O5-13's power to return most of the world's population back to life.
These reports may, or may not, conflict with other claims that the O5 Council's immortality comes from imprisoning Death, or from residing in a location shielded from the processes that cause mortality. Alternative reports claim that the Administrator, not O5-13, has assumed the role of Death.
Unknown connection, if any, to SCP-2935.
"The Swallowed Tail" source also identifies Death as having been bound to the Council by a bargain, in exchange for the life and Council seat of one Felix Carter, the former O5-13 ("The Meddler"). SCP-006 exists but is insufficient for the Council's purposes, and long since exhausted. The body of Felix Carter, which grants Death a council seat, is preserved somewhere in the South Atlantic.
This report contradicts the specifics of other reports claiming O5-13 to be "Death", but we can confirm that there is some form of anomaly in the South Atlantic, with antimemetic properties matching the description given in this report. Something is being hidden here.
05-13: AI Complex
[Personal traits not applicable]
O5-13 is an artificial intelligence construct.""")
        await ctx.channel.send(""" This AI construct (using a variety of anomalous technological and non-technological methods) is supposedly able to take all factors relevant to the Foundation's goals and make a recommendation on any major course of action.
Due to certain consequences (whether occult, resourced-based, or simply bureaucratic) of making use of this AI construct, it is only employed when the O5 Council must break a tie on a non-trivial matter.
Further details have been remarkably hard to attain even by esoteric methods. Whether or not this version of O5-13 exists, there are secrets behind this thing that the Foundation wishes to keep hidden.
05-13: The Activist
Male. South Asian descent. Sikh origin. Appears to be about 50. Formerly affiliated with 0th Anti-Cult Regiment, a colonial regiment in British India. Signatory of the Forbidden City Convention if "The Persian" is not present.
Major advocate for a meritocratic administration within the Foundation. Known to have formed an informal voting bloc with O5-11 and O5-12 to pursue racial equality within the Foundation.
Also known to have voted with O5-1 for many operational matters. Known O5-1 prior to the Forbidden City Convention. Perhaps a puppet for O5-1 to gain an additional vote in the O5 Council? Perhaps in exchange for said meritocratic administration?
05-13: The Persian
Male. Middle Eastern descent. Iranian origin. Appears to be about 70. Shia Muslim. Formerly an independent consultant on anomalous matters for the Ottoman Empire. Signatory of the Forbidden City Convention, if "The Activist" is not present.
Knows O5-7 prior to the Forbidden City Convention. Holds strong suspicion towards O5-1.
In charge of the 'Autonomous Administration of the Greater Middle East', a sub-organisation of the Foundation based in the Middle East. Him and the AAGME do not exist in realities where "The Activist" exists.""")
        await ctx.channel.send(""" In fact, I can't seem to find the Office for the Reclamation of Islamic Artefacts or its equivalent in realities where "The Persian" takes up O5-13. AAGME and ORIA – counterparts???
Resembles ORIA founding member, Jibril Mani, in realities where "The Activist" is present instead.
05-13: The Pedestrian
Male. Latin American descent. Late-50s. No unusual appearance.
O5-13's special connection to the anomalous gives him a perspective no other council member could begin to fathom. While Normalcy Confirmation meetings require eleven members for quorum, no meeting is allowed to proceed without O5-13's attendance.
Additionally, he is the only member of the original O5 council to survive the Caesar incident. Investigation into the nature of the incident and O5-13 is still ongoing.""")
    @commands.command(aliases=['05staff'])
    async def staffofthe05(self,ctx):
        await ctx.channel.send("""O5 Command possesses their own Mobile Task Force, MTF Alpha-01, the Red Right Hand. They alternately act as the Foundation researcher's best friend and an outright medieval inquisition, complete with 'disappearing' people who the O5s disfavor.
Besides MTF-Alpha-01, each O5 has their own personal staff and security. Usually O5 personal staff have Level 5 ("Thaumiel") access to Foundation archives (though they still need to be added to Special Access Programs, and do not have the "blanket" access that O5s do). Some of the O5's personal staff and secretaries are among the most powerful people in the Foundation.
O5 Council members sometimes fixate on certain Foundation researchers. Many of the most well-known Foundation doctors and agents have been under the eye of one or more O5 members, willingly or not. This does not always end well for those favored in this way.
Factotum
According to some reports, the personal staff of the O5 Council are known as the Factotum. These Foundation operatives are selected for absolute loyalty, and act as personal assistants, bodyguards and decoys. Many encounters with an "O5" are actually mediated by a Factotum, dressed and disguised to perfectly resemble their assigned Council Member.\mReports ascribe some of these staff certain anomalous abilities, and the O5 Command reportedly approves this anomalous alteration to allow them to act as better decoys or bodyguards, directly circumventing official Foundation procedure. This makes it almost impossible to tell a decoy apart from the real thing.
Of course, if they want to mislead, there's no reason to make this a perfect resemblance. For all we know, every one of the O5s described in this dossier are mere decoys, and the real O5 Council remains unknown.
Delegation
Although O5 Command holds tightly to its power over the Foundation, they do delegate many tasks.""")
        await ctx.channel.send(""" The exact command structure of the Foundation is unclear, but references have been made to the body known variously as the Site Directors’ Council, the Site Directors' Executive Committee of the Whole or the O4 Council (not to be confused with the O4 Command in charge of Lockdown Procedures). This organisation is assembled for matters requiring a broader perspective, or considered too minor for the O5 Council yet too significant or far reaching for any individual to decide. Under certain circumstances, this body may even have the power to depose and appoint O5 Council members, and it seems designed to ensure that the Foundation can continue functioning in the event that anything happens to the O5 Council.
Regional branches of the SCP Foundation have their own equivalent bodies with full clearance for all anomalies under their regional jurisdiction, acting as an O5 equivalent for most intents and purposes, although still subordinate to the O5 Council. This includes the German Directors Council (known as the O4 Council), the Superintendence of the Italian Branch (The S5), and the Lusophone Board of Directors (The CL5).""")
    @commands.command(aliases=['05info'])
    async def infoaboutthe05(self,ctx):
        await ctx.channel.send("""Appointing new O5s is rare to the point of being legendary, at least publicly. Rumors persist — potentially true — that some or all of the O5 Council members are inhuman or possess supernatural powers. Rumors also persist that they are unkillable, but this is at least partially untrue, given that several are known to be deceased.
As far as I can tell (and I may be wrong), all O5 Council members are human in origin, even if altered after the fact. A minority of the O5 Council may have anomalous abilities or traits, if reports are to be believed (in particular reports on O5-1 and O5-2), but none of the O5 Council are reality benders, and most of them are simply human… but humans with access to the Water of Life, and power beyond imagining. Far, far, far too much power.
The O5s rarely intervene in the day-to-day processes of the Foundation, or the containment of SCP objects. They tend to keep an eye on Keter-Class objects, and practically micromanage Thaumiels and Apollyons.
But sometimes — rarely — they'll jump into an apparently random Euclid- or Safe-Class object's documentation, and make some summary judgment with or without explanation. After all, no explanation is required of them.
O5 Council members are officially barred from coming into contact with any anomalous entities. This is, naturally, not strictly true in practice. At minimum, all O5 Council members of sufficient tenure have access to SCP-006, a "fountain of youth", and likely to other means of prolonging their lifespan as well. And that aside, O5s tend to be able to bend rules, even their own rules.
Some reports suggest that O5s regularly switch numbers with each other, either ad hoc or on a standardized basis. They make common use of body doubles and other security and disinformation techniques.
The Meeting Place of the O5 Council is frequently referred to as Protected Site-001, and one or more O5 Council Members may reside there most or all of the time.""")
        await ctx.channel.send(""" Alternative reports have described this headquarters as Building T-01 or O5 Command instead. Some reports claim that at least one O5 is in space at all times.
One particularly interesting report indicates that O5 Command members all wear an article of clothing and/or fetish object as a symbol of their office, with this totem being passed on to their successors. Possibly fashioned from the corpse of the most powerful reality bender to ever live, each object can completely stabilize reality around an O5 member. (Unclear how long this lasts, or if it is a permanent low-level effect.) Also said to grant additional abilities; precisely what these are remains unclear, as does the truth of this report.
Another set of reports claim that a number of humanoid SCPs are family members of O5 Council members. It is possible that fictional anomalous documentation was drawn up for them to justify keeping them under the best protection possible. There are also claims that some O5s have gone as far as to actually anomalously alter their family members to permanently justify Foundation protection via containment.
The O5 Council appears to choose their own members should a seat become vacant, although under certain circumstances they may become accountable to the Senior staff of the Foundation.
The exact relationship between O5 Command and the Foundation's Ethics Committee is unclear. I used to think that the Committee either didn't exist or just rubber-stamped the Council's decisions, but some reports suggest that the Ethics Committee has the power to overrule or even depose the Council. Who's really in charge here?
There are a few reports of an unofficial "O5-0", a former associate of the original O5 Council Members who left the Foundation due to ideological differences. Much like the official members of the Overwatch Council, I've encountered multiple contradictory descriptions of this "O5-0" - sorry, that seems to be a trend.""")
        await ctx.channel.send(""" They certainly sound like they'd be an interesting person to meet, if I ever get the opportunity…
One source bears notable mention: the reports, sources, and personas collectively referred to as "The Swallowed Tail". Please be warned before looking into this report: we acquired access to this documentation through the heart of the Chaos Insurgency, and they seem to have gotten most of their intel from a journal written by a Global Occult Coalition agent that later defected to the Foundation. If you're unfamiliar with the risks of Insurgency dealings, avoid looking at this, if you value your own life.
We initially thought this report to be Foundation disinformation (perhaps even targeted at me/us, the creator/creators of this dossier), but when we became aware of greater context, we realized we could draw zero conclusions.
Is there a multiversal thread issue here that we're not aware of? A disconnection followed by an unknown bridge? An undescribed resonance? Something so obvious, too close to ourselves that we cannot see it? Something Outside, and dangerous?
I/We really have to look into this.
If you don't know what you're doing, remember this: there are many worlds, and there are as many ends of the world. Some things you're better off not knowing. The number of these things may or may not be zero. Help, or don't.""")
    @commands.command(aliases=['Alternate05theories'])
    async def alt05theories(self,ctx):
        await ctx.channel.send("""Some well-sourced reports suggest a specific membership or structure for the O5 Council that is not indicated in the previous reports in this dossier. These reports follow.
Some well-sourced reports suggest that most information in this dossier is an elaborate facade and that the nature of the O5 Council is significantly different than what we think. For example, reports that O5 members are extraterrestrials, angels/demons from Abrahamic mythology, or simply do not exist at all. These reports follow, as well.
Usurpation
The conflicting descriptions of the O5 Council strongly suggest that the Council's membership has changed before, perhaps many times. Claims that the entire O5 Council has been overthrown and replaced at various points are harder to verify since no two stories are the same. Some claim that the coup came from within the council, consolidating all power under a single seat, while others claim that the O5 Council was deemed corrupt or obsolete and so were deposed or replaced by their subordinates within the Foundation, or even by external enemies. If any of these reports have any basis in reality, it is likely that some (all?) of the information in this dossier is outdated.
Individuality
According to some of our sources, the O5 Council was long ago overthrown. After the Chaos Insurgency defection catastrophe, the SCP Foundation was severely lacking in top-level administrators. Desperate, the O5 Council used anomalous genetic engineering and other tools to create personnel capable of filling key Directorships and executive roles. This proved to be a mistake.
Once in power, these entities conspired to take control of the Foundation. Using their combined influence, they were able to secretly remove the council and replace it with themselves. Mismanagement due to this instability may cause the Foundation to make mistakes.""")
        await ctx.channel.send("""
Containment
If the purpose of the Foundation is to contain the anomalous, the alleged abnormality of the O5 Council may seem like a betrayal of their original mission. But what if the Foundation exists to contain its Overseers? What if all the security and all the mystery exists not to protect the Council, but to hide them from the world?
Perhaps it's been this way the entire time.
Puppet Masters
Although the O5s and the Administrator are generally regarded as being committed to the SCP Foundations stated goal of preserving "normalcy", multiple reports allege that the O5 Council is secretly responsible for creating anomalies.
Additionally, there are descriptions of the Administrator playing a role in creating anomalies, and founding, running and collaborating with multiple Groups of Interest, despite these organisations generally being seen as adversaries and competitors to the Foundation. It is unclear whether the rest of the O5 Council is aware of this.""")
    @commands.command(aliases=['admin', 'admindossier'])
    async def administrator(self,ctx):
        await ctx.channel.send("""Note The Administrator's role within the SCP Foundation is often nebulous, but they always seem to have played a role in the organisation's founding, and are credited with writing the Mission Statement. Consistently associated with SCP-262. These things, at least, seem to be true, at least assuming the Administrator exists.
If reports are to be believed, each Administrator has had some anomalous traits which may be a factor of the position, including partial protection from reality shifts and extremely slow aging. Some reports even indicate that "the Administrator" is an anomalous entity contained by the Foundation.
The Administrator's position in relation to O5 Command is unclear. The Administrator may hold a position similar to an O5 Council member, and may be less powerful or more powerful depending on the situation and time. Because of all this, the Administrator often comes off seeming like a wild card, albeit a rather calm wild card.
There may have been multiple Administrators throughout the Foundation's history, but very few reports have indicated more than one at a time. Some reports claim that the Administrator has retired, others claim that the Administrator is deceased, and still others claim that "the Administrator" was only ever an alias used by another member of the O5 Council, possibly O5-1.
The Offical
Male. European descent. American origin. Verified post-human lifespan; reported as appearing between mid-30s and mid-50s. No unusual appearance.
Note: This version of the Administrator has been repeatedly confirmed as a false front, used as a cover for one or more of the Foundation's actual Administrators. May still be worth looking into further.
Deliberately over-the-top reputation. Lack of aging made relatively public by way of universally repeated rumor. Associates with numerous major heads of government, representing Foundation interests to them. Said (rather insultingly) to have "a penchant for suits, fine liquors and loose women".""")
        await ctx.channel.send(""" An example from a typical report:"He has been friendly with people of many political stances and is generally well liked if not respected. When he does become angered, even heads of state are quick to appease him and commonly offer sincere apologies."
Usually said to have a number of over-the-top traits, such as never bringing his hands more than a few inches apart, and ordinarily being slow and sluggish and then displaying amazing feats of strength.
F.Williams
Male. European descent. American origin. Mid-30s. No unusual appearance.
According to these reports, an individual known as "F. Williams" created the original [CORRUPTED]
[FURTHER DATA LOST]
We're not even sure what that first initial is short for. We've found sources claiming it's "Frederick", "Francis", "Fritz", "Friedrich" or "Franz". Sometimes, the surname's something else or the name's "William Fritz" or "Fritzwillis", but the letters "F. W." keep showing up.
Agnes Peterson
Female. European descent. American origin. Verified post-human lifespan. Appears 50+. Old fashioned, wears horn-rim glasses, keeps hair in a bun. Very proper.
One of the original founders of the SCP Foundation. Pulled together the initial members into an organization; produced order from the initial chaos. Jokingly referred to as being very good at herding cats. Brisk in manner. Smart, ambitious, and good at knowing when to either create or ignore rules of order.
Kismet
Female. Middle Eastern descent. American origin. Verified post-human lifespan. Appears 50+. No unusual appearance.
Her role is to track down and select each new and future member of O5 Command. She is a trained mathematician, and uses a form of statistics along with occultic procedures for her selection methods. She has personally selected every single member of O5 Command, in some cases years in advance.""")
        await ctx.channel.send(""" She occasionally also opts to choose their number, though which number is sometimes kept secret from all others except her and her staff until the new promotion is ready (presumably via a slot being opened).
Spider
Masculine. Descent/origin unknown. Head appears 30+. Unkempt white hair. Wears thick-lensed glasses and SCP-262 (Coat of Many Arms). Nonhuman body.
Apparently a human hybrid, or nonhuman entirely. Remarkable in appearance: A mostly human head, albeit with orange eyes. Body is completely nonhuman and hardly even bipedal, made of a twisted, weathered charcoal-like material, with atrophied natural limbs. A steel mesh covering holds the body inside the Coat of Many arms, and some of the many arms keep it in place. Other arms make up his "arms" and "legs", giving him either a generally humanoid look or a rather spidery look depending on how subtle he's attempting to be.
Apparently associated with the SCP Foundation since its inception, though always in a supporting role, not at the top of the power structure. Possibly owns the land Site-19 is built on. Only a few personnel outside of O5 Command have ever seen him. Softly spoken, but harshly punishes failure.
References in reports claim this Administrator originates from "The Plane Where Eyes Cannot Follow."
The Middleman
Male. Unknown ethnicity. Unknown nationality. Unknown age.
Efforts to obscure this man's identity go beyond what would be expected, even for someone of his position - I've seen video recordings of him and still couldn't describe what he actually looks like. It does seem that he was originally a file clerk for a government organisation dealing with the anomalous, but sold his secrets to the thirteen people that would become the O5 Council. Despite this, it's rumored that he's sided with the Foundation's Ethics Committee in opposing several O5 decisions. Reported dead multiple times, but never seems to stay that way, for some unknown reason.""")
        await ctx.channel.send("""
Possibly commands Mobile Task Force Rēsh-1 ("Seat of Consciousness"), although it's unclear if such a Task Force even exists.
The Archaeologist
Male. European descent. English Origin. Appears 60+ (verified post-human lifespan).
According to official records, Frederick William Abernathy engaged in some minor archaeological research, discovered nothing of note and died in obscurity. Unofficial sources indicate a much more eventful career, starting with the discovery of a Mesopotamian Goddess while excavating an Egyptian Tomb. Later encountered the entity known as the "Guardian At the Gate" and commanded to "PREPARE" (for what?). This was the impetus for the establishment of the Secret Society for Cultural Preservation, ~~the precursor~~ one possible precursor to the SCP Foundation. Current location and status unknown, but believed to still be in an influential position within the Foundation.
Certain reports suggest that this individual (or someone similar) may have been succeeded by a female Administrator. If so, the original Administrator is likely deceased, although there are rumors that he's still able to advise the Foundation.
The Duke
Male. European Descent. Austrian origin? Appears to be in his 40s, despite being over 300 years old. Human?
Known as Franz C. Williams. Inherited a title as an Austrian Duke within the Hapsburg Empire in the early 1700s. Emigrated to the USA during the Seven Years' War (also known as the First Occult War). Played an unknown role in the conflict, reason for leaving Europe unclear. Established a precursor to the Foundation from his mansion in rural Virginia. Arrived in the Americas with eleven others - the original twelve Overseers? Outlived multiple O5 Councils, continues to lead the Foundation in the present day.
Ethan Horowitz
Male. Undetermined European ethnicity. Anomalous artifacts and techniques have extended his physical capabilities/longevity. Unknown true age.""")
        await ctx.channel.send("""
An acquaintance of the Serpent prior to the Foundation's creation, and frequent face in the Wanderer's Library. Perpetually youthful, optimistic, charismatic, and charming. Creator of novel spellcraft. Formed the Foundation alongside O5-1, having been inspired by the Serpent's rejection from Heaven.
He drinks love so deeply, it's a wonder he hasn't drowned.
Too many arms,
too many faces,
for one man to carry.
Assumed the form of Death in 2016.
Led his ground-forces against humanity in 2███.
Assented to the disembowelment of Heaven.
i think
he simply
lost sight
of everything.""")
    @commands.command(aliases=['05induction'])
    async def inductiontothe05(self,ctx):
        await ctx.channel.send("""If you're reading this, then congratulations. One of us has died. Something killed one of us. A monster, perhaps, or a rival from the GOC. Or maybe we got just a little close to the flame, like Aaron. Not old age, of course. We took care of that, didn’t we? Anyway, one of the old guard is gone. Maybe Jason. Maybe Agnes. Maybe me. Hell, I'd be surprised if I wasn't the next one to die. I always was the most expendable.
I’m going to write this to you as though you were a human being. It will be the last time anyone extends you the courtesy, so I hope you appreciate it.
Whoever you are, whatever you did before, you must have been high-ranking when you were pulled into this. You must have noticed the discrepancies, the inconsistencies. I don’t know how much you’ve been told already, or how much you’ve pieced together. The crux of the matter is this: The retrievals and recoveries of SCP objects are staged, or made up whole cloth. We have never \“discovered\” an SCP in the entire history of the Foundation.
I should start from the beginning. Let me tell you a story.
Aaron Siegel was a physicist studying at Cornell in 1891. He was a truly gifted individual, and had his life taken a different path, I believe that his name would be there with Edison, Einstein, and Hawking. I knew him very well. He was, and may still be, my brother.
He was also an avid amateur naturalist, and enjoyed hiking through the woods. One day, while visiting our family home in Essex county, he came across a gravel path. He decided to follow it for a time, and noticed that it kept climbing uphill far longer than it should have. It should have taken him above the nearby hills. Instead, he found himself back where he’d started, without a foot of downwards travel.
Another man would have assumed his senses were faulty and left. Aaron, however, was a stubborn man. He investigated further. He found the path did not conform to the pure geometry of Euclid.""")
        await ctx.channel.send(""" Like Saccheri before him, he had found something abhorrent to the nature of straight lines.
He studied it. The equations he derived are part of the file you’ve received. You’ll learn them by heart eventually. He built a small shack nearby which served as a makeshift laboratory. His first experiments produced a key capable of opening any lock, now contained as SCP-005.
He brought in others. As his brother, I was one of the first he contacted. I was a medical student at Harvard at the time. I initially thought he was mad, but when he showed me the path, the key, I had to learn more. There were others with us, other friends and colleagues. Most of them are gone now, but… We were the core. We created the Foundation from around ourselves.
In the beginning, it was just about discovery, about finding the things we could do. We had such high hopes, such plans. We were going to change the world. We were going to save it from itself. We could feed the hungry, shelter the homeless, heal the sick and dying.
Thomas Carter found us money. We were none of us poor, but we ran through our fortunes quickly. Thomas used his connections on Wall Street and in Washington to fund us. He showed them the least of what we could do, and promised heaven against the threat of hell.
Agnes Peterson, my brother’s fiancée, was the administrator. We knew nothing of how to run an organization. We were a herd of cats, running to and fro, and she turned us into a foundation, putting us dreamers and madmen to the same yoke.
We soon had a facility built. But we were still so secretive. As much as we wanted to shout from the rooftops what we had found, we were frightened, too, that it would be taken from us. We told ourselves it was just for the interim, until we were sure of our footing. We’d show them, eventually. We’d show them all.
We were careful, at first. We made small, inoffensive, or even helpful items. The fountain of youth. The bouncing ball. The Civil War statue.""")
        await ctx.channel.send(""" We grew more confident, and we started working on humans. The concrete man. He volunteered. Or the man with the abdominal planet. Just a drifter, but we made him something special, didn't we?
It was all so easy. Perhaps it seems absurd to get so many things from that one little break in reality, but it all flowed, one discovery to the next. It almost seemed like something was helping us along.
But then, things started going a bit wrong. While he was playing with his equations, Aaron accidentally derived the missing number. In my laboratory, I found I’d made the zombie plague. But we were too invested in our projects, so we pushed ahead. Then came the pipe nightmare, and the stairwell. We knew we’d need more help.
Thomas showed what we’d done to the military. Told them we’d \“found\” these things, discovered them. We made up names like \“Prometheus Labs,\” and \“the Chaos Insurgency.\” They gave us funding, personnel. We built up, and expanded outward. We repeated the sell in other countries. Some listened, some didn’t. Enough did. We became an international organization. We brought in more researchers, though very few ever suspected we were the source of these items they studied. Sometimes we would arrange for an object to be “found” by a field team, sometimes we would simply write the reports. We generated the paperwork, and we were the oversight. If we said a thing was, it was. It still is.
There were still problems, of course. Jeremy and Thomas took one of our experiments and ran off with it, creating their ridiculous club. One of our researchers grew mad and started worshipping machines, escaping with enough knowledge to be dangerous. We still deal with the fallout of these splinter groups.
So we contained them. We handled them. We couldn't stop, surely you can see that? Rather than more cautious, we grew bolder. I cut a little boy up and turned him into the Flesh That Hates.
There were reasons. There were always reasons. Two thirty-one.""")
        await ctx.channel.send(""" We created her, and her sisters. We took them from orphanages, and arranged for what followed. And it was no accident. We knew what we were doing. There was a reason for it once, but I’ll be damned if I can remember it now. None of us do, except maybe my brother, wherever, whatever he is now.
We keep moving forward. Even after Abel, after the blood pond, after that damnable reptile, we still move forward with our work. What else can we do? Our only hope to survive the events we’ve set in motion is to understand better, to learn more. We’re on the back of a terrible beast, and if we try to jump off now, we’ll be crushed beneath. But that’s not what frightens me, and it isn’t what should frighten you. We’ve maintained our foothold for over a hundred years.
The things I really worry about are the anomalies we didn't create. No, I was telling the truth the first time. We didn't discover any of them. But some of them, they aren't our work. They just… were, one day. They were in containment, and they'd always been in containment. Don't you see? We're not in control anymore. We never were.""")
def setup(client):
    client.add_cog(dossier(client))