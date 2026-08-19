import discord
import logging
import os


from discord.ext import commands
from dotenv import load_dotenv
from emojis import emojis


# |===============|
# | Discord cofig |
# |===============|


load_dotenv()
token = os.getenv("DISCORD_TOKEN")
if not token:
    raise RuntimeError("Discord token not found.")


handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="a")

# |=========|
# | Intents |
# |=========|


intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix=None, intents=intents)


# |========|
# | Events |
# |========|


@bot.event
async def on_ready():
    synced = await bot.tree.sync()
    print()
    print("OutBot is ready to be used.")
    print()
    print(f"Synced {len(synced)} slash commands.")


# |================|
# | Slash Commands |
# |================|


async def outmyth(interaction):
    """
    Useful information about OutMyth (Explains what OUtMyth is).
    """
    await interaction.response.send_message(
        f"""OutMyth is a YouTube channel and discord server owned by Valorous; Outdaner; Mythrodian!

OutMyth YouTube = <https://www.youtube.com/channel/UCGjkPP8sjN8WanIY6hhAeKw>
    
OutMyth Discord = https://discord.gg/Sc5vAvTJtc.
{interaction.user.mention}"""
    )


@bot.tree.command(
    name="omrules",
    description="OutMyth Discord Server Rules.",

)
async def rules(interaction: str):
    """
    OutMyth discord server rules. These can be found in the channel "rules" in OutMyth's Discord server.
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


@bot.tree.command(
    name="poll",
    description="Create a new poll.",

)
async def poll(interaction, title: str, question: str):
    """
    Creates a poll with a title, question, and reactions
    """
    
    embed = discord.Embed(title=title, description=question)
    await interaction.response.send_message(embed=embed)
    poll_msg = await interaction.original_response()
    for emoji in emojis:
        await poll_msg.add_reaction(emoji)


@bot.tree.command(
    name="help",
    description="Command guide",

)
async def help(interaction):
    """
    OutBot's command list and what they do/how to use them. It is Split into 3 parts of 5 commands to bypass discord's 2000 character 
    limit.
    """
    part1 = """## OutBot Commands (1 - 5)

    - Command 1: /hello
    To use the /hello command, type /hello in commands/chatbot, or in the bot's DMs.
        Says Hello to the user and ping the user.
    - Command 2: /outmyth
        To use /outmyth, type /outmyth in the bot's DMs or in the channels commands/chatbot.
        /outmyth will tell you about OutMyth. It will send the links of OutMyth's YouTube channel and discord server.
    - Command 3: /dm
        To use /dm, type /dm in the channels commands/chatbot followed by what you want to be Dmed. 
        Eg: /dm Hello. The bot will DM me Hello) Please make sure your DMs are turned on. If they are not on, the command will not work.
    - Command 4: /say
        To use /say, type /say in the bot's DMs, in the channels commands or chatbot. /say say anything you want it to say.
    - Command 5: /poll
        To use /poll, type /poll in the Bot's DMs or in the channels commands/chatbot followed by what you want your poll to be about.
        Eg: /poll Do you like to sleep"""

    
    part2 = """## OutBot Commands (6 - 10)

    - Command 6: /outbot
        To use the command: /outbot, type /outbot in the Bot's DMs or in the channels commands/chatbot.
        The command outbot will show the bots developers, GitHub page, TOS etc.Please only use OutBot in the channel chatbot, commands or in the bots DMs.
    - Command 7: /youtube
        To use /youtube, type /youtube in the bot's DMs or in the channels commands/chatbot.
        /youtube will give you the link to OutMyth's YouTube channel.
    - Command 8: /serverlink
        To use /serverlink, type /serverlink in the bot's DMs or in the channels commands/chatbot.
        /serverlink will give you the invite link to OutMyth's discord server.
    - Command 9: /omrules
        To use /omrules, type /omrules in the bot's DMs or in the channels command/chatbot.
        /omrules will display OutMyth's discord server rules.
    - Command 10: /botrules
        To use /botrules, type /botrules in the bot's DMs or in the channels commands/chatbot.
        The command: /botrules will display the rules on how to use OutBot"""

    
    part3 = f"""Outbot Commands (11 - 15)

