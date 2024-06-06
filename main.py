from dotenv import load_dotenv
import nextcord
from nextcord.ext import commands
import os
import aiohttp
from random import randint
import csv

load_dotenv()

def update_csv(name, filename):
    updated = False
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        rows = list(reader)
        for row in rows:
            if row['Name'] == name:
                row['Value'] = str(int(row['Value']) + 1)
                updated = True
                break
        else:
            rows.append({'Name': name, 'Value': '1'})
            updated = True

    if updated:
        with open(filename, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['Name', 'Value'])
            writer.writeheader()
            writer.writerows(rows)

def main():
    # allows privledged intents for monitoring members joining, roles editing, and role assignments
    intents = nextcord.Intents.default()
    intents.guilds = True
    intents.members = True
    intents.message_content = True
    activity = nextcord.Activity(
        type=nextcord.ActivityType.listening, name=f"calls to frongation"
    )

    bot = commands.Bot(
        command_prefix="/",
        intents=intents,
        activity=activity,
        owner_id="null",
    )

    csv_file = "data.csv"

    # responses for the arch user replies
    responses = ["",
    "Oh you use arch? Why don’t you `sudo pacman -S some-bitches`.", 
    """
    ```
    sudo pacman -Syu
    reboot

    grub rescue>
    ```    
    """,
    "https://tenor.com/view/arch-linux-linux-open-source-arch-i-use-arch-btw-gif-25315741",
    "https://tenor.com/view/arch-linux-i-use-arch-lonely-gif-26341678",
    "https://tenor.com/view/me-looking-for-who-asked-looking-for-who-asked-who-asked-me-looking-gif-20318322"
]

    # boolean that will be set to true when views are added
    bot.persistent_views_added = False

    @bot.event
    async def on_ready():
        print(f"USER: {bot.user} \nURL:", f"https://discord.com/api/oauth2/authorize?client_id={bot.user.id}&scope=applications.commands%20bot")
        print(f"{bot.user} standing by on...")
        print('\n'.join(guild.name for guild in bot.guilds))
        print(f"Loading cogs...")

    @bot.event
    async def on_message(message):
        # do not reply with anything if the message is from the bot
        if message.author == bot.user:
            return
        
        # convert message to all lowercase for case-insensitive matching
        content_lower = message.content.lower()

        # for arch linux replies
        arch_words = ["i use arch btw", "i use arch", "arch btw"]
        for word in arch_words:
            if word.lower() in content_lower:
                number = randint(0, len(responses) - 1)
                # arch form reply
                if number == 0:
                    await message.channel.send('An Arch user? You might need this.', files=[nextcord.File('arch_form.jpg')])
                    return
                # other insult reply
                else:
                    await message.channel.send(responses[number])
                    return

        # for frong response
        frong_words = ["frong"]
        for word in frong_words:
            if word.lower() in content_lower:
                # increment message author frong count
                update_csv(str(message.author), 'data.csv')

                # send frong response
                await message.channel.send('frong', files=[nextcord.File('frong.png')])
                return

    for filename in os.listdir('cogs'):
        if filename.endswith('.py'):
            bot.load_extension(f'cogs.{filename[:-3]}')

    async def startup():
        bot.session = aiohttp.ClientSession()

    bot.loop.create_task(startup())

    # run the bot
    bot.run(str(os.getenv('TOKEN')))


if __name__ == "__main__":
    main()

