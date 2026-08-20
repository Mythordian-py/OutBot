import discord

from discord.ext import commands

class FunCommands(commands.Cog):
  
    def __init__(self, bot):
        self.bot = bot

    @discord.tree.command(
        name="rickroll",
        description="Don't do it...",
)
  
    async def rickroll(self, interaction: discord.Interaction):
    """Sends a youtube link to rickroll the user."""
        await interaction.response.send_message(
        "CLICK ME ---> ||<https://www.youtube.com/watch?v=dQw4w9WgXcQ&list=RDdQw4w9WgXcQ&start_radio=1>||",
        ephemeral=True)
    
async def setup(bot):
    await bot.add_cog(FunCommands(bot))
