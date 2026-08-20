import discord

from discord.ext import commands

class InformationCommands(commands.Cog)

  def __init__(self, bot):
    self.bot = bot

  @discord.app_commands.command(
    name="help",
    description="Command guide",
)
  async def help(interaction: discord.Interaction):
    """It is Split into 3 parts of 5 commands to bypass discord's 2000 character limit."""
    part1 = """## OutBot Commands (1 - 5)

    - Command 1: /hello
    To use the /hello command, type /hello in commands/chatbot, or in the bot's DMs.
        Says Hello to the user and ping the user.
    - Command 2: /dm
        To use /dm, type /dm in the channels commands/chatbot followed by what you want to be Dmed. 
        Eg: /dm Hello. The bot will DM me Hello) Please make sure your DMs are turned on. If they are not on, the command will not work.
    - Command 3: /say
        To use /say, type /say in the bot's DMs, in the channels commands or chatbot. /say say anything you want it to say.
    - Command 4: /poll
        To use /poll, type /poll in the Bot's DMs or in the channels commands/chatbot followed by what you want your poll to be about.
        Eg: /poll Do you like to sleep?
    - Command 5: /outbot
        To use the command: /outbot, type /outbot in the Bot's DMs or in the channels commands/chatbot.
        The command outbot will show the bots developers, GitHub page, TOS etc.Please only use OutBot in the channel chatbot, commands or in the bots DMs."""
    
    part2 = """OutBot Commands (6 - 10)

    - Command 6: /youtube
        To use /youtube, type /youtube in the bot's DMs or in the channels commands/chatbot.
        /youtube will give you the link to OutMyth's YouTube channel.
    - Command 7: /serverlink
        To use /serverlink, type /serverlink in the bot's DMs or in the channels commands/chatbot.
        /serverlink will give you the invite link to OutMyth's discord server.
    - Command 8: /omrules
        To use /omrules, type /omrules in the bot's DMs or in the channels command/chatbot.
        /omrules will display OutMyth's discord server rules.
    - Command 9: /botrules
        To use /botrules, type /botrules in the bot's DMs or in the channels commands/chatbot.
        The command: /botrules will display the rules on how to use OutBot
    - Command 10: /ping
    To use /ping, type /ping in the bot's DMs or in the channels commands/chatbot.
    The command: /ping will ping the user who called the command."""

    
    part3 = f"""Outbot Commands (11 - 13)

- Command 11: ||/rickroll||
    To use ||/rickroll||, type ||/rickroll|| in the bot's DMs or in the channels command/chatbot.
    The command will send you a special link...
- Command 12: /invite
    To use /invite, type /invite in the bot's DMs or in the channels commands/chatbot.
    The command will send you the invite link for OutBot
-Command 13: /roadmap
    To use /roadmap, type /roadmap in the bot's DMs or in the channels commands/chatbot.
    /roadmap will show you OutBot's planned features!
    {interaction.user.mention}"""

    await interaction.response.send_message(part1, ephemeral=True)
    await interaction.followup.send(part2, ephemeral=True)
    await interaction.followup.send(part3, ephemeral=True)


  @discord.app_commands.command(
    name="outbot",
    description="Information about OutBot!",
)

  async def outbot(interaction: discord.Interaction):
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
    name="roadmap",
    description="OutBot's Planned Features!",
)
  
  async def roadmap(interaction: discord.Interaction):
    await interaction.response.send_message(f"""## OutBot's Planned features!
    - Assign/Remove onboarding roles
    - Error handling
    - TOS & Privacy Policy
    - Bot Settings Commands
    - Role Information
    - Improved Quality Of Existing Commands
    {interaction.user.mention}""")


async def setup(bot):
  await bot.add_cog(InformationCommands(bot))
