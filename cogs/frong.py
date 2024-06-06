import nextcord
from nextcord.ext import commands

class Frongcmd(commands.Cog):
    def __init__(self,bot):
      self.bot=bot

    @commands.Cog.listener()
    async def on_ready(self):
      print(f"frong - Loaded")

    @nextcord.slash_command(name="frongs", description="List all Frong definitions")
    async def frongs(self, interaction: nextcord.Interaction):
      embed = nextcord.Embed(title=":rat: **Frongs**", color=0x4287f5)
      embed.add_field(name="**Definitions**", value="/frong \n /frang \n /frongincidence \n /frongonianunits \n /unfuckwithable",inline=False)
      await interaction.response.send_message(embed=embed, ephemeral=False)
      
    @nextcord.slash_command(name="frong", description="Original Frong definition")
    async def frong(self, interaction: nextcord.Interaction):
      embed = nextcord.Embed(title=":rat: **Frong**", color=0x4287f5)
      embed.add_field(name="**Definition:**", value="Frong (for real, on God) is an expression used in the Cosmodium Cyber Security server for humorous means. It is most commonly utilised in a fashion of agreement about a given subject. Frong (for real, on God) is a derivative of “Fr” (for real) and “ong” (on God). It is not recognized as a legitimate word in the 2022 Oxford English Dictionary but is utilized nonetheless as a cultural reference of mutual agreement. This expression was first coined by Soulsender and CØ$MØ where the two individuals were saying “Fr Fr ong” (for real, for real, on God) as a method of agreement, where after the two expressions were merged to form the new commonly used phrase. Since the debut, the phrase has found use in a server emoji of a small mammal dubbed a “gerbil” with the text “frong” (for real, on God) displayed on the bottom of the image in 2013 type-2 impact font.",inline=False)
      await interaction.response.send_message(embed=embed, ephemeral=False)

    @nextcord.slash_command(name="frongincidence", description="A suspicious conincidence")
    async def frongincidence(self, interaction: nextcord.Interaction):
      embed = nextcord.Embed(title=":rat: **Frongincidence**", color=0x4287f5)
      embed.add_field(name="**Definition:**", value="Frongincidence (for real, on God, coincidence) is most commonly utilized in a fashion of suspicious coincidence (dubbed \"sus\") about a given subject. Frongincidence (for real, on God, coincidence) is a derivative of “Fr” (for real) and “ong” (on God), as well as the word \"coincidence.\" It is not recognized as a legitimate word in the 2022 Oxford English Dictionary but is utilized nonetheless as a cultural reference of suscoincidence. This expression was first coined by CØ$MØ where he was referencing an aspect of the media platform discord, and how it pertained to the word \"frong\" (for real, on God) as is the emoji letters were in a sequential fashion, where after the two expressions were merged to form the new commonly used phrase; Frongincidence (for real, on God, coincidence). Since its debut, the phrase has found use in a server emoji of a small mammal dubbed a “gerbil” with the text “frong” (for real, on God), with the additional context of something being of suspicious coincidence (\"sus\").",inline=False)
      await interaction.response.send_message(embed=embed, ephemeral=False)

    @nextcord.slash_command(name="frang", description="FrongLang")
    async def frang(self, interaction: nextcord.Interaction):
      embed = nextcord.Embed(title=":rat: **Frang**", color=0x4287f5)
      embed.add_field(name="**Definition:**", value="Frang (for real, on God, language) otherwise known as \"Fronlang\" is a programming language used to develop programs like FrongOS (for real, on God, operating system) as well as Google and PowerFrong. It is Comterpreted language, meaning that the user must compile it and then run the compiled binary through an interpreter. The langauge is not object oriented, because fuck that. Frang is well recognized as a programming language in the computer science community and has even received an oscar for how well developed it is. The original developers, CØ$MØ and Haze, chose the name \"Frang\" or \"Fronglang\" due to its associaton of the word \"frong\" (for real, on God).",inline=False)
      await interaction.response.send_message(embed=embed, ephemeral=False)

    @nextcord.slash_command(name="frongonianunits", description="The best unit of measurement")
    async def frongonianunits(self, interaction: nextcord.Interaction):
      embed = nextcord.Embed(title=":rat: **FrongonianUnits**", color=0x4287f5)
      embed.add_field(name="**Definition:**", value="Think about it like this, you have 182 watermelons and each cost 6 quid (Or 7 euros for my European folks. And 7 dollars for freedom lovers). in order to convert into frongonian units, you must take the squared derivative of each seed and calculate the megahertz it generates after a 15 ton, 31-year-old mother, has sat on it. from there you can calculate the amount of politeness each person interacts with the mother. the nicer, the more Canadian. convert it back to micro coulombs squared and you will get it in light year",inline=False)
      await interaction.response.send_message(embed=embed, ephemeral=False)

    @nextcord.slash_command(name="unfuckwithable", description="An old term from the early-late 1900s")
    async def unfuckwithable(self, interaction: nextcord.Interaction):
      embed = nextcord.Embed(title=":rat: **UnFuckWithable**", color=0x4287f5)
      embed.add_field(name="**Definition:**", value="Unfuckwithable, an old term dating back to the early-late 1900s (roughly 2 years after the CosmodiumCS debut). the term is used to describe any noun (person, place, creature, thing, or idea) that is incapable of being \"fucked with\". this term represents an older technological way of representing words via concatenative abbreviation, where the words are laid back-to-back to make a new word (of course inspired by gay seckz). this is dissimilar to words like \"frong\" (\"for real\", \"on God\") which are composed of two separate acronyms.",inline=False)
      await interaction.response.send_message(embed=embed, ephemeral=False)

def setup(bot):
  bot.add_cog(Frongcmd(bot))