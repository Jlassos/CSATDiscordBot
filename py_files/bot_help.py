async def bot_help(message):
    the_message = ("```!help - command shows all possible commands, and what they do"
                       "!hello - command to get a warm greeting from the bot"
                       "!coinflip - flips a coin and either responds with Heads! or Tails!"
                       "!tictactoe - command to start a tic tac toe game```")
    await message.channel.send(the_message)
