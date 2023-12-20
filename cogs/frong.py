import nextcord
from nextcord.ext import commands

class Sourcecode(commands.Cog):
    def __init__(self,bot):
      self.bot=bot

    @commands.Cog.listener()
    async def on_ready(self):
      print(f"frong - Loaded")

    @nextcord.slash_command(name="frongs")
    async def frongs(self, interaction: nextcord.Interaction):
      embed = nextcord.Embed(title="**Frongs**", color=0x4287f5)
      embed.add_field(name="**Definitions**", value="/frong \n /frang \n /frongincidence",inline=False)
      await interaction.response.send_message(embed=embed, ephemeral=False)

    @nextcord.slash_command(name="frong")
    async def frong(self, interaction: nextcord.Interaction):
      embed = nextcord.Embed(title="**Frong**", color=0x4287f5)
      embed.add_field(name="**Definition:**", value="Frong (for real, on god) is a expression used in the Cosmodium Cyber Security server for humorous means. It is most commonly utilised in a fashion of agreement about a given subject. Frong (for real, on god) is a derivative of “Fr” (for real) and “ong” (on god). It is not recognized as a legitimate word in the 2022 Oxford English Dictionary, but is utilized nonetheless as a cultural reference of mutual agreement. This expression was first coined by Soulsender and CØ$MØ where the two individuals were saying “Fr Fr ong” (for real, for real, on god) as a method of agreement, where after the two expressions were merged to form the new commonly used phrase. Since the debut, the phrase has found use in a server emoji of a small mammal dubbed a “gerbil” with the text “frong” (for real, on god) displayed on the bottom of the image in 2013 type-2 impact font.",inline=False)
      await interaction.response.send_message(embed=embed, ephemeral=False)
    
    @nextcord.slash_command(name="frongincidence")
    async def frongincidence(self, interaction: nextcord.Interaction):
      embed = nextcord.Embed(title="**Frongincidence**", color=0x4287f5)
      embed.add_field(name="**Definition:**", value="Frongincidence (for real, on god, coincidence) is most commonly utilized in a fashion of suspicious coincidence (dubbed \"sus\") about a given subject. Frongincidence (for real, on god, coincidence) is a derivative of “Fr” (for real) and “ong” (on god), as well as the word \"coincidence.\" It is not recognized as a legitimate word in the 2022 Oxford English Dictionary, but is utilized nonetheless as a cultural reference of suscoincidence. This expression was first coined by CØ$MØ where he was referencing an aspect of the media platform discord, and how it pertained to the word \"frong\" (for real, on god) as is the emoji letters were in a sequential fashion, where after the two expressions were merged to form the new commonly used phrase; Frongincidence (for real, on god, coincidence). Since it’s debut, the phrase has found use in a server emoji of a small mammal dubbed a “gerbil” with the text “frong” (for real, on god), with the additional context of something being of  suspicious coincidence (\"sus\").",inline=False)
      await interaction.response.send_message(embed=embed, ephemeral=False)

    @nextcord.slash_command(name="frang")
    async def frang(self, interaction: nextcord.Interaction):
      embed = nextcord.Embed(title="**Frang**", color=0x4287f5)
      embed.add_field(name="**Definition:**", value="Frang (for real, on god, language) otherwise known as \"Fronlang\" is a programming language used to develop programs like FrongOS (for real, on god, operating system) as well as Google and PowerFrong. It is Comterpreted language, meaning that the user must compile it and then run the compiled binary through an interpreter. The langauge is not object oriented, because fuck that. Frang is well recognized as a programming language in the computer science community, and has even received an oscar for how well developed it is. The original developers, CØ$MØ and Haze, chose the name \"Frang\" or \"Fronglang\" due to its associaton of the word \"frong\" (for real, on god).",inline=False)
      await interaction.response.send_message(embed=embed, ephemeral=False)

def setup(bot):
  bot.add_cog(Sourcecode(bot))