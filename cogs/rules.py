import discord

from discord.ext import commands

class RulesCommands(commands.cog):
  
  def __init__(self, bot):
    self.bot = bot

  
  @discord.app_commands.command(
    name="omrules",
    description="OutMyth Discord Server Rules.",
)

  async def rules(self, interaction: discord.Interaction):
    """These can be found in the channel "rules", in OutMyth's Discord server."""
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
    name="botrules",
    description="OutBot's Rules!",
)
    
  async def botrules(self, interaction: discord.Interaction):
    await interaction.response.send_message(f"""## Bot Rules
    - 1. Use the bot for its intended purpose.
    - 2. Only use OutBot in the channels command or chatbot.
    - 3. Do NOT try to exploit OutBot.
    - 4. Please try to find bugs and report them by opening a ticket.
    - 5. Do **NOT** make the bot DM you something offensive or make the bot say something offensive
## - {interaction.user.mention}""")


async def setup(bot):
  await bot.add_cog(RulesCommands(bot))
