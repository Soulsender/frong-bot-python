import nextcord
from nextcord.ext import commands
from dotenv import load_dotenv
import openai
import os

openai.api_key = str(os.getenv('OPENAI_KEY'))

def ask_chatgpt(question):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", 
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": question},
            ]
        )
        return response['choices'][0]['message']['content']

class AskFrong(commands.Cog):
    def __init__(self,bot):
        self.bot=bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"ask-frong - Loaded")

    # for testing add guild_ids=[guild_id]
    @nextcord.slash_command(name="askfrong", description="Ask the almighty.", guild_ids=[414625175217242113])
    async def askfrong(self, interaction: nextcord.Interaction, question):
        answer = ask_chatgpt(question)
        await interaction.response.send_message(f"{answer}")

def setup(bot):
  bot.add_cog(AskFrong(bot))