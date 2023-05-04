import discord
from discord.ext import commands

class mtfs(commands.Cog):
    def __init__(self,client):
        self.client=client
    @commands.Cog.listener()
    async def on_ready(self):
        print('mtfs Cog Ready')

    @commands.command(aliases=[])
    async def mtfinfo(self,ctx):
        await ctx.channel.send("""Mobile Task Forces (MTFs) are elite units comprised of personnel drawn from across the Foundation and are mobilized to deal with specific threats or situations that sometimes exceed the operational capacity or expertise of regular field personnel and — as their name suggests — may be relocated between facilities or locations as they are needed. Mobile Task Force personnel represent the "best of the best" of the Foundation.
Mobile Task Forces vary greatly in size, composition, and purpose. A battalion-strength combat-oriented task force trained to deal with highly aggressive anomalous entities may consist of hundreds of troops plus support personnel, vehicles, and equipment and can be deployed in whole or in part to deal with threats across the globe. However, a Mobile Task Force can also be a small, specialized intelligence-gathering or investigative task force that may have fewer than a dozen personnel if that is deemed sufficient to accomplish their goals.
While in the field, task force members often pose as emergency responders, local or federal law enforcement, or military personnel appropriate to the region in which they are operating. Mobile Task Force Commanders can also request the assistance of local field units or personnel stationed at nearby Foundation facilities in order to accomplish their missions.
Organization
Each unit is fundamentally structured in a way that best suits their intended purpose. While combat-oriented task forces may closely follow military hierarchy and organization, smaller units may have an informal or otherwise esoteric chain of command. As such, the responsibilities of the Mobile Task Force Commander (MTFC) for each particular task force can vary greatly; the commander for a large task force might focus on maintaining multiple teams and deploying them as necessary to each assigned operation, whereas the commander of a small team might deploy with their team and direct the operation from on location.""")
        await ctx.channel.send("""
Similarly, the cohesion of each unit will vary as well. Some Mobile Task Forces consist of personnel who have trained and worked for many years or even decades together, whereas the personnel of a Mobile Task Force formed on a moment's notice to deal with a specific incident may know little more than each others' names and fields of expertise.
Creation
Mobile Task Forces are typically commissioned as deemed necessary by the Foundation's Director of Task Forces, often with the direct approval of one or more O5 Council members. A significant number of Mobile Task Forces are created to deal with specific anomalies exhibiting traits that standard containment or response teams are unable to effectively counteract, though many were also created to pre-empt an emerging or theoretical threat.
Deactivation
Mobile Task Forces created for the purpose of containing a particular anomaly are typically deactivated at the end of the recovery operation or when ongoing containment is deemed no longer necessary. Occasionally, such task forces remain operational if the expertise and experiences learned are considered useful for future incidents, but otherwise the task force will likely be disbanded and its personnel returned to their prior posts. Very rarely, a Mobile Task Force will also be disbanded if it suffers sufficient casualties to render it incapable of operation. In these cases, if the prior capability of that particular task force is deemed necessary, a new task force may be commissioned to replace it.""")
    @commands.command(aliases=['redrighthand', 'alpha-1'])
    async def alpha1(self,ctx):
        await ctx.channel.send("""Task Force Mission: Mobile Task Force Alpha-1 (Red Right Hand) is a task force that reports directly to the O5 Council and is used in situations that require the strictest operational security. The task force consists of the Foundation's best and most loyal operatives, and serves as the O5 Council's special operations unit. Further information regarding MTF Alpha-1 is classified Level 5.
Assisting In Containment of Objects:
SCP-001: Dead Men
SCP-001: MAMJUL & KORAR
SCP-2271
SCP-3434
SCP-3499
SCP-3741
SCP-3791
SCP-4470
SCP-5008
SCP-5105
SCP-5920
SCP-7001
SCP-7760
https://media.discordapp.net/attachments/812131957692694528/1099121878343360573/small.png?width=300&height=300""")
    @commands.command(aliases=['ponyexpress', 'alpha-4'])
    async def alpha4(self,ctx):
        await ctx.channel.send("""Task Force Mission: Mobile Task Force Alpha-4 (Pony Express) consists primarily of personnel trained to act as undercover employees and specialize in tracking, intercepting, and securing anomalous objects sent through postal and package delivery services worldwide.
Assisting In Containment of Objects:
SCP-111
SCP-130
SCP-360
SCP-2177
SCP-2577
SCP-2752
SCP-3060
SCP-3512
SCP-3601
SCP-4209
SCP-5430
https://scp-wiki.wdfiles.com/local--resized-images/task-forces/Alpha4.png/small.jpg""")
    @commands.command(aliases=['lasthope', 'alpha-9'])
    async def alpha9(self,ctx):
        await ctx.channel.send("""Task Force Mission: The reborn Omega-7.  Mobile Task Force Alpha-9 (Last Hope) is explicitly intended to train and utilize humanoid SCP objects in the field.
Utilizing Objects:
SCP-073
SCP-105
SCP-2913
SCP-2987
SCP-4051
SCP-4494
SCP-4818
SCP-7414-A
Assisting In Containment of Objects:
SCP-5025
https://scp-wiki.wdfiles.com/local--resized-images/task-forces/Alpha9.png/small.jpg""")
    @commands.command(aliases=['bayouboys', 'beta-2'])
    async def beta2(self,ctx):
        await ctx.channel.send("""Task Force Mission: Region-specific task force MTF Beta-2 (Bayou Boys) is based in Louisiana. Trained to act in swamp/wetland environments.
Assisting In Containment of Objects:
SCP-4421
SCP-4476
SCP-5038
SCP-5138
https://scp-wiki.wdfiles.com/local--files/task-forces/Beta2.png""")
    @commands.command(aliases=['castaways', 'beta-4'])
    async def beta4(self,ctx):
        await ctx.channel.send("""Task Force Mission: MTF Beta-4 (Castaways) is a task force created with the sole purpose of assisting and monitoring GoI-466 (Wilson's Wildlife Solutions) in their interactions with local fauna-based anomalies.
Assisting In Containment of Objects:
SCP-3465
SCP-3466
SCP-3467
SCP-3577
SCP-3676
SCP-3879
https://scp-wiki.wdfiles.com/local--resized-images/task-forces/Beta4.png/small.jpg""")
    @commands.command(aliases=['mazhatters', 'beta-7'])
    async def beta7(self,ctx):
        await ctx.channel.send("""Task Force Mission: Mobile Task Force Beta-7 (Maz Hatters) specializes in the acquisition and containment of anomalies exhibiting extreme biological, chemical, or radiological hazards as well as the rapid containment and cleanup of areas affected by such anomalies. This includes the planning and deployment of contingencies for wide-area or pandemic spread of anomalous disease agents or other contagious phenomena.
Assisting In Containment of Objects:
SCP-400
SCP-550
SCP-1280
SCP-1393
SCP-2133
SCP-2376
SCP-2438
SCP-2810
SCP-3016
SCP-4771
SCP-5397
SCP-6118
https://scp-wiki.wdfiles.com/local--resized-images/task-forces/Beta7.png/small.jpg""")
    @commands.command(aliases=['hecatesspear', 'beta-777'])
    async def beta777(self,ctx):
        await ctx.channel.send("""Task Force Mission: MTF Beta-777 (Hecate's Spear) specializes in thaumaturgical ritual analysis and countermeasures; including thaumaturgical combat. Based out of Site-91.
Assisting In Containment of Objects:
SCP-3743
SCP-4612
SCP-4712
SCP-5079
SCP-5512
SCP-5626
SCP-5923
SCP-5957
SCP-6094
SCP-6364
https://scp-wiki.wdfiles.com/local--resized-images/task-forces/Beta777.png/small.jpg""")
    @commands.command(aliases=['blondebeardscrew', 'gamma-4'])
    async def gamma4(self,ctx):
        await ctx.channel.send("""Task Force Mission: MTF Gamma-4 (Blondebeard's Crew) is a five-man task force specialized in performing tasks in low to zero-gravity and vacuum environments. Based out of Lunar Area-32.
Assisting In Containment of Objects:
SCP-2493
SCP-3609""")
    @commands.command(aliases=['redherrings', 'gamma-5'])
    async def gamma5(self,ctx):
        await ctx.channel.send("""Task Force Mission: Mobile Task Force Gamma-5 (Red Herrings) specializes in preventing the dissemination of knowledge of anomalous events or phenomena in cases where initial suppression efforts have proven ineffective or insufficient, or in cases where such knowledge has already reached critical levels of public exposure. This includes the research and deployment of experimental amnestics as well as memory fabrication procedures.Assisting In Containment of Objects:
SCP-1086
SCP-1110
SCP-1460
SCP-1532
SCP-1548
SCP-1570
SCP-1618
SCP-1670
SCP-2105
SCP-2342
SCP-2631
SCP-3339
SCP-3666
SCP-4039
SCP-4160
SCP-5060
SCP-5479
SCP-5916
https://scp-wiki.wdfiles.com/local--resized-images/task-forces/Gamma5.png/small.jpg""")
    @commands.command(aliases=['deepfeeders', 'gamma-6'])
    async def gamma6(self,ctx):
        await ctx.channel.send("""Task Force Mission: Mobile Task Force Gamma-6 (Deep Feeders) specializes in the investigation and tracking of deep-sea or oceanic anomalies.
Assisting In Containment of Objects:
SCP-169
SCP-879
SCP-1264
SCP-1409
SCP-2120
SCP-2770
SCP-2956
SCP-3069
SCP-5533
SCP-6055
https://scp-wiki.wdfiles.com/local--resized-images/task-forces/Gamma6.png/small.jpg""")
    @commands.command(aliases=['asimovslawbringers', 'gamma-13'])
    async def gamma13(self,ctx):
        await ctx.channel.send("""Task Force Mission: Mobile Task Force Gamma-13 (Asimov's Lawbringers) specializes in the investigation, tracking, and apprehension of anomalous objects, persons, and entities associated with GoI-1115 (Anderson Robotics). This includes identification of Anderson customers, location of Anderson products and conduction of raids on Anderson offices.
Assisting In Containment of Objects:
SCP-2306
SCP-2806
SCP-2906
SCP-3560
SCP-6660
SCP-750-KO
https://scp-wiki.wdfiles.com/local--resized-images/task-forces/Gamma13.png/small.jpg""")
    @commands.command(aliases=['frontrunners', 'delta-5'])
    async def delta5(self,ctx):
        await ctx.channel.send("""Task Force Mission: Mobile Task Force Delta-5 (Front Runners) is comprised of multiple autonomous deep-cover cells specializing in the identification and pre-emptive acquisition of anomalous objects and entities of interest to other Groups of Interest.
Assisting In Containment of Objects:
SCP-185
SCP-472
SCP-1139
SCP-5071
https://scp-wiki.wdfiles.com/local--resized-images/task-forces/Delta5.png/small.jpg""")
    @commands.command(aliases=['winterwonderland', 'delta-14'])
    async def delta14(self,ctx):
        await ctx.channel.send("""Task Force Mission: Task force Delta-14 (Winter Wonderland) specializes in handling and containing anomalies in subzero or cold environments, or anomalies related to snow.
Assisting In Containment of Objects:
SCP-4230
SCP-5140
SCP-5392
https://scp-wiki.wdfiles.com/local--files/task-forces/Delta14.png""")
    @commands.command(aliases=['villageidiots', 'epsilon-6'])
    async def epsilon6(self,ctx):
        await ctx.channel.send("""Task Force mission: MTF Epsilon-6 (Village Idiots) specializes in the investigation, containment, and subsequent cleanup of anomalies in rural and suburban environments.
Assisting In Containment of Objects:
SCP-2447
SCP-2480
SCP-2561
SCP-2815
SCP-3322
SCP-3449
SCP-3845
Undefined
SCP-4709
SCP-4775
SCP-5000
SCP-5536
SCP-5700
SCP-5820
SCP-5910
SCP-6186
SCP-6619
SCP-6717
https://scp-wiki.wdfiles.com/local--resized-images/task-forces/Epsilon6.png/small.jpg""")
    @commands.command(aliases=['forgetmenots', 'epsilon-7'])
    async def epsilon7(self,ctx):
        await ctx.channel.send("""Task Force Mission: MTF Epsilon-7 (Forget Me Nots) deals with the undercover disruption of the research and development of mnestic drugs.
Assisting In Containment of Objects:
SCP-2111
SCP-2828
SCP-2358
SCP-2438
SCP-4144""")
    @commands.command(aliases=['fireeaters', 'epsilon-9'])
    async def epsilon9(self,ctx):
        await ctx.channel.send("""Task Force mission: Epsilon-9 (Fire Eaters) specializes in the use of incendiary weaponry and operations in high-temperature environments.
Assisting In Containment of Objects:
SCP-165
SCP-262
SCP-968
SCP-2340
SCP-3205
SCP-4111
https://scp-wiki.wdfiles.com/local--resized-images/task-forces/Epsilon9.png/small.jpg""")
    @commands.command(aliases=['ninetailedfox', 'epsilon-11'])
    async def epsilon11(self,ctx):
        await ctx.channel.send("""Task Force Mission: Mobile Task Force Epsilon-11 (Nine Tailed Fox) handles internal security for the SCP Foundation, under oversight by MTF Alpha-1. They are a special ops force deployed to Foundation Sites when standard protocols fail and multiple breaches are imminent. As such, most of their operations are classified.
Assisting In Containment of Objects:
SCP-2139
SCP-2479
SCP-3030
SCP-4171
SCP-4511
SCP-5018
SCP-5254
https://scp-wiki.wdfiles.com/local--resized-images/task-forces/Epsilon11.png/small.jpg""")
    @commands.command(aliases=['molerats', 'zeta-9'])
    async def zeta9(self,ctx):
        await ctx.channel.send("""Task Force Mission: Mobile Task Force Zeta-9 (Mole Rats) specializes in the investigation, exploration, and containment of underground or enclosed areas exhibiting anomalous phenomena, particularly those with inconsistent topography or unstable spacetime.
Assisting In Containment of Objects:
SCP-001: AMONI-RAM
SCP-184
SCP-455
SCP-835
SCP-1162
SCP-1444
SCP-1730
SCP-2518
SCP-2591
SCP-2955
SCP-3066
SCP-3512
SCP-3667
SCP-5015
SCP-5100
SCP-5392
SCP-5653
SCP-5992
SCP-6991
https://scp-wiki.wdfiles.com/local--resized-images/task-forces/Zeta9.png/small.jpg""")
    @commands.command(aliases=['begonethoth', 'eta-4'])
    async def eta4(self,ctx):
        await ctx.channel.send("""Task Force Mission: Mobile Task Force Eta-4 (Begone Thoth) is a unit of intelligent SCP-3095-affected seabirds. Eta-4 specializes in information collection and analysis, complementary field research and support, and in extreme cases, airborne combat. The task force was ultimately charged with protecting humanity after the BE-Class "Migration" End-of-Consciousness Scenario.
Assisting In Containment of Objects:
EE-3570
SCP-4688
SCP-5106
https://scp-wiki.wdfiles.com/local--resized-images/task-forces/Eta4.png/small.jpg""")
    @commands.command(aliases=['jaegerbombers', 'eta-5'])
    async def eta5(self,ctx):
        await ctx.channel.send("""Task Force Mission: Mobile Task Force Eta-5 (Jaeger Bombersis a rapid-response unit specializing in the tracking, capturing, and containment of Large-Scale Aggressors (entities over 30m in height). Deploys from, and detains LSAs within Dimensional-Site-172.
Assisting In Containment of Objects:
SCP-2764
SCP-3534
SCP-4315
SCP-5391
SCP-5514
https://scp-wiki.wdfiles.com/local--resized-images/task-forces/Eta5.png/small.jpg""")
    @commands.command(aliases=['seenoevil', 'eta-10'])
    async def eta10(self,ctx):
        await ctx.channel.send("""Task Force Mission: Mobile Task Force Eta-10 (See No Evil) specializes in the investigation, acquisition, and initial containment of objects or entities exhibiting visual cognitohazards, visual memetic agents, or otherwise require indirect or alternative observation in order to safely handle.
Assisting In Containment of Objects:
SCP-020
SCP-125
SCP-571
SCP-904
SCP-1561
SCP-2136
SCP-2140
SCP-2155
SCP-2828
SCP-3393
SCP-3519
SCP-3597
SCP-4149
SCP-4550
SCP-4600
SCP-4879
SCP-5052
SCP-6178
https://scp-wiki.wdfiles.com/local--resized-images/task-forces/Eta10.png/small.jpg""")
    @commands.command(aliases=['savagebeasts', 'eta-11'])
    async def eta11(self,ctx):
        await ctx.channel.send("""Task Force Mission: Mobile Task Force Eta-11 (Savage Beasts) specializes in the investigation, acquisition, and containment of auditory and musical anomalies, including any auditory cognitohazards or sound-based anomalous threats.
Assisting In Containment of Objects:
SCP-1687
SCP-1844
SCP-2402
SCP-2828
SCP-3447
SCP-3519
SCP-4150
SCP-4614
https://scp-wiki.wdfiles.com/local--resized-images/task-forces/Eta11.png/small.jpg""")
    @commands.command(aliases=['sphereswithinspheres', 'eta-77'])
    async def eta77(self,ctx):
        await ctx.channel.send("""Task Force Mission: MTF Eta-77 (Spheres Within Spheres) is The Department of Tactical Theology's personalized operational unit, consisting of fifteen specialized members. All personnel in the task force have expertise in dealing with aggressive or threatening religion-related anomalies.
Assisting In Containment of Objects:
SCP-4531
SCP-5327
SCP-5993
SCP-6542
SCP-6777
https://scp-wiki.wdfiles.com/local--resized-images/task-forces/Eta77.png/small.jpg""")
    @commands.command(aliases=['gardners', 'theta-4'])
    async def theta4(self,ctx):
        await ctx.channel.send("""Task Force Mission: Mobile Task Force Theta-4 (Gardners) specializes in the acquisition and containment of plant or plant-like anomalous objects and entities, especially fieldwork involving wide-spread infestations of such anomalies.
Assisting In Containment of Objects:
SCP-628
SCP-1147
SCP-1255
SCP-1262
SCP-1717
SCP-2108
SCP-3215
SCP-3421
SCP-6880
SCP-6896
https://scp-wiki.wdfiles.com/local--resized-images/task-forces/Theta4.png/small.jpg""")
    @commands.command(aliases=['thebiggerboat', 'theta-5'])
    async def theta5(self,ctx):
        await ctx.channel.send("""Task Force Mission: MTF Theta-5 (The Bigger Boat) specializes in anomalies involving or threatening marine vehicles.
Assisting In Containment of Objects:
SCP-1373
SCP-1409
SCP-1568
SCP-2162
SCP-3057""")
    @commands.command(aliases=['anglegrinders', 'theta-90'])
    async def theta90(self,ctx):
        await ctx.channel.send("""Task Force Mission: Mobile Task Force Theta-90 (Angle Grinders), specialize in operating in locations of anomalous topology/geometry and in securing anomalies connected with these kinds of spacetime distortions.
Assisting In Containment of Objects:
SCP-1707
SCP-2601
SCP-3307
SCP-4037
SCP-4096
SCP-4104
https://scp-wiki.wdfiles.com/local--resized-images/task-forces/Theta90.png/small.jpg""")
    @commands.command(aliases=['damnfeds', 'iota-10'])
    async def iota10(self,ctx):
        await ctx.channel.send("""Task Force Mission: Mobile Task Force Iota-10 (Damn Feds) maintains undercover operatives in various international, federal, and provincial law enforcement agencies and specializes in facilitating the transfer of anomalous evidence and objects into Foundation control as well as the transfer of jurisdiction over anomalous event locations from local law enforcement to Foundation containment and response teams.
Assisting In Containment of Objects:
SCP-210
SCP-437
SCP-1243
SCP-1359
SCP-2036
SCP-2578
SCP-2890
SCP-2942
SCP-3117
SCP-3155
SCP-3458
SCP-3183
SCP-4581
SCP-5177
SCP-5617
https://scp-wiki.wdfiles.com/local--resized-images/task-forces/Iota10.png/small.jpg""")
    @commands.command(aliases=['skynet', 'kappa-10'])
    async def kappa10(self,ctx):
        await ctx.channel.send("""Task Force Mission: Mobile Task Force Kappa-10 (Skynet) is a temporary designation until such time it is either officially dissolved or sanctioned. It is strictly tasked in investigating and engaging 'cyber-anomalies' using a combination of virtual agents (AICs) and Foundation researchers to track, neutralize, and/or contain such intangible threats.
Assisting In Containment of Objects:
SCP-2522
SCP-2806
SCP-2987
SCP-3090
SCP-3323
SCP-3959
SCP-4950
SCP-5018
SCP-5860
https://scp-wiki.wdfiles.com/local--resized-images/task-forces/Kappa10.png/small.jpg""")
    @commands.command(aliases=['themediators', 'kappa-43'])
    async def kappa43(self,ctx):
        await ctx.channel.send("""Task Force Mission: MTF Kappa-43 (The Mediators) specialize in the investigation, tracking, and apprehension of anomalous objects and media associated with GoI-5889 (Vikander-Kneed Technical Media) and amnestization of any witnesses.
Assisting In Containment of Objects:
SCP-5358
SCP-5379
SCP-5571
SCP-5681
SCP-5698
SCP-5974
SCP-6121
SCP-6123
SCP-6677""")
    @commands.command(aliases=['birdwatchers', 'lambda-4'])
    async def lambda4(self,ctx):
        await ctx.channel.send("""Task Force Mission: Mobile Task Force Lambda-4 (Birdwatchers) specializes in the identification, tracking, and containment of airborne biological anomalies, especially anomalous avian organisms.
Assisting In Containment of Objects:
SCP-514
SCP-1476
SCP-1505
SCP-1560
SCP-2760
SCP-2967
SCP-3497
SCP-5447
https://scp-wiki.wdfiles.com/local--resized-images/task-forces/Lambda4.png/small.jpg""")
    @commands.command(aliases=['whiterabbits', 'lambda-5'])
    async def lambda5(self,ctx):
        await ctx.channel.send("""Task Force Mission: Mobile Task Force Lambda-5 (White Rabbits) specializes in traversing unstable, surreal, and controlled reality, and containing potentially dangerous persons and artifacts capable of manipulating space and time.
Assisting In Containment of Objects:
SCP-2446
SCP-3087
SCP-4507
https://scp-wiki.wdfiles.com/local--resized-images/task-forces/Lambda5.png/small.jpg""")
    @commands.command(aliases=['pestcontrol', 'lambda-12'])
    async def lambda12(self,ctx):
        await ctx.channel.send("""Task Force Mission: MTF Lambda-12 (Pest Control) specializes in tracking, containing, and exterminating anomalous vermin. Often used as a first-response team when tracking anomalous organisms.
Assisting In Containment of Objects:
SCP-2350
SCP-2810
SCP-3470
SCP-3640
SCP-4310
SCP-4749
SCP-6092
https://scp-wiki.wdfiles.com/local--resized-images/task-forces/Lambda12.png/small.jpg""")
    @commands.command(aliases=['onestarreviewers', 'lambda-14'])
    async def lambda14(self,ctx):
        await ctx.channel.send("""Task Force Mission: Task force Lambda-14 (One Star Reviewers) specializes in dealing with retail-oriented locations and anomalies, be they singular restaurants or entire shopping districts displaying anomalies. Since their initial investigation of The Ambrose Restaurant, MTF Lambda-14 has been assigned to work to combat this group.
For more information on this task force, see the Ambrose Restaurants Dossier.
Assisting In Containment of Objects:
SCP-4348
SCP-4554
SCP-5516
SCP-5559-D
https://scp-wiki.wdfiles.com/local--resized-images/task-forces/Lambda14.png/small.jpg""")
    @commands.command(aliases=['highestbidders', 'mu-3'])
    async def mu3(self,ctx):
        await ctx.channel.send("""Task Force Mission: Mobile Task Force Mu-3 (Highest Bidders) is dedicated to monitoring GoI 'Marshall, Carter & Dark Ltd'. Through the combined efforts of undercover agents and covert-ops specialists, their objective is: identifying objects of interest in possession of Marshall, Carter and Dark; isolating opportunities to recover these objects; and, ultimately achieving their containment.
Assisting In Containment of Objects:
SCP-2423
SCP-2463
SCP-2818
SCP-5169
SCP-6140
https://scp-wiki.wdfiles.com/local--resized-images/task-forces/Mu3.png/small.jpg""")
    @commands.command(aliases=['debuggers', 'mu-4'])
    async def mu4(self,ctx):
        await ctx.channel.send("""Task Force Mission: Mobile Task Force Mu-4 (Debuggers) specializes in the identification, tracking, retrieval, and containment of electronic devices and transmissions, especially anomalous computers and network-related anomalies. This includes the investigation of internet sites suspected of anomalous capabilities or involved in anomalous events.
Assisting In Containment of Objects:
SCP-155
SCP-892
SCP-896
SCP-1290
SCP-1866
SCP-2160
SCP-2223
SCP-2698
SCP-2738
SCP-2876
SCP-2890
SCP-3030
SCP-3045
SCP-3089
SCP-3101
SCP-3334
SCP-3858
https://scp-wiki.wdfiles.com/local--resized-images/task-forces/Mu4.png/small.jpg""")
    @commands.command(aliases=['ghostbusters', 'mu-13'])
    async def mu13(self,ctx):
        await ctx.channel.send("""Task Force Mission: Mobile Task Force Mu-13 (Ghostbusters) specializes in the tracking, analysis, and containment of incorporeal or intangible manifestations and entities, particularly those believed to be sentient, sapient, or otherwise intelligent and adaptive.
Assisting In Containment of Objects:
SCP-128
SCP-460
SCP-1036
SCP-2227
SCP-3371
SCP-4973
SCP-5230
SCP-5685
SCP-6403
SCP-6501
https://scp-wiki.wdfiles.com/local--resized-images/task-forces/Mu13.png/small.jpg""")
    @commands.command(aliases=['hammerdown', 'nu-7'])
    async def nu7(self,ctx):
        await ctx.channel.send("""Task Force Mission: Armed Mobile Task Force Nu-7 (Hammer Down) is a battalion-strength force consisting of three company-sized elements of special operations infantry forces, a light armored vehicle company, tank platoon, helicopter squadron, chemical-biological-radiological-nuclear (CBRN) platoon, combat engineer platoon, nuclear weapon specialist (NWS) squad, plus additional combat specialist and support personnel. AMTF Nu-7 is based primarily out of Armed Bio-Containment Area-14 and is tasked with responding to incidents involving loss of communication with major Foundation facilities under circumstances wherein a site-wide breach, enemy compromise, or other similarly catastrophic event is suspected.
Assisting In Containment of Objects:
SCP-939
SCP-1105
SCP-1943
SCP-2128
SCP-2546
SCP-2660
SCP-2706
SCP-2803
SCP-3221
SCP-4290
SCP-4297
SCP-6644
https://scp-wiki.wdfiles.com/local--resized-images/task-forces/Nu7.png/small.jpg""")
    @commands.command(aliases=['dreamteam'])
    async def omicronrho(self,ctx):
        await ctx.channel.send("""Task Force Mission: The Foundation has discovered the method of becoming Oneiroi, and now with this power are more capable of containing them. For decades they teach their agents the technique that allows one consciousness to join another’s. The few mentally hardened individuals that succeed are organized into a task force. The first of these was Mobile Task Force Omicron Rho.
Assisting In Containment of Objects:
SCP-1394
SCP-2144
SCP-2235
SCP-2603
SCP-2934
SCP-2942
SCP-3060
https://scp-wiki.wdfiles.com/local--resized-images/task-forces/OmicronRho.png/small.jpg""")
    @commands.command(aliases=['cityslickers', 'pi-1'])
    async def pi1(self,ctx):
        await ctx.channel.send("""Task Force Mission: Mobile Task Force Pi-1 (City Slickers) specializes in the investigation, containment, and subsequent cleanup of anomalies in densely-populated urban environments, particularly in the New York metropolitan area.
Assisting In Containment of Objects:
SCP-274
SCP-602
SCP-1155
SCP-1219
SCP-1388
SCP-2162
SCP-2409
SCP-2890
SCP-2990
SCP-3335
SCP-3360
SCP-3597
SCP-4051
SCP-5151
SCP-5841
https://scp-wiki.wdfiles.com/local--resized-images/task-forces/Pi1.png/small.jpg""")
    @commands.command(aliases=['theprofessers', 'rho-1'])
    async def rho1(self,ctx):
        await ctx.channel.send("""Task Force Mission: Mobile Task Force Rho-1 (The Professers) specializes in the acquisition, containment, and transport of anomalies related to Group of Interest Alpha-388, "Alexylva University". With the reduction of the threat posed by the specific GoI, the MTF has expanded its focus to any and all containment for anomalous academic endeavors.
Assisting In Containment of Objects:
SCP-877
SCP-1546
SCP-3138
SCP-4028
SCP-4218
SCP-5179
https://scp-wiki.wdfiles.com/local--resized-images/task-forces/Rho1.png/small.jpg""")
    @commands.command(aliases=['technicalsupport', 'rho-9'])
    async def rho9(self,ctx):
        await ctx.channel.send("""Task Force Mission: Mobile Task Force Rho-9 (Technical Support) handles computer security for the Foundation. When memetic kill agents can lurk throughout the data structure, this is no simple task.
Assisting In Containment of Objects:
SCP-1549
SCP-2234
SCP-4550
SCP-5018
https://scp-wiki.wdfiles.com/local--resized-images/task-forces/Rho9.png/small.jpg""")
    @commands.command(aliases=['cythereans', 'rho-19'])
    async def rho19(self,ctx):
        await ctx.channel.send("""Task Force Mission: Mobile Task Force Rho-19 (Cythereans) has been sent to Venus, in the hopes to establish a Foundation presence where there may be considerable anomalous activity.
Assisting In Containment of Objects:
SCP-2474
https://scp-wiki.wdfiles.com/local--resized-images/task-forces/Rho19.png/small.jpg""")
    @commands.command(aliases=['bibliographers', 'sigma-3'])
    async def sigma3(self,ctx):
        await ctx.channel.send("""Task Force Mission: Mobile Task Force Sigma-3 (Bibliographers) is charged with covert infiltration of the anomalous community for the purpose of gathering intel, with a particular focus on the vast otherworldly location of The Wanderers' Library.
Assisting In Containment of Objects:
SCP-472
SCP-1591
SCP-2975
SCP-3591
SCP-5917
SCP-6000
https://scp-wiki.wdfiles.com/local--resized-images/task-forces/Sigma3.png/small.jpg""")
    @commands.command(aliases=['valkyries', 'sigma-9'])
    async def sigma9(self,ctx):
        await ctx.channel.send("""Task Force Mission: MTF Sigma-9 (Valkyries) is a small unit providing air support for ground operations or combat against aerial anomalies.
Assisting In Containment of Objects:
SCP-526
SCP-1262
SCP-2069
https://scp-wiki.wdfiles.com/local--files/task-forces/Sigma9.png""")
    @commands.command(aliases=['theslothsarm', 'sigma-10'])
    async def sigma10(self,ctx):
        await ctx.channel.send("""Task Force Mission: Based at Site-87, MTF Sigma-10 (The Sloths Arm) is dedicated to the containment of dangerous anomalies within Nexus-18, better known as Sloth's Pit, Wisconsin.
Assisting In Containment of Objects:
SCP-4040""")
    @commands.command(aliases=['sixteentons', 'sigma-66'])
    async def sigma66(self,ctx):
        await ctx.channel.send("""Task Force Mission: Mobile Task Force Sigma-66 (Sixteen Tons) is formed of captured members from other GoI. Despite the lack of loyalty the Foundation expects from the assembled team, they find the members' expertise of value.
https://scp-wiki.wdfiles.com/local--resized-images/task-forces/Sigma66.png/small.jpg""")
    @commands.command(aliases=['samsara', 'tau-5'])
    async def tau5(self,ctx):
        await ctx.channel.send("""Task Force Mission: Immortal cyborg clones created from the flesh of a dead god, Tau-5 (Samsara) utilizes esoteric and experimental Foundation weaponry to investigate and contain thaumaturgic, magical, and psionic threats.
Assisting In Containment of Objects:
SCP-1730
SCP-2621
SCP-2970
SCP-3780
SCP-4755
SCP-6442
https://scp-wiki.wdfiles.com/local--resized-images/task-forces/Tau5.png/small.jpg""")
    @commands.command(aliases=['bookworms', 'tau-9'])
    async def tau9(self,ctx):
        await ctx.channel.send("""Task Force Mission: MTF Tau-9 (Bookworms) deals with anomalies related to the Library, the Serpent's Hand, and 'magic'; A more traditional counterpart to Sigma-3.
Assisting In Containment of Objects:
SCP-2546
SCP-3743
SCP-5267
SCP-6237
https://scp-wiki.wdfiles.com/local--resized-images/task-forces/Tau9.png/small.jpg""")
    @commands.command(aliases=['urbanbrawl', 'tau-51'])
    async def tau51(self,ctx):
        await ctx.channel.send("""Task Force Mission: MTF Tau-51 (Urban Brawl) specializes in the containment and recovery of SCP objects from urban environments, especially the Three Portlands Location of Interest.
Assisting In Containment of Objects:
SCP-3560
SCP-3960
SCP-4160
SCP-4660
SCP-5460
SCP-6560
SCP-6660
https://scp-wiki.wdfiles.com/local--files/task-forces/Tau51.png""")
    @commands.command(aliases=['sugarpill', 'upsilon-4'])
    async def upsilon4(self,ctx):
        await ctx.channel.send("""Task Force Mission: Originally formed in order to contain SCP-2559, Mobile Task Force Upsilon-4 (Sugar Pill) is tasked with epidemiological containment, especially with the containment of memetic outbreaks.
Assisting In Containment of Objects:
SCP-2350
SCP-2546
SCP-2559
SCP-3519
SCP-6364
https://scp-wiki.wdfiles.com/local--resized-images/task-forces/Upsilon4.png/small.jpg""")
    @commands.command(aliases=['clevergirls', 'phi-2'])
    async def phi2(self,ctx):
        await ctx.channel.send("""Task Force Mission: MTF Phi-2 (Clever Girls) specializes in the study, tracking, capture, and hunting of prehistoric anomalies, especially dinosaurs.
Assisting In Containment of Objects:
SCP-3057
SCP-3467
SCP-3659
SCP-3934
SCP-4041
SCP-4131
SCP-5533
SCP-5893
https://scp-wiki.wdfiles.com/local--resized-images/task-forces/Phi2.png/small.jpg""")
    @commands.command(aliases=['providenttrawlers', 'phi-eolh'])
    async def phieolh(self,ctx):
        await ctx.channel.send("""Task Force Mission: MTF Phi-Eolh (Provident Trawlers_ specially trained agents armed with amnestics, tasked with covertly retrieving civilians with anomalous connections from the general populace.
Assisting In Containment of Objects:
SCP-3617
SCP-3716
SCP-3723
SCP-4668""")
    @commands.command(aliases=['lasttofall', 'xi-8'])
    async def xi8(self,ctx):
        await ctx.channel.send("""Task Force Mission: Mobile Task Force Xi-8 (Last To Fall) is a battalion-strength task force dedicated to the acquisition and/or termination of Sarkic entities and artifacts. Created as a response to the growing Sarkic threat, Xi-8's operational scope encompasses all six major continents, with naval support provided by the Foundation as needed.
Assisting In Containment of Objects:
SCP-238
SCP-3911
SCP-5038
SCP-5407
https://scp-wiki.wdfiles.com/local--files/task-forces/Xi8.png""")
    @commands.command(aliases=['plaguetamers', 'chi-7'])
    async def chi7(self,ctx):
        await ctx.channel.send("""Task Force Mission: MTF Chi-7 (Plague Tamers) specializes in the containment of microbiological, biochemical, and pathogenic anomalies.
Assisting In Containment of Objects:
SCP-2381
SCP-2431
SCP-2546
SCP-2870""")
    @commands.command(aliases=['pageturners', 'chi-9'])
    async def chi9(self,ctx):
        await ctx.channel.send("""Task Force Mission: MTF Chi-9 (Page Turners) specializes in the detection, recovery, and neutralisation of anomalous literature.
Assisting In Containment of Objects:
SCP-3317
SCP-3716
SCP-4177
SCP-5790
https://scp-wiki.wdfiles.com/local--files/task-forces/Chi9.png""")
    @commands.command(aliases=['homeimprovment', 'psi-7'])
    async def psi7(self,ctx):
        await ctx.channel.send("""Task Force Mission: Mobile Task Force Psi-7 (Home Improvement) specializes in the undercover investigation, containment, and/or demolition of anomalous buildings or buildings affected by anomalies, particularly residential homes in populated areas. This includes the acquisition or transfer of affected buildings to Foundation control as well as initial observation and documentation of such buildings prior to transfer to local containment teams for long-term or ongoing containment.
Assisting In Containment of Objects:
SCP-574
SCP-744
SCP-941
SCP-1452
SCP-1684
SCP-1967
SCP-2215
SCP-2281
SCP-2311
SCP-2407
SCP-2426
SCP-2490
SCP-2891
SCP-2975
SCP-3050
SCP-3970
SCP-4480
SCP-4572
SCP-5028
SCP-5421
SCP-7991
https://scp-wiki.wdfiles.com/local--resized-images/task-forces/Psi7.png/small.jpg""")
    @commands.command(aliases=['thesilencers', 'psi-8'])
    async def psi8(self,ctx):
        await ctx.channel.send("""Task Force Mission: Mobile Task Force Psi-8 (The Silencers) specializes in the investigation, tracking, containment and/or destruction of individuals suspected to be capable of or having been affected by reanimation anomalies, as well as investigating suspected cases of communication with deceased individuals. This includes the severing of devices intended to allow communication with individuals buried alive, such as bells, pipes, and phones, as well as detainment and interrogation of individuals claiming to have had contact with deceased individuals.
Assisting In Containment of Objects:
SCP-565
SCP-2158
SCP-2922
SCP-3591
SCP-3914
SCP-4175
SCP-6944
https://scp-wiki.wdfiles.com/local--resized-images/task-forces/Psi8.png/small.jpg""")
    @commands.command(aliases=['witchhunters', 'psi-13'])
    async def psi13(self,ctx):
        await ctx.channel.send("""Task Force Mission: A highly classified joint Foundation/GOC task force. MTF Psi-13 (Witch Hunters) is designed for the infiltration of Sarkic organizations and the termination of high threat members. Operatives are trained in Counter Occult Stratagems (COS) and the use of corrosive/incendiary armaments.
Assisting In Containment of Objects:
SCP-2408
SCP-2815
https://scp-wiki.wdfiles.com/local--files/task-forces/Psi13.png""")
    @commands.command(aliases=['araorun', 'omega-0'])
    async def omega0(self,ctx):
        await ctx.channel.send("""Task Force Mission: The "saints" of MTF Omega-0 (Ara Orun) are informational constructs with the memories of deceased Foundation personnel able to manifest through access of the Foundation's intranet terminals. Using Identity Warfare Training (IWT) they protect their living comrades against informational threats and entities. The existence of MTF ω-0 is unknown to most or all of the living members of the Foundation.
Assisting In Containment of Objects:
SCP-1463
SCP-2111
SCP-2759
SCP-3664
https://scp-wiki.wdfiles.com/local--resized-images/task-forces/Omega0.png/small.jpg""")
    @commands.command(aliases=[])
    async def omega1(self,ctx):
        await ctx.channel.send("""Task Force Mission: MTF Omega-1 (Laws Left Hand) is empowered to remove or execute high-ranking Foundation personnel if they are determined to be acting unethically. Answers only to the Ethics Committee; counterpart to the O5's "Red Right Hand".
Known Deployments:
SCP-001: Dead Men
SCP-4263
SCP-4339
https://scp-wiki.wdfiles.com/local--files/task-forces/Omega1.png""")
    @commands.command(aliases=['pandorasbox', 'omega-7'])
    async def omega7(self,ctx):
        await ctx.channel.send("""~~Task Force Mission: Mobile Task Force Omega-7 (Pandora's Box) is an experimental task force specializing in the acquisition and containment of anomalies utilizing cooperative anomalous humanoid entities, particularly SCP-076 and SCP-105.~~ Mobile Task Force Omega-7 has been disbanded and decommissioned; this entry is to be deleted by order of the Records and Information Security Administration.
~~Utilizing Objects:~~
~~SCP-076~~
~~SCP-105~~
~~SCP-657~~
Assisting In Containment of Objects:
SCP-175
SCP-354
SCP-732
SCP-4450
https://scp-wiki.wdfiles.com/local--resized-images/task-forces/Omega7.jpg/small.jpg""")
    @commands.command(aliases=['achillesheels', 'omega-12'])
    async def omega12(self,ctx):
        await ctx.channel.send("""Task Force Mission: A task force composed of reality bending Foundation personnel from an alternate universe. Omega-12 (Achilles' Heels) is tasked with capturing SCP-3480-2 instances, guarding the many entities imprisoned in Area-13, and hunting down powerful uncontained reality benders elsewhere.
Assisting In Containment of Objects:
SCP-3155
SCP-3221
SCP-3480
SCP-3797-ARC
SCP-4455
SCP-4800
https://scp-wiki.wdfiles.com/local--resized-images/task-forces/Omega12.png/small.jpg""")
    @commands.command(aliases=['evolvedfromnaturallyoccuringgearsleversandpulleys', 'stigma-9'])
    async def stigma9(self,ctx):
        await ctx.channel.send("""Task Force Mission: —Historically, the Church of the Broken God had always prided itself on its artificiality - that its faith is proven with tangible artifacts and physical devices of miracles. So, when the time came to destabilize the Church, the Foundation put forth a team of forgers, and Stigma-9 (Evolved from Naturally Occurring Gears, Levers and Pulleys) was it.
Assisting In Containment of Objects:
SCP-2834
SCP-3221
SCP-3341
SCP-5862
https://scp-wiki.wdfiles.com/local--resized-images/task-forces/Stigma9.png/small.jpg""")
def setup(client):
    client.add_cog(mtfs(client))