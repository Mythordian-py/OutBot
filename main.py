#The first words in a comment, is the command name. 
#imports
import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

#Loads .env and the bot token.
load_dotenv()
token = os.getenv("DISCORD_TOKEN")

handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="a") #<--- How logging works
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

#Command prefix
bot = commands.Bot(command_prefix=("!", "?", "-", "=", ";"), intents=intents)

#Shows up in terminal when the bot is ready to be used.
@bot.event
async def on_ready():
    print("|--------------------------|") #<--- Decorative text
    print("|-The bot can now be used.-|") #<--- The line that tells u s if the bot is ready for use.
    print("|--------------------------|") #<--- Decorative text

#Dms the user a join message.
@bot.event
async def on_member_join(member):
    await member.send(f"Welcome to Outmyth {member.name}!")

#checks who sent the message || Avoids the bot responding to itself.
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

#!hello || Hello command. I will add a how are you command too.
@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello, {ctx.author.mention}!")

#!outmyth || Outmyth command.
@bot.command()
async def outmyth(ctx):
    await ctx.send(f"""Outmyth is a youtube channel and discord server owned by Valorous; Outdaner; Mythrodian! 
    
OutMyth's Discord Server currently has 28 members.

OutMyth's YouTube channel currently has 12 subcribers. 
    
OutMyth YouTube = https://www.youtube.com/channel/UCGjkPP8sjN8WanIY6hhAeKw
    
OutMyth Discord = https://discord.gg/Sc5vAvTJtc.
{ctx.author.mention}""")


#!outmythhis|| This is the code for outmyth's history code.
@bot.command()
async def outmythhis(ctx):
    await ctx.send(f"""
    -2025

    OutMyth, originally known as SVO(Syglassss(Mythordian), Valorous, Outdaner), was created on the 18th of July 2025. OutMyth's discord server
    came out on the 1st of August 2025. Outmyth's discord server was first owned by Mythordian(Syglassss). Mythordian transferred ownership to Outdaner, after their 
    account got falsely banned. On December 13th 2025 the new OutMyth server was created.The old server had around 50 members. The new server currently has 28. 
    
-2026

    In early January, Valorous decided to leave OutMyth. This was the main reason there was a name change. Valorous decided to join back after around
    2 months later. OutBot(Outmyth Ai) was created on 11th of July 2026. Outmyth Ai was renamed to Outbot on the 19th of July 2026. Outmyth Ai did briefly exist 
    (under another name askie) for around a couple of days. Unfortunately, Outmyth Ai's(Askie's) Api key was lost.{ctx.author.mention}""")


#!server_Rules || Server Rules command.
@bot.command()
async def server_rules(ctx):
    await ctx.send(f"""## :scroll: Rules

## 1. :x: No NSFW And NO Malicious Content.

- :underage: Absolutely no NSFW content, pornography, sexual content, and malicious links.

## 2. :x: No Swearing / Offensive Language

- :speaking_head: Use common sense when chatting.

- :no_entry_sign: Check out Censored Words.

## 3. :white_check_mark: Respect Privacy

- :lock: Do NOT dox or share anyone’s personal information.

- :mailbox_with_mail: Do NOT DM staff or owners unnecessarily.

## 4. :x: No Self Promotion

- :loudspeaker: NO advertising in DMs or channels.

- :no_entry_sign: This applies to everyone, including staff and owners.

## 5. :white_check_mark: Use Mentions Responsibly

- :zap: DON’T ping @everyone ; @here; any other types of mass pinging or message spam.

## 6. :ticket: Tickets

- :tickets: Do NOT open tickets without a valid reason. 

## 7. :people_hugging:  Behaviour

- :handshake: Be kind, respectful, and helpful to everyone.

- :dart: Avoid using censored words and disruptive behaviour. (This includes malicious; manipulative; rage-baiting people etc.).
    {ctx.author.mention})""")

#!dm command code || To use !dm, type !dm followed by what you want to be dmed. Make sure you HAVE Dms ON! Or else the bot can't dm you
@bot.command()
async def dm(ctx, *, msg):
    await ctx.author.send(f"""Dm

{msg}""")

#The bot will reply to its dms.
@bot.command()
async def reply(ctx):
    await ctx.reply("This is a reply to your message")

