import discord

from discord.ext import commands

class RulesCommands(commands.cog):
  
  def __init__(self, bot):
    self.bot = bot

  
  @bot.tree.command(
    name="omrules",
    description="OutMyth Discord Server Rules.",
)

  async def rules(interaction: str):
    """These can be found in the channel "rules" in OutMyth's Discord server."""
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
  
async setup(bot):
  await bot.add_cog(RulesCommands(bot))
