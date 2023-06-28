import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Je suis : {client.user.name}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    content = message.content.lower()

    if "hein" in content:
        await message.channel.send("Apagnan")
    elif "quoi" in content:
        await message.channel.send("Quoicoubeh")

client.run('TON_TOKEN')