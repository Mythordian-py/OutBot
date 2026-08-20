import discord
import logging

from discord.ext import commands

class GeneralCommands(commands.Cog):
  
  def __init__(self, bot):
    self.bot = bot

  @discord.app_commands.command(
    name="hello",
    description="It pings you & says hello!",
  )
  
  async def hello(self, interaction):
      """
      This command greets the user.
      """
      await interaction.response.send_message(f"Hello, {interaction.user.mention}!")
  
  @discord.app_commands.command(
    name="dm",
    description="Dms the user. Please make sure you have Dms turned on.",
)

  async def dm(self, interaction, msg: str):
      """
      THe command Dms the user who triggered the command.
      """
      if len(msg) > 2000:
          await interaction.response.send_message(
              """Error 413! Your message was more than characters 2000. This means your message is too long to send. Please make your 
          message shorter""",
              ephemeral=True,
          )
          return
  
      try:
          await interaction.user.send(f"Dm: ||{msg}||")
          await interaction.response.send_message("Check your Dms!", ephemeral=True)
  
      except discord.Forbidden:
          await interaction.response.send_message(
              """Error 403! I could not send you a Dm. This is because you have them turned off. Please turn them on to allow me to send
          you a dm""",
              ephemeral=True,
          )
  
      except Exception:
          logging.exception("Unexpected error in /dm")
    
  @discord.app_commands.command(
      name="say",
      description="You tell the Bot what to say!",
  )

  async def say(self, interaction, say: str):
      """
      You tell the bot what to say.
      """
      if len(say) > 2000:
          await interaction.response.send_message(
              "Error 413! Your message was too long. Please make it shorter. To allow me to send you a DM.",
              ephemeral=True,
          )
          return
  
      try:
          await interaction.response.send_message(
              f"{interaction.user.mention} told me to say: ||{say}||"
          )
  
      except discord.HTTPException as e:
          await interaction.response.send_message(
              f"Error{e.status}! Discord API failure", ephemeral=True
          )
  
      except Exception:
          logging.exception("Unexpected error in /say")


@discord.app_commands.command(
    name="ping",
    description="Pings you",
)

async def ping(self, interaction):
    """
    This command pings the user when it is used.
    """
    await interaction.response.send_message(f"{interaction.user.mention}")


async def setup(bot):
  await bot.add_cog(GeneralCommands(bot))
