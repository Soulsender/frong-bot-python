import nextcord
from nextcord.ext import commands
from dotenv import load_dotenv
from openai import OpenAI
import os

client = OpenAI(api_key=str(os.getenv('OPENAI_KEY')))

def ask_chatgpt(question):
        response = client.chat.completions.create(model="gpt-3.5-turbo", 
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": question},
        ])
        return response.choices[0].message.content

class AskChatGPT(commands.Cog):
    def __init__(self,bot):
        self.bot=bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"chatgpt - Loaded")

    # for testing add guild_ids=[guild_id]
    @nextcord.slash_command(name="chatgpt", description="Ask ChatGPT.")
    async def askchatgpt(self, interaction: nextcord.Interaction, question):
        answer = ask_chatgpt(question)
        await interaction.response.send_message(f"**Question: **{question} \n\n **Answer: **{answer}")

def setup(bot):
  bot.add_cog(AskChatGPT(bot))