# The first words in a comment, is the command name.
import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

"""
|=================================|
|Discord Token % Logging & Intents|
|=================================|
"""
# Loads .env and gets the discord token from .env form the variable DISCORD_TOKEN. This is to ensure the OutBot's token doesn't get leaked
load_dotenv()
token = os.getenv("DISCORD_TOKEN")

# Logging | Saves logs into a discord.log file so crashes and can be reviewed later
handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")

# Intents | We need member intents to add/remove onbaording roles. Prefixs are set to "None" because OuBot has no prefix commands.
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="!",intents=intents)


# |======|
# |Events|
# |======|


# This prints if the bot is ready for use and the amound of slash commands that can be used. If this doesn's print, there is a bug.
@bot.event
async def on_ready():
    synced = await bot.tree.sync()
    print()
    print("OutBot is ready!")
    print()
    print(f"Synced {len(synced)} slash commands!")


# |==============|
# |Slash Commands|
# |==============|

# ephemeral=False by defult. This means everyone can see the message displayed by the bot. When ephemeral=True, only the user who send the command can see
# the message displayed by the bot.
# All commands ping the user. This is to ensure the user knows waht command they used. Except emphemeral commands.
# Error Mesage can only be seen by the user who used the command ephemeral=True.

@bot.tree.command(name="hello", description="It pings you & says hello!")
async def hello(interaction):
    """
    /hello | This command can be used to check if the bot is online; if commands work; a "fun"-command.
    """
    await interaction.response.send_message(f"Hello, {interaction.user.mention}!")

@bot.tree.command(name="outmyth", description="Shows OutMyth's Discord & YouTube links and OutMyth's owners")
async def outmyth(interaction):
    """
    /outmyth | Useful information about OutMyth. For example, links to OutMyth's Discord server and YouTube channel. Explains what OUtMyth is.
    """
    await interaction.response.send_message(f"""OutMyth is a YouTube channel and discord server owned by Valorous; Outdaner; Mythrodian! 
    
OutMyth YouTube = https://www.youtube.com/channel/UCGjkPP8sjN8WanIY6hhAeKw
    
OutMyth Discord = https://discord.gg/Sc5vAvTJtc.
{interaction.user.mention}""")

@bot.tree.command(name="omrules", description="OutMyth Discord Server Rules.")
async def rules(interaction):
    """
    /omrules | OutMyth discord server rules. These can be found in the channel "rules" in OutMyth's Discord server.
    """
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

#- :zap: **DON’T** ping @everyone; @here; any other types of mass pinging or message spam.

## 6. :ticket: Tickets

- :tickets: Do **NOT** open tickets without a valid reason. 

## 7. :people_hugging:  Behaviour

