import nextcord
from nextcord.ext import commands

class TryAndSee(commands.Cog):
    def __init__(self,bot):
        self.bot=bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"try-and-see - Loaded")

    # for testing add guild_ids=[guild_id]
    @nextcord.slash_command(name="tryandsee", description="For people that are too lazy to try themselves.")
    async def tryandsee(self, interaction: nextcord.Interaction, question):
        await interaction.response.send_message("https://tenor.com/view/try-it-and-see-give-it-a-try-try-try-and-see-try-it-yourself-gif-24095805")

def setup(bot):
  bot.add_cog(TryAndSee(bot))
