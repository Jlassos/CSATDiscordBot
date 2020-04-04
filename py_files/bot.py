import discord
import coin_flip, bot_help, tictactoe, states

client = discord.Client()
state = states.State() # a state machine to keep track of different games 
                       # or modes it is in
with open("token.txt", 'r') as file: #opens file and gets token
    TOKEN = file.readline()

@client.event
async def on_ready(): # called when bot gets logged in
    print(f"We have logged in as {client.user}")
    

@client.event
async def on_reaction_add(reaction, user):
    if user == client.user: # if message sent by bot
        return

    if state.tictactoe: # if there is a ttt game
        for game in state.tictactoe:
            if user == game.PLAYER and \
                reaction.message.id == game.message.id: # if reaction for tictactoe
                await game.do_move(reaction)
                return



@client.event
async def on_message(message): # called when a message is sent
    if message.author == client.user: # if message is sent by the bot
        return

    if message.content.startswith("!help"):
        await bot_help.bot_help(message)

    if message.content.startswith("!hello"):
        await message.channel.send("Hello there.")

    if message.content.startswith("!coinflip"):
        await coin_flip.coinflip(message)

    if message.content.startswith("!tictactoe"):
        state.tictactoe.append(tictactoe.TicTacToe(message))
        await state.tictactoe[-1].create_board()


client.run(TOKEN)
