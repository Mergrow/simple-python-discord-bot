import discord

bot_token= 
client = discord.Client()

@client.event
async def on_ready():

    print("Bot esta funcionando! Logado como {0.user}" .format(client))

ownerid = '<@337651715677618176>'

@client.event
async def on_message(message):
    if message.author == client.user:
     return

    username = str(message.author).split('$')[0]
    usermention = str(message.author.mention).split('$')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f' {username}: {user_message} {channel}')

 #----------------------------COMANDOS DISCORD---------------------------------# 
    if user_message.lower() == '$salve':
        await message.channel.send(f'Salve {usermention}')

    if user_message.lower() == '$dev':
        await message.channel.send (f'**Meu desenvolverdor é o: **' + (ownerid))

    if user_message.lower() == '$linguagem':
        await message.channel.send ('Escrito em Python v3.9.6!')

 # ----------------------------------------------------------------------------#

client.run(bot_token)
