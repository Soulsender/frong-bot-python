import nextcord
from nextcord.ext import commands

class GoogleThat(commands.Cog):
    def __init__(self,bot):
        self.bot=bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"google-that - Loaded")

    # for testing add guild_ids=[guild_id]
    @nextcord.slash_command(name="googlethat", description="For people that are too lazy to google themselves.")
    async def googlethat(self, interaction: nextcord.Interaction, question):
        text_new = question.replace(" ", "+")
        url = f"https://letmegooglethat.com/?q={text_new}"
        await interaction.response.send_message(f"[{question}]({url})")

def setup(bot):
  bot.add_cog(GoogleThat(bot))