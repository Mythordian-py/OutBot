import discord

from discord.ext import commands

class LinksCommands(commands.Cog):
  def __init__(self,bot):
    self.bot = bot


  @discord.app_commands.command(
    name="youtube",
    description="OutMyth's YouTube channel link",
)

  async def youtube(self, interaction: discord.Interaction):
    await interaction.response.send_message(f"""OutMyth's YouTube Channel:
    
<https://www.youtube.com/channel/UCGjkPP8sjN8WanIY6hhAeKw>
{interaction.user.mention}""")


  @discord.app_commands.command(
    name="serverlink", description="OutMyth's Discord server invite link."
)

  async def serverlink(interaction):
    await interaction.response.send_message(f"""OutMyth's Discord Server:

https://discord.gg/Sc5vAvTJtc
{interaction.user.mention}""")


  @bot.tree.command(
    name="invite",
    description="Invite link for OutBot",
)
  async def invite(interaction):
    await interaction.response.send_message(f"""Outbot Invite Link:
    
    <https://discord.com/oauth2/authorize?client_id=1525595736706781384>
    
    {interaction.user.mention}""")


async def setup(bot):
  await bot.add_cog(Links(bot))
