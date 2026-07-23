#The first words in a comment, is the command name.
import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os





#===========================================================================================================================================================================
#Discord Token % Logging & Intents
#===========================================================================================================================================================================





load_dotenv()
token = os.getenv("DISCORD_TOKEN")





#Logging & Intents
handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w") #<--- How logging works
intents = discord.Intents.default()
intents.members = True
intents = discord.Intents.default()
bot = commands.Bot(command_prefix=None,intents=intents)





#===========================================================================================================================================================================
#Events
#===========================================================================================================================================================================





@bot.event
async def on_ready():
    synced = await bot.tree.sync()
    print(f"Synced {len(synced)} slash commands")





#===========================================================================================================================================================================
#Slash Commands
#===========================================================================================================================================================================





#/hello
@bot.tree.command(name="hello", description="It pings you & says hello!")
async def hello(interaction):
    await interaction.response.send_message(f"Hello, {interaction.user.mention}!")





#/outmyth
@bot.tree.command(name="outmyth", description="Shows OutMyth's Dicord & YouTube links, and their members/subscribers.")
async def outmyth(interaction):
    await interaction.response.send_message(f"""OutMyth is a YouTube channel and discord server owned by Valorous; Outdaner; Mythrodian! 
    
OutMyth's Discord Server currently has 28 members.

OutMyth's YouTube channel currently has 12 subcribers. 
    
OutMyth YouTube = https://www.youtube.com/channel/UCGjkPP8sjN8WanIY6hhAeKw
    
OutMyth Discord = https://discord.gg/Sc5vAvTJtc.
{interaction.user.mention}""")





#/omhis
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





#/omrules
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





#/dm
@bot.tree.command(name="dm", description="Dms the user. Please make sure you have Dms turned on.")
async def dm(interaction, msg: str):
    await interaction.user.send(f"Dm: ||{msg}||")
    await interaction.response.send_message("Check your Dms!", ephemeral=True)





#/reply
@bot.tree.command(name="reply", description="The bot replies to your message.")
async def reply(interaction, reply: str):
    await interaction.response.send_message(f"Reply: ||{reply}||", ephemeral=True)





#/poll
@bot.tree.command(name="poll", description="Create a new poll.")
async def poll(interaction,poll_title: str, question: str):
    embed = discord.Embed(title=poll_title, description=question)
    await interaction.response.send_message(embed=embed)
    poll_msg = await interaction.original_response()
    #reactions
    for emoji in ("👍", "👎","✅", "❌", "😭", "🥀", "💀", "☠️", "😂", "🤣", "🔥", "🤡", "😱", "🗣️", "🐐", "👑", "🥶", "🤏", "🗿"):
        await poll_msg.add_reaction(emoji)





#/obhelp
@bot.tree.command(name="obhelp", description="Command guide")
async def obhelp(interaction):
    #part1 | Contains a guide for commands 1 - 5
    part1 = ("""## OutBot Commands (1 - 5)

    - Command 1: /hello
    To use the /hello command, type /hello in commands/chatbot, or in the bot's Dms.
    /hello will say Hello to the user and ping the user.
    - Command 2: /outmyth
    To use /outmyth, type /outmyth in the bot's Dms or in the channels commands/chatbot.
    /outmyth will tell you about OutMyth. It will send the links of OutMyth's youtube channel and discord server.
    - Command 3: /omhis
    To use /omhis, type /omhis in the bot's Dms or in the channels commands/chatbot.
    /omhis will tell you about the history of OutMyth
    - Command 4: /dm
    To use /dm, type /dm in the channels commands/chatbot followed by what you want to be Dmed. 
    Example: /dm Hello. The bot will Dm me Hello) Please make sure your Dms are turned on. If they are not on, the command will not work.
    - Command 5: /reply
    To use /reply, type /reply in the bot's Dms, in the channels commands or chatbot. /reply will reply to your message. 
    For now it just says "Hello, <pings you>! How are you?".""")
    




    #part2 | Contains a guide for commands 6 - 12 
    part2 = (f"""## OutBot Commands (6 - 12)
    
    - Command 6: /poll
    To use /poll, type /poll in the Bot's Dms or in the channels commands/chatbot followed by what you want your poll to be about.
    For Example = /poll Do you like to sleep?
    - Command 7: /outbot
    To use the command: /outbot, type /outbot in the Bot's Dms or in the channels commands/chatbot.
    The command outbot will show the bots developers, GitHub page, TOS etc.Please only use OutBot in the channel chatbot, commands or in the bots DMs.
    - Command 8: /youtube
    To use /youtube, type /youtube in the bot's Dms or in the channels commands/chatbot. /youtube will give you the link to OutMyth'syoutube channel.
    - Command 9: /serverlink
    To use /serverlink, type /serverlink in the bot's Dms or in the channels commands/chatbot. /serverlink will give you the invite link to OutMyth'sdiscord server.
    - Command 10: /omrules
    To use /omrules, type /omrules in the bot's Dms or in the channels command/chatbot. /omrules will display OutMyth'sdiscord server rules.
    - Command 11: /botrules
    To use /botrules, type /botrules in the bot's Dms or in the channels commands/chatbot. The command: /botrules will display the rules onhow to use OutBot
    - Command 12: /ping
    To use /ping, type /ping in the bot's Dms or in the channels commands/chatbot. The command: /ping will ping the user who called the command.
    {interaction.user.mention}""")

    await interaction.response.send_message(part1)
    await interaction.followup.send(part2)





#/outbot
@bot.tree.command(name="outbot", description="Imformation about OutBot!")
async def outbot(interaction):
    await interaction.response.send_message(f"""## OutBot
## - Bot Version = 0.3
## - Developers = mythordian & aardappel1
## - Date Started = July 11th 2026
## - Last update = July 22nd July 2026
## - TOS = Coming Soon
## - Privacy Policy = Coming Soon
## - GitHub = https://github.com/Mythordian-py/OutBot/blob/main/main.py
## - {interaction.user.mention}""")





#/botrules
@bot.tree.command(name="botrules", description="OutBot's Rules!")
async def botrules(interaction):
    await interaction.response.send_message(f"""## Bot Rules
    - 1. Use the bot for its intended purpose.
    - 2. Only use OutBot in the channels command or chatbot.
    - 3. Do NOT try to exploit OutBot.
    - 4. Please try to find bugs and report them by opening a ticket.
## - {interaction.user.mention}""")





#/youtube
@bot.tree.command(name="youtube", description="OutMyth's Youtube channel link")
async def youtube(interaction):
    await interaction.response.send_message(f"""OutMyth's Youtube Channel:

https://www.youtube.com/channel/UCGjkPP8sjN8WanIY6hhAeKw
{interaction.user.mention}""")





#/serverlink
@bot.tree.command(name="serverlink", description="OutMyth's Discord server invite link.")
async def serverlink(interaction):
    await interaction.response.send_message(f"""OutMyth's Discord Server:

https://discord.gg/Sc5vAvTJtc
{interaction.user.mention}""")





#/ping
@bot.tree.command(name="ping", description="Pings the user who used the command")
async def ping(interaction):
    await interaction.response.send_message(f"{interaction.user.mention}")

bot.run(token, log_handler=handler, log_level=logging.DEBUG)
