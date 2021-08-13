import discord
import time
from discord.ext import commands



bot_token= '' #Token do bot

client = commands.Bot(command_prefix='$', intents=discord.Intents.all()) #Definindo a variavel client, tendo como argumento o prefixo do comando.
                                                                         #Intents são as permissoes do bot para capturar e armazenar a presença dos usuários.
@client.event               #evento no inicio do bot
async def on_ready():

    print("Bot esta funcionando!" .format(client)) #log no console, para saber se o bot foi iniciado corretamente!
    print('Logado como {0.user}'  .format(client)) 
    await client.change_presence(activity=discord.Game(name="Primeiro Discordbot do Mergrow!")) # Atualiza o RPC do discordbot

ownerid = '<@337651715677618176>' #Meu UID pessoal do discord

@client.event                           #captura de mensagens nos canais de texto
async def on_message(message): 
    if message.author == client.user:
     return
  
    username = str(message.author) # autor da mensagem
    usermention = str(message.author.mention) #menção do autor da mensagem
    user_message = str(message.content) # conteúdo da mensagem
    channel = str(message.channel.name) # nome do canal em que a mensagem foi enviada.
    print(f'{channel} | {username}: {user_message} ') #Log da mensagem do usuário!

 #----------------------------COMANDOS DISCORD---------------------------------# 
    if user_message.lower() == '$salve':                        
        await message.channel.send(f'Salve {usermention}')

    elif user_message.lower() == '$dev':
        await message.channel.send (f'**Meu desenvolverdor é o: **' + (ownerid))

    elif user_message.lower() == '$linguagem':
        await message.channel.send ('Escrito em Python v3.9.6!')

    
    else:
        await client.process_commands(message)  #Se as mensagens acima nao forem registrados, ele irá procurar por comandos abaixo!


 #------------------------------------------------------------------------------# 


@client.command()
async def move(ctx, member: discord.Member, *, channel_name):
    if member.voice is None:
        # Se nao estiver conectado ao canal de voz envia essa mensagem.
        return await ctx.send('O usuários precisa estar em um canal de voz!')

    channel = discord.utils.get(ctx.guild.voice_channels, name=channel_name) #Define o channel com base na busca dos nomes de canais
    if channel is None:
        return await ctx.send('Canal inválido!') #retorna a mensagem de canal inválido caso o canal não seja encontrado.
    
    # mover o usuario
    await member.move_to(channel)

@client.command(aliases=['stream','live'])
async def twitch(message):
    usermention = str(message.author.mention)
    await message.send(f'{usermention} **Siga minha stream: https://www.twitch.tv/mergrow_ !**')

@client.command()
async def padilla(ctx):
    await ctx.send('*SimSim*')

#Wakeup move o usuário entre dois canais.
@client.command()
async def wakeup(ctx, member: discord.Member, ):
    if member.voice is None:
        return await ctx.send('O usuário precisa estar um canal de voz!')
    if member is ownerid:
        return await ctx.send('Meu mestre não pode ser acordado! ')
    saco1 = client.get_channel(683512951650779206) #define o id dos canais do wakeup (saco1)
    saco2 = client.get_channel(683512913130029058) #define o id dos canais do wakeup (saco2)
    await ctx.send(f'{member} ACORDA!!!!')
    await member.move_to(saco1) #move o usuário entre os carais saco1 e saco2
    time.sleep(0.1)
    await member.move_to(saco2)
    time.sleep(0.1)
    await member.move_to(saco1)
    time.sleep(0.1)
    await member.move_to(saco2)
    time.sleep(0.1)
    await member.move_to(saco1)
    time.sleep(0.1)
    await member.move_to(saco2)
    time.sleep(0.1)
    await member.move_to(saco1)
    time.sleep(0.1)
    await member.move_to(saco2)

#comandos de RPC
@client.command()
async def rpc(ctx):
    await client.change_presence(activity=discord.Streaming(name='Primeiro Discordbot do Mergrow!', url='https://www.twitch.tv/mergrow_', status=discord.Status.idle))

@client.command()
async def rpc2(ctx):
    await client.change_presence(activity=discord.Game(name='Primeiro Discordbot do Mergrow!', status=discord.Status.idle))

    
client.run(bot_token) #starta o bot usando o token.
