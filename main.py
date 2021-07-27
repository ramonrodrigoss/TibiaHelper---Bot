import os
import discord
my_secret = os.environ['TOKEN']
from keep_alive import keep_alive

from boosted_creature import criatura_dia

import threading

def hello():
    t = threading.Timer(3600.0, hello)
    t.start()
    criatura_dia()
    print('criatura carregada!') 

t = threading.Timer(3600, hello)
t.start() 
 


nome, foto = criatura_dia()
###############################################################
client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

  
  

@client.event
async def on_message(message):
  
  if message.author == client.user:
    return



#################################################
  if message.content.startswith('!ola'):
    await message.channel.send('Olá, {0.author.mention}!'.format(message))
    
#################################################


  if message.content.startswith('!criatura'):

    await message.channel.send('Olha, {0.author.mention}, a Criatura do dia é...'.format(message))
    await message.channel.send(content = nome)
    embed1 = discord.Embed()
    embed1.set_image(url=foto)
    await message.channel.send(embed=embed1)




keep_alive()
client.run(os.getenv("TOKEN")) #get your bot token and create a key named `TOKEN` to the secrets panel then paste your bot token as the value. 
#to keep your bot from shutting down use https://uptimerobot.com then create a https:// monitor and put the link to the website that appewars when you run this repl in the monitor and it will keep your bot alive by pinging the flask server
#enjoy!