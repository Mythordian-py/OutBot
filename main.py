#The first words in a comment, is the command name.
import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os





#===========================================================================================================================================================================
#Discord Token % Logging & Intents
#===========================================================================================================================================================================





#Loads .env and gets the discord token from .env form the variable DISCORD_TOKEN
load_dotenv()
token = os.getenv("DISCORD_TOKEN")





#Logging
handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")





#Intents
intents = discord.Intents.default()
bot = commands.Bot(command_prefix=None,intents=intents)





#===========================================================================================================================================================================
#Events
#===========================================================================================================================================================================





#Tells us when the Bot is ready for use
@bot.event
async def on_ready():
    synced = await bot.tree.sync()
    print()
    print("OutBot is ready!")
    print("================")
    print(f"Synced {len(synced)} slash commands!")





#===========================================================================================================================================================================
#Slash Commands
#===========================================================================================================================================================================





#/hello | Says Hello to the user & pings them.
@bot.tree.command(name="hello", description="It pings you & says hello!")
async def hello(interaction):
    await interaction.response.send_message(f"Hello, {interaction.user.mention}!")





#/outmyth | Useful information about OutMyth.
@bot.tree.command(name="outmyth", description="Shows OutMyth's Dicord & YouTube links, and their members/subscribers.")
async def outmyth(interaction):
    await interaction.response.send_message(f"""OutMyth is a YouTube channel and discord server owned by Valorous; Outdaner; Mythrodian! 
    
OutMyth YouTube = https://www.youtube.com/channel/UCGjkPP8sjN8WanIY6hhAeKw
    
OutMyth Discord = https://discord.gg/Sc5vAvTJtc.
{interaction.user.mention}""")





#/omhis | Important events that happened in OutMyth's history.
@bot.tree.command(name="omhis", description="OutMyth's History.")
async def omhis(interaction):
    await interaction.response.send_message(f"""
    -2025

    OutMyth, originally known as SVO,(Syglassss(Mythordian), Valorous, Outdaner), was created on the 18th of July 2025. OutMyth's discord server
    came out on the 1st of August 2025. Outmyth's discord server was first owned by Mythordian(Syglassss). Mythordian transferred ownership to Outdaner, after their 
    account got falsely banned. On December 13th 2025 the new OutMyth server was created.The old server had around 50 members
    
-2026

    In early January, Valorous decided to leave OutMyth. This was the main reason there was a name change. Valorous decided to join back after around
    2 months later. OutBot(Outmyth Ai) was created on 11th of July 2026. Outmyth Ai was renamed to Outbot on the 19th of July 2026. Outmyth Ai did briefly exist 
    under another alias, askie for around a couple of days. Unfortunately, Outmyth Ai's(Askie's) Api key was lost.{interaction.user.mention}""")





#/omrules | OutMyth discord server rules.
@bot.tree.command(name="omrules", description="OutMyth Discord Server Rules.")
async def omrules(interaction):
    await interaction.response.send_message(f"""## :scroll: **Rules**

## 1. :x:** NO** NSFW And **NO** Malicious Content.

- :underage: Absolutely **NO** NSFW content, pornography, sexual content, or malicious links.

## 2. :x: **NO** Swearing / Offensive Language

- :speaking_head: Use common sense when chatting.

- :no_entry_sign: Check out Censored Words.

## 3. :white_check_mark: Respect Privacy

- :lock: Do **NOT** dox or share anyone’s personal information.

- :mailbox_with_mail: Do **NOT** Dm anyone without a valid reason.

## 4. :x: No Self Promotion

- :loudspeaker: **NO** advertising in Dms or channels.

- :no_entry_sign: This applies to **EVERYONE**, including staff and owners.

## 5. :white_check_mark: Use Mentions Responsibly

- :zap: **DON’T** ping @everyone; @here; any other types of mass pinging or message spam.

## 6. :ticket: Tickets

- :tickets: Do **NOT** open tickets without a valid reason. 

## 7. :people_hugging:  Behaviour

- :handshake: Be kind, respectful, and helpful to everyone.
    {interaction.user.mention}""")





#/dm | Dms the suer. ("Check you Dms!" Can only be seen by you becasue: ephemeral=True)
@bot.tree.command(name="dm", description="Dms the user. Please make sure you have Dms turned on.")
async def dm(interaction, msg: str):
    await interaction.user.send(f"Dm: ||{msg}||")
    await interaction.response.send_message("Check your Dms!", ephemeral=True)





#/say | You tell the bot what to say!
@bot.tree.command(name="say", description="You tell the Bot what to say!")
async def say(interaction, say: str):
    await interaction.response.send_message(f"You told me to say: ||{say}||")





#/poll | Creates a poll with a title, description and 20 readtions. (20 reactions is the max amount of reactions a Discord message can have)
@bot.tree.command(name="poll", description="Create a new poll.")
async def poll(interaction,poll_title: str, question: str):
    embed = discord.Embed(title=poll_title, description=question)
    await interaction.response.send_message(embed=embed)
    poll_msg = await interaction.original_response()
    #reactions
    for emoji in ("👍", "👎","✅", "❌", "😭", "🥀", "💀", "☠️", "😂", "🤣", "🔥", "🤡", "😱", "🗣️", "🐐", "👑", "🥶", "🤏", "🗿"):
        await poll_msg.add_reaction(emoji)
    #Tuple used because they are faster than lists; are ordered & unchangable.





