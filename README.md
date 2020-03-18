# CSATDiscordBot
A bot for discord created by the CSAT club at North Idaho College

## Commands: 
`!help` - command shows all possible commands, and what they do

`!hello` - command to get a warm greeting from the bot

`!coinflip` - flips a coin and either responds with Heads! or Tails!

## Getting started:
### Creating a bot
1. Sign in to your account here: https://discordapp.com/developers
2. Press "New Application" in the top right
3. Once the application is created, click on "Bot" and "Add Bot"
**Note: copy the token generated on the "Bot" page. you will need this later in step 8)**
4. Head to "OAuth2" on the left side of the screen

    a) under scopes, click on bot

    b) under privileges, click on Administrator

    c) Copy and paste the link generated (located under scopes) into your web browser

### Adding the bot to a server
5. After following the aforementioned link, you should be able to add the bot to any server you own.
6. Your bot has now just joined the server, although it cannot do any commands just yet.

### Setting up the bot
7. Download python 3.6 or higher if you have not already done so: https://www.python.org/downloads/
7. Clone or download the repository
8. Open token.txt and replace the first line with your bot token you collected from step 3
9. Open your terminal, and type in `pip intall discord`

10. Navigate to the root directory of the repository in your terminal, and type in `bot.py`

11. The bot should now be running on all connected servers, so long as that program is running!