- :handshake: Be kind, respectful, and helpful to everyone.
    {interaction.user.mention}""")

@bot.tree.command(name="dm", description="Dms the user. Please make sure you have Dms turned on.")
async def dm(interaction, msg: str):
    """
    /dm | Dms the user. ("Check you Dms!" Can only be seen by you becasue: ephemeral=True) You can Dm yourself anything you want. Error handling including.
    """
    if len(msg)> 2000:
        await interaction.response.send_message("""Error 413! Your message was more than characters 2000. This means your message is too long to send. Please make your 
        message shorter""", ephemeral=True)
        return
    try:
        await interaction.user.send(f"Dm: ||{msg}||")
        await interaction.response.send_message("Check your Dms!", ephemeral=True)
        return
    except discord.Forbidden:
        await interaction.response.send_message("""Error 403! I could not send you a Dm. This is because you have them turned off. Please turn them on to allow me to send
        you a dm""", ephemeral=True)
        return
    except Exception as e:
        print(e)
        return

@bot.tree.command(name="say", description="You tell the Bot what to say!")
async def say(interaction, say: str):
    """
    /say | You tell the bot what to say. This command includes error handling.
    """
    if len(say) > 2000:
        await interaction.response.send_message("Error 413! Your message was too long. Please make it shorter.", ephemeral=True)
        return
    try:
        await interaction.response.send_message(f"{interaction.user.mention} told me to say: ||{say}||")
        return
    except discord.HTTPException as e:
        await interaction.response.send_message(f"Error{e.status}! Discord API faliure", ephemeral=True)
        return
    except Exception as e:
        print(e)
        return

@bot.tree.command(name="poll", description="Create a new poll.")
async def poll(interaction,poll_title: str, question: str):
    """
    /poll | Creates a poll with a title, question and 20 readtions to alow the user to pick a reaction of their choice. (20 reactions is the max amount of reactions a 
    Discord message can have).The poll title and question are both strings.
    """
    embed = discord.Embed(title=poll_title, description=question)
    await interaction.response.send_message(embed=embed)
    poll_msg = await interaction.original_response()
    for emoji in ("👍", "👎","✅", "❌", "😭", "🥀", "💀", "☠️", "😂", "🤣", "🔥", "🤡", "😱", "🗣️", "🐐", "👑", "🥶", "🤏", "🗿"):
        await poll_msg.add_reaction(emoji)
    # A list or tuple can be used here. The difference is too small to notice.

@bot.tree.command(name="help", description="Command guide")
async def help(interaction):
    """
    /obhelp | Outbot commands list. This can only be seen by you because of ephemeral=True. Split into 3 parts of 5 commands to byspass discord's 2000 charecter limit. 
    This message can only be seen by you because of ephemeral=True.
    """
    part1 = ("""## OutBot Commands (1 - 5)

    - Command 1: /hello
    To use the /hello command, type /hello in commands/chatbot, or in the bot's Dms.
        Says Hello to the user and ping the user.
    - Command 2: /outmyth
        To use /outmyth, type /outmyth in the bot's Dms or in the channels commands/chatbot.
        /outmyth will tell you about OutMyth. It will send the links of OutMyth's YouTube channel and discord server.
    - Command 3: /dm
        To use /dm, type /dm in the channels commands/chatbot followed by what you want to be Dmed. 
        Example: /dm Hello. The bot will Dm me Hello) Please make sure your Dms are turned on. If they are not on, the command will not work.
    - Command 4: /say
        To use /say, type /say in the bot's Dms, in the channels commands or chatbot. /say say anything you want it to say.
    - Command 5: /poll
        To use /poll, type /poll in the Bot's Dms or in the channels commands/chatbot followed by what you want your poll to be about.
        For Example: /poll Do you like to sleep""")

    part2 = ("""## OutBot Commands (6 - 10)

    - Command 6: /outbot
        To use the command: /outbot, type /outbot in the Bot's Dms or in the channels commands/chatbot.
        The command outbot will show the bots developers, GitHub page, TOS etc.Please only use OutBot in the channel chatbot, commands or in the bots DMs.
    - Command 7: /youtube
        To use /youtube, type /youtube in the bot's Dms or in the channels commands/chatbot.
        /youtube will give you the link to OutMyth's YouTube channel.
    - Command 8: /serverlink
        To use /serverlink, type /serverlink in the bot's Dms or in the channels commands/chatbot.
        /serverlink will give you the invite link to OutMyth'sdiscord server.
    - Command 9: /omrules
        To use /omrules, type /omrules in the bot's Dms or in the channels command/chatbot.
        /omrules will display OutMyth'sdiscord server rules.
    - Command 10: /botrules
        To use /botrules, type /botrules in the bot's Dms or in the channels commands/chatbot.
        The command: /botrules will display the rules onhow to use OutBot""")

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
-Command 15 /roadmap
    To use /invite, type /invite in the bot's Dms or in the channels commands/chatbot.
    /roadmap will show you OutBot's planned features!
    {interaction.user.mention}""")

    await interaction.response.send_message(part1, ephemeral=True)
    await interaction.followup.send(part2, ephemeral=True)
    await interaction.followup.send(part3, ephemeral=True)

