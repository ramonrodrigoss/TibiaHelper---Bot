import os
import discord
my_secret = os.environ['TOKEN']
from keep_alive import keep_alive
from boosted_creature import criatura_dia
from datetime import datetime
import os
import threading

#def hello():
    #t = threading.Timer(30.0, hello)
   # t.start() 
    #criatura_dia()
    ##data = str(datetime.datetime.now())
    #print('criatura carregada!'+data) 
#t = threading.Timer(30.0, hello)
#t.start() 



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
    data_e_hora_atuais = datetime.now()
    data= data_e_hora_atuais.strftime('%d/%m/%Y %H:%M:%S')



    await message.channel.send('Olá, {0.author.mention}!'.format(message))
    print("jogador {0.author} usou o comando !ola às " .format(message)+data)
    
    with open ('logs.txt', 'a') as log:
      log.write("jogador {0.author} usou o comando !ola às ".format(message)+data)
    
#################################################


  if message.content.startswith('!criatura'):

    await message.channel.send('Olha, {0.author.mention}, a Criatura do dia é...'.format(message))
    
    with open ('criatura.txt', 'r+') as arquivo:
      bixin = arquivo.readlines(1)
      bixin = str(bixin[0])

      fotin = arquivo.readlines(2)
      fotin = str(fotin[0])

    await message.channel.send(content = bixin)
    embed1 = discord.Embed()
    
    embed1.set_image(url=fotin)
    await message.channel.send(embed=embed1)
    print("jogador {0.author} usou o comando !criatura".format(message))




keep_alive()
client.run(os.getenv("TOKEN")) #get your bot token and create a key named `TOKEN` to the secrets panel then paste your bot token as the value. 
#to keep your bot from shutting down use https://uptimerobot.com then create a https:// monitor and put the link to the website that appewars when you run this repl in the monitor and it will keep your bot alive by pinging the flask server
#enjoy!