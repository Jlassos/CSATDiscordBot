import discord
import random

client = discord.Client()
with open("token.txt", 'r') as file: #opens file and gets token
    TOKEN = file.readline()

@client.event
async def on_ready(): # called when bot gets logged in
    print(f"We have logged in as {client.user}")
    
@client.event
async def on_message(message): # called when a message is sent
    if message.author == client.user: # if message is sent by the bot
        return

    if message.content.startswith("!help"):
        await bot_help(message)

    if message.content.startswith("!hello"):
        await message.channel.send("Hello there.")

    if message.content.startswith("!coinflip"):
        await coinflip(message)


async def bot_help(message):
    the_message = ("Try calling one of the commands below!\n```"
                   "!hello      makes me greet you back\n"
                   "!coinflip   very helpful if you are indecisive```")
    await message.channel.send(the_message)

async def coinflip(message):
    the_message = random.choice(["Heads!", "Tails!"])
    await message.channel.send(the_message)


client.run(TOKEN)
