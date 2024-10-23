import nextcord
from nextcord.ext import commands
import os
import csv

# get path name for csv file
file_path = os.path.join(os.getcwd(), "data")
csv_file = "data.csv"
file_path = os.path.join(file_path, csv_file)
print(file_path)

class Leaderboard(commands.Cog):
    def __init__(self,bot):
      self.bot=bot

    @commands.Cog.listener()
    async def on_ready(self):
      print(f"leaderboard - Loaded")

    @nextcord.slash_command(name="leaderboard", description="Frong leaderboard")
    async def leaderboard(self, interaction: nextcord.Interaction):
      await interaction.response.defer()
      csv_dict = {}
      data = ""
      total = 0
      with open(file_path, 'r') as file:
          reader = csv.DictReader(file)

          # turn csv into dictionary
          for row in reader:
              key = row.pop('Name')  # Replace 'Key_Column_Name' with the actual column name for the key
              csv_dict[key] = row

          # sort the dictionary
          sorted_dict = dict(sorted(csv_dict.items(), key=lambda x: int(x[1]['Value']), reverse=True))

          # get values from dictionary
          for key, value in sorted_dict.items():
              content = "**" + key + "**: "
              data += content
              for key2, value2 in dict(value).items():
                  content2 = value2 + "\n"
                  data += content2
                  total += int(value2)

      # send embed
      embed = nextcord.Embed(title=":crown: **LEADERBOARD**", color=0xd6b509)
      embed.add_field(name=":speech_balloon: __FRONGS BY USER__", value=data,inline=False)
      embed.add_field(name=":loudspeaker: __TOTAL FRONGS__", value=total,inline=False)
      await interaction.followup.send(embed=embed, ephemeral=False)

def setup(bot):
  bot.add_cog(Leaderboard(bot))
