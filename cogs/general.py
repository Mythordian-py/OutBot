import discord
import logging

from discord.ext import commands
from emojis import emojis

class GeneralCommands(commands.Cog):
  
  def __init__(self, bot):
    self.bot = bot

  @discord.app_commands.command(
    name="hello",
    description="It pings you & says hello!",
  )
  
  async def hello(self, interaction: discord.Interaction):
      await interaction.response.send_message(f"Hello, {interaction.user.mention}!")
  
  @discord.app_commands.command(
    name="dm",
    description="Dms the user. Please make sure you have Dms turned on.",
)

  async def dm(self, interaction: discord.Interaction, msg: str):
      if len(msg) > 1999:
          await interaction.response.send_message(
              """Your message was more than characters 2000. This means your message is too long to send. Please make your message 
              shorter""",
              ephemeral=True,
          )
          return
  
      try:
          await interaction.user.send(f"Dm: ||{msg}||")
          await interaction.response.send_message("Check your Dms!", ephemeral=True)
  
      except discord.Forbidden:
          await interaction.response.send_message(
              """I could not send you a Dm. This is because you have them turned off. Please turn them on to allow me to send you a dm""",
              ephemeral=True,
          )
  
      except Exception:
          logging.exception("Unexpected error in /dm")
    
  @discord.app_commands.command(
      name="say",
      description="You tell the Bot what to say!",
  )

  async def say(self, interaction: discord.Interaction, say: str):
      if len(say) > 1999:
          await interaction.response.send_message(
              "Your message was too long. Please make it shorter. To allow me to send you a DM.",
              ephemeral=True,
          )
          return
  
      try:
          await interaction.response.send_message(
              f"{interaction.user.mention} told me to say: ||{say}||"
          )
  
      except discord.HTTPException as e:
          await interaction.response.send_message(
               "Discord API failure", ephemeral=True
          )
  
      except Exception:
          logging.exception("Unexpected error in /say")


@discord.app_commands.command(
    name="ping",
    description="Pings you",
)

async def ping(self, interaction: discord.Interaction):
    await interaction.response.send_message(f"{interaction.user.mention}")

@dsicord.app_commands.command(
    name="poll",
    description="Create a new poll.",
)
  async def poll(interaction, title: str, question: str):
    """20 reactions to allow the user to pick a reaction of their choice. 20 reactions is the max amount of reactions aDiscord message
    can have.The poll title and question are both strings."""
    embed = discord.Embed(title=title, description=question)
    await interaction.response.send_message(embed=embed)
    poll_msg = await interaction.original_response()
    for emoji in emojis:
        await poll_msg.add_reaction(emoji)


async def setup(bot):
  await bot.add_cog(GeneralCommands(bot))