#/obhelp | Outbot commands list. | Thic can only be seen by you because of ephemeral=True.
@bot.tree.command(name="help", description="Command guide")
async def help(interaction):
    #part1 | Contains a guide for commands 1 - 5.
    part1 = ("""## OutBot Commands (1 - 5)

    - Command 1: /hello
    To use the /hello command, type /hello in commands/chatbot, or in the bot's Dms.
        Says Hello to the user and ping the user.
    - Command 2: /outmyth
        To use /outmyth, type /outmyth in the bot's Dms or in the channels commands/chatbot.
        /outmyth will tell you about OutMyth. It will send the links of OutMyth's YouTube channel and discord server.
    - Command 3: /omhis
        To use /omhis, type /omhis in the bot's Dms or in the channels commands/chatbot.
        /omhis will tell you about the history of OutMyth
    - Command 4: /dm
        To use /dm, type /dm in the channels commands/chatbot followed by what you want to be Dmed. 
        Example: /dm Hello. The bot will Dm me Hello) Please make sure your Dms are turned on. If they are not on, the command will not work.
    - Command 5: /say
        To use /say, type /say in the bot's Dms, in the channels commands or chatbot. /say say anything you want it to say.""")
    




    #part2 | Contains a guide for commands 
    part2 = ("""## OutBot Commands (6 - 10)
    
    - Command 6: /poll
        To use /poll, type /poll in the Bot's Dms or in the channels commands/chatbot followed by what you want your poll to be about.
        For Example: /poll Do you like to sleep?
    - Command 7: /outbot
        To use the command: /outbot, type /outbot in the Bot's Dms or in the channels commands/chatbot.
        The command outbot will show the bots developers, GitHub page, TOS etc.Please only use OutBot in the channel chatbot, commands or in the bots DMs.
    - Command 8: /youtube
        To use /youtube, type /youtube in the bot's Dms or in the channels commands/chatbot.
        /youtube will give you the link to OutMyth's YouTube channel.
    - Command 9: /serverlink
        To use /serverlink, type /serverlink in the bot's Dms or in the channels commands/chatbot.
        /serverlink will give you the invite link to OutMyth'sdiscord server.
    - Command 10: /omrules
        To use /omrules, type /omrules in the bot's Dms or in the channels command/chatbot.
        /omrules will display OutMyth'sdiscord server rules.""")




    part3 = (f"""Outbot Commands (11 - 15)
    - Command 11: /botrules
    To use /botrules, type /botrules in the bot's Dms or in the channels commands/chatbot.
    The command: /botrules will display the rules onhow to use OutBot
- Command 12: /ping
    To use /ping, type /ping in the bot's Dms or in the channels commands/chatbot.
    The command: /ping will ping the user who called the command.
- Command 13: ||/rickroll||
    To use ||/rickroll||, type ||/rickroll|| in the bot's Dms or in the channels command/chatbot.
    The command will send you a special link...
- Command 14: /invite
    To use /invite, type /invite in the bot's Dms or in the channels commands/chatbot.
    The command will send you the invite link for OutBot
    {interaction.user.mention}""")

    await interaction.response.send_message(part1, ephemeral=True)
    await interaction.followup.send(part2, ephemeral=True)
    await interaction.followup.send(part3, ephemeral=True)





#/outbot | Useful imformation about OutBot
@bot.tree.command(name="outbot", description="Imformation about OutBot!")
async def outbot(interaction):
    await interaction.response.send_message(f"""## OutBot
## - Bot Version = 0.3
## - Developers = mythordian & aardappel1
## - Date Started = July 11th 2026
## - Last update = July 22nd July 2026
## - TOS = Coming Soon
## - Privacy Policy = Coming Soon
## - GitHub = <https://github.com/Mythordian-py/OutBot/>
## - {interaction.user.mention}""")





#/botrules | OutBot useage rules.
@bot.tree.command(name="botrules", description="OutBot's Rules!")
async def botrules(interaction):
    await interaction.response.send_message(f"""## Bot Rules
    - 1. Use the bot for its intended purpose.
    - 2. Only use OutBot in the channels command or chatbot.
    - 3. Do NOT try to exploit OutBot.
    - 4. Please try to find bugs and report them by opening a ticket.
    - 5. Do **NOT** make the bot dm you something offensive or make the bot say something offensive
## - {interaction.user.mention}""")





#/youtube | OutMyth YouTube channel link.
@bot.tree.command(name="youtube", description="OutMyth's YouTube channel link")
async def youtube(interaction):
    await interaction.response.send_message(f"""OutMyth's YouTube Channel:

<https://www.youtube.com/channel/UCGjkPP8sjN8WanIY6hhAeKw>
{interaction.user.mention}""")





#/serverlink | OutMyth Discord server invite link.
@bot.tree.command(name="serverlink", description="OutMyth's Discord server invite link.")
async def serverlink(interaction):
    await interaction.response.send_message(f"""OutMyth's Discord Server:

https://discord.gg/Sc5vAvTJtc
{interaction.user.mention}""")





#/ping | Pings the user.
@bot.tree.command(name="ping", description="Pings you")
async def ping(interaction):
    await interaction.response.send_message(f"{interaction.user.mention}")





#r/ickroll | Sends the youtube link to rickroll the user. Only the user can you it because of ephemeral=True
@bot.tree.command(name="rickroll", description="Don't do it...")
async def rickroll(interaction):
    await interaction.response.send_message(f"{interaction.user.mention} | CLICK MEEEEEE ---> ||<https://www.youtube.com/watch?v=dQw4w9WgXcQ&list=RDdQw4w9WgXcQ&start_radio=1>||", ephemeral=True)





#/invite | Sends the invite link for the bot.
@bot.tree.command(name="invite", description="Invite link for OutBot")
async def invite(interaction):
    await interaction.response.send_message(f"""Outbot Invite Link:
    https://discord.com/oauth2/authorize?client_id=1525595736706781384{interaction.user.mention}""")

bot.run(token, log_handler=handler, log_level=logging.DEBUG)
