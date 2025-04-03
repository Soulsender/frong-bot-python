# Frong Bot

[This project is deprecated, see the new project here.](https://github.com/Soulsender/frong-bot)

A multipurpose discord bot originally created for a meme.

### Functions
- `/askfrong` and `/askchatgpt` can be used to get the bot to use the ChatGPT API to respond in the theme of the god Frong, or to give a generic ChatGPT response.
- If a user says the word "frong" the bot will reply with "frong" and the attached image below.
    - It will also take note of the user, and add them to `data.csv` to count how many times they say frong in total. This `data.csv` files is mounted via docker volume for persistant storage through updates, and ease of backup ~~(if you REALLY care about backing this shit up, consider taking a shower)~~.
    - You can use `/leaderboard` to see frongs by users, and total frongs said.
    - ~~I put way too much time into this stupid project.~~
- If a user says "I use arch btw" or something of a similar degree, the bot will reply with a random response from a list of responses. These include gifs, images, and phrases.
- `/googlethat` can be used to sarcastically look something up for a user that is too lazy to do it themselves. The bot will reply with a link to [letmegooglethat.com](https://letmegooglethat.com/) with the search query specified.
- `/frong` and `/frongs` can be used to get the bot to respond with different urban-dictionary-esc phrases made by the CosmodiumCS community.

### Terms of Use / Privacy
- Frong bot uses the chatGPT API. This means that info it provides may/may not be correct. I take no responsibility for what the chatGPT API says.
- Using this bot means you agree to me storing your username, user ID, server name, server ID, and server members for use for statistics. This info is used so I can generate the leaderboard, and to give me credit for if I use this to get a job lol
- Using this bot means you agree to the risk of my server getting hacked and the bot used to destory your discord server by either spam or deletion or something similar. I don't want this to happen of course but it is an inherent risk. This is a hobby project, I don't take any responsibility for what the bot may or may not do.

# The frong in question:
Frong (for real, on God) is an expression used in the Cosmodium Cyber Security server for humorous means. It is most commonly utilised in a fashion of agreement about a given subject. Frong (for real, on God) is a derivative of “Fr” (for real) and “ong” (on God). It is not recognized as a legitimate word in the 2022 Oxford English Dictionary but is utilized nonetheless as a cultural reference of mutual agreement. This expression was first coined by Soulsender and CØ$MØ where the two individuals were saying “Fr Fr ong” (for real, for real, on God) as a method of agreement, where after the two expressions were merged to form the new commonly used phrase. Since the debut, the phrase has found use in a server emoji of a small mammal dubbed a “gerbil” with the text “frong” (for real, on God) displayed on the bottom of the image in 2013 type-2 impact font.

![](frong.png)
