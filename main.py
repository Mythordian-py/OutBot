import discord
import logging
import os


from cogs import fun, general, information, links, rules
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


async bot.load_extention(cog.general)
async bot.load_extention(cog.rules)
async bot.load_extention(cog.links)
async bot.load_extention(cog.information)
async bot.load_extention(cog.fun)


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
    synced = await dicord.app_commands.sync()
    print()
    print("OutBot is ready to be used.")
    print()
    print(f"Synced {len(synced)} slash commands.")


bot.run(token, log_handler=handler, log_level=logging.DEBUG)
