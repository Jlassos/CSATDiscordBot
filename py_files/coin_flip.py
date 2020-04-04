import random

async def coinflip(message):
    the_message = random.choice(["Heads!", "Tails!"])
    await message.channel.send(the_message)
