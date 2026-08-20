import discord

from discord.ext import commands

class RulesCommands(commands.cog):
  
  def __init__(self, bot):
    self.bot = bot



async setup(bot):
  await bot.add_cog(RulesCommands(bot))