- Command 11: /ping
    To use /ping, type /ping in the bot's DMs or in the channels commands/chatbot.
    The command: /ping will ping the user who called the command.
- Command 12: ||/rickroll||
    To use ||/rickroll||, type ||/rickroll|| in the bot's DMs or in the channels command/chatbot.
    The command will send you a special link...
- Command 13: /invite
    To use /invite, type /invite in the bot's DMs or in the channels commands/chatbot.
    The command will send you the invite link for OutBot
-Command 14: /roadmap
    To use /roadmap, type /roadmap in the bot's DMs or in the channels commands/chatbot.
    /roadmap will show you OutBot's planned features!
    {interaction.user.mention}"""

    await interaction.response.send_message(part1, ephemeral=True)
    await interaction.followup.send(part2, ephemeral=True)
    await interaction.followup.send(part3, ephemeral=True)


@bot.tree.command(
    name="outbot",
    description="Information about OutBot!",

)
async def outbot(interaction):
    """
    Useful information about OutBot.
    """
    await interaction.response.send_message(f"""## OutBot
## - Bot Version = 0.4
## - Developers = mythordian & aardappel1
## - Date Started = July 11th 2026
## - Last update = July 28nd 2026
## - TOS = Coming Soon
## - Privacy Policy = Coming Soon
## - GitHub = <https://github.com/Mythordian-py/OutBot/>
## - {interaction.user.mention}""")


    @bot.tree.command(
    name="botrules",
    description="OutBot's Rules!",

)
async def botrules(interaction):
    """
    OutBot usage rules. Ensures the user knows how to use OutBot appropriately.
    """
    await interaction.response.send_message(f"""## Bot Rules
    - 1. Use the bot for its intended purpose.
    - 2. Only use OutBot in the channels command or chatbot.
    - 3. Do NOT try to exploit OutBot.
    - 4. Please try to find bugs and report them by opening a ticket.
    - 5. Do **NOT** make the bot DM you something offensive or make the bot say something offensive
## - {interaction.user.mention}""")


@bot.tree.command(
    name="youtube",
    description="OutMyth's YouTube channel link",

)
async def youtube(interaction):
    """
    OutMyth YouTube channel link.
    """
    await interaction.response.send_message(f"""OutMyth's YouTube Channel:
    
<https://www.youtube.com/channel/UCGjkPP8sjN8WanIY6hhAeKw>
{interaction.user.mention}""")


@bot.tree.command(
    name="serverlink", description="OutMyth's Discord server invite link."

)
async def serverlink(interaction):
    """
    OutMyth Discord server invite link.
    """
    await interaction.response.send_message(f"""OutMyth's Discord Server:

https://discord.gg/Sc5vAvTJtc
{interaction.user.mention}""")


@bot.tree.command(
    name="rickroll",
    description="Don't do it...",

)
async def rickroll(interaction):
    """
    Sends a youtube link to rickroll the user.
    """
    await interaction.response.send_message(
        "CLICK ME ---> ||<https://www.youtube.com/watch?v=dQw4w9WgXcQ&list=RDdQw4w9WgXcQ&start_radio=1>||",
        ephemeral=True,
    )


@bot.tree.command(
    name="invite",
    description="Invite link for OutBot",

)
async def invite(interaction):
    """
    Sends the invite link for the bot.
    """
    await interaction.response.send_message(f"""Outbot Invite Link:

    <https://discord.com/oauth2/authorize?client_id=1525595736706781384>
    
    {interaction.user.mention}""")


@bot.tree.command(
    name="roadmap",
    description="OutBot's Planned Features!",

)
async def roadmap(interaction):
    """
    Outbot's planned features.
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
