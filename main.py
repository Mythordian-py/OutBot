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


# |===============|
# | Intents & cogs|
# |===============|


intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix=None, intents=intents)

await bot.load_extension("cog.general")
await bot.load_extension("cog.rules")
await bot.load_extension("cog.links")
await bot.load_extension("cog.information")
await bot.load_extension("cog.fun")

# |========|
# | Events |
# |========|


@bot.event
async def on_ready():
    synced = await self.tree.sync()
    print()
    print("OutBot is ready to be used.")
    print()
    print(f"Synced {len(synced)} slash commands.")


bot.run(token, log_handler=handler, log_level=logging.DEBUG)