#!poll || Poll command.
@bot.command()
async def poll(ctx, *, question):
    embed = discord.Embed(title = "New Poll", description = question)
    poll_message = await ctx.send(embed = embed)
    await poll_message.add_reaction("👍") #<--- Reacts with a thumbs up.
    await poll_message.add_reaction("👎") #<--- Reacts  with thumbs down.
    await poll_message.add_reaction("✅") #<--- Reacts with a tick.
    await poll_message.add_reaction("❌") #<--- Reacts  with a cross.

#!help || Help command.
#There are two parts because it prevents the bot form hitting the 2000 character limit.
@bot.command()
async def obhelp(ctx):
    part1 = ("""## OutBot Commands (1 - 5)
    ## You aren't just limited to using ! as a command prefix. You can also use ?, -, = and ; All commands work with these prefixes. 
    ## Feel free to use which ever one you're most comfortable with.

    - Command 1: !hello
    To use the !hello command, type !hello in commands/chatbot, or in the bot's Dms.
    !hello will say Hello to the user and ping the user.
    - Command 2: !outmyth
    To use !outmyth, type !outmyth in the bot's Dms or in the channels commands/chatbot.
    !outmyth will tell you about OutMyth. It will send the links of OutMyth's youtube channel and discord server.
    - Command 3: !outmythhis
    To use !outmythhis, type !outmythhis in the bot's Dms or in the channels commands/chatbot.
    !outmyth_history will tell you about the history of OutMyth
    - Command 4: !dm
    To use !dm, type !dm in the channels commands/chatbot followed by what you want to be Dmed. 
    Example: !dm Hello. The bot will Dm me Hello) Please make sure your Dms are turned on. If they are not on, the command will not work.
    - Command 5: !reply
    To use !reply, type !reply in the bot's Dms, in the channels commands or chatbot. /reply will reply to your message. 
    For now it just says "This is a reply to your message".""")

    part2 = (f"""## OutBot Commands (6 - 11)
    
    - Command 6: !poll
    To use !poll, type !poll in the Bot's Dms or in the channels commands/chatbot followed by what you want your poll to be about.
    For Example = !poll Do you like to sleep?
    - Command 7: !outbot
    To use the command: !outbot, type !outbot in the Bot's Dms or in the channels commands/chatbot.
    The command outbot will show the bots developers, GitHub page, TOS etc.Please only use OutBot in the channel chatbot, commands or in the bots DMs.
    - Command 8: !youtube
    To use !youtube, type !youtube in the bot's Dms or in the channels commands/chatbot. !youtube will give you the link to OutMyth'syoutube channel.
    - Command 9: !discord
    To use !discord, type !discord in the bot's Dms or in the channels commands/chatbot. !discord will give you the invite link to OutMyth'sdiscord server.
    - Command 10: !server_rules
    To use ! server rules, type !server_rules in the bot's Dms or in the channels command/chatbot. !server_rules will display OutMyth'sdiscord server rules.
    - Command 11: !botrules
    To use !botrules, type !botrules in the bot's Dms or in the channels commands/chatbot. The command !botrules will display the rules onhow to use OutBot
    {ctx.author.mention}""")

    await ctx.send(part1)
    await ctx.send(part2)

#!OutBot|| Bot Information command.
@bot.command()
async def outbot(ctx):
    await ctx.send(f"""## OutBot
## - Bot Version = 0.2
## - Total lines of code = 226
## - Developers = mythordian & aardappel1
## - Date Started = July 11th 2026
## - Last update = July 19th 2026
## - TOS = Coming Soon
## - Privacy Policy = Coming Soon
## - GitHub = https://github.com/Mythordian-py/OutBot/blob/main/main.py
## - {ctx.author.mention}""")


#!bot rules || Bot rules command.
@bot.command()
async def botrules(ctx):
    await ctx.send(f"""## Bot Rules
    - 1. Use the bot for its intended purpose.
    - 2. Only use OutBot in the channels command or chatbot.
    - 3. Do NOT try to exploit OutBot.
    - 4. Please try to find bugs and report them by opening a ticket.
## - {ctx.author.mention}""")

#!youtube|| Youtube command.
@bot.command()
async def youtube(ctx):
    await ctx.send(f"""OutMyth's Youtube Channel:

https://www.youtube.com/channel/UCGjkPP8sjN8WanIY6hhAeKw
{ctx.author.mention}""")

#!Discord || Discord server command.
@bot.command()
async def discord(ctx):
    await ctx.send(f"""OutMyth's Discord Server:

https://discord.gg/Sc5vAvTJtc
{ctx.author.mention}""")

bot.run(token, log_handler=handler, log_level=logging.DEBUG)