"""/outbot | Useful imformation about OutBot. This command exists for user transparency."""
@bot.tree.command(name="outbot", description="Imformation about OutBot!")
async def outbot(interaction):
    """
    /outbot | Useful imformation about OutBot. This command exists for user transparency.
    """
    await interaction.response.send_message(f"""## OutBot
## - Bot Version = 0.3
## - Developers = mythordian & aardappel1
## - Date Started = July 11th 2026
## - Last update = July 22nd July 2026
## - TOS = Coming Soon
## - Privacy Policy = Coming Soon
## - GitHub = <https://github.com/Mythordian-py/OutBot/>
## - {interaction.user.mention}""")

@bot.tree.command(name="botrules", description="OutBot's Rules!")
async def botrules(interaction):
    """
    /botrules | OutBot useage rules. Ensures the user knows how to use OutBot appropriately. ephemeral=Flase so other users can see OutBot's rules.
    """
    await interaction.response.send_message(f"""## Bot Rules
    - 1. Use the bot for its intended purpose.
    - 2. Only use OutBot in the channels command or chatbot.
    - 3. Do NOT try to exploit OutBot.
    - 4. Please try to find bugs and report them by opening a ticket.
    - 5. Do **NOT** make the bot dm you something offensive or make the bot say something offensive
## - {interaction.user.mention}""")

@bot.tree.command(name="youtube", description="OutMyth's YouTube channel link")
async def youtube(interaction):
    """
    /youtube | OutMyth YouTube channel link. ephemeral=Flase to other users can see OutMyth's channel link.
    """
    await interaction.response.send_message(f"""OutMyth's YouTube Channel:

<https://www.youtube.com/channel/UCGjkPP8sjN8WanIY6hhAeKw>
{interaction.user.mention}""")

@bot.tree.command(name="serverlink", description="OutMyth's Discord server invite link.")
async def serverlink(interaction):
    """
    /serverlink | OutMyth Discord server invite link. ephemeral=Flase so other users can use the discord invite link.
    """
    await interaction.response.send_message(f"""OutMyth's Discord Server:

https://discord.gg/Sc5vAvTJtc
{interaction.user.mention}""")

@bot.tree.command(name="ping", description="Pings you")
async def ping(interaction):
    """
    /ping | This command is a "fun"-command.
    """
    await interaction.response.send_message(f"{interaction.user.mention}")

@bot.tree.command(name="rickroll", description="Don't do it...")
async def rickroll(interaction):
    """
    /rickroll | Sends the youtube link to rickroll the user. Only the user can you it because of ephemeral=True.
    """
    await interaction.response.send_message("CLICK ME ---> ||<https://www.youtube.com/watch?v=dQw4w9WgXcQ&list=RDdQw4w9WgXcQ&start_radio=1>||"
    , ephemeral=True)

@bot.tree.command(name="invite", description="Invite link for OutBot")
async def invite(interaction):
    """
    /invite | Sends the invite link for the bot. This can be seen by anyone to ensure people can easily add OutBot to their own Discord  server's.
    """
    await interaction.response.send_message(f"""Outbot Invite Link:

    https://discord.com/oauth2/authorize?client_id=1525595736706781384
    
    {interaction.user.mention}""")

@bot.tree.command(name="roadmap", description="OutBot's Planned Features!")
async def roadmap(interaction):
    """
    /roadmap | Outbot's planned features. This command is for users to improve any planned features, or give the Devs new ideas for new features.
    """
    await interaction.response.send_message(f"""## OutBot's Planned features!
    - Assign/Remove onboarding roles
    - Error handling
    - TOS & Privacy Policy
    - Bot Settings Commands
    - Role Information
    - Improved Quality Of Existing Commands
    {interaction.user.mention}""")

bot.run(token, log_handler=handler, log_level=logging.DEBUG)
