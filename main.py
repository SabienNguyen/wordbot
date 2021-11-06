import discord
import os
from replit import db
client = discord.Client()

# Variables
text = []
recentUser = 0
userInput = ""

def arrayToString(text):
  story = ""
  for word in text:
    story += word
  return story
    

# Check to see if wordbot is running at all
@client.event
async def on_ready():
  print('Logged in as {0.user}'.format(client))

# runs each time messages is receieved
@client.event
async def on_message(message):
  global text, recentUser, userInput
  
  # gets server id so it knows where to go
  channels = ["one-word-story"]
  
  if message.author == client.user:
    return
    
  # if bot recieves this type of message
  if message.content.startswith('$testing'):
    # bot replies
    await message.channel.send('testing')

  if str(message.channel) in channels:


    #add a story
    if message.content.startswith('$add'):
      if(recentUser != message.author.id):
        recentUser = message.author.id
        userInput = message.content.split(" ")
        text.append(userInput[1])
        text.append(" ")
        await message.add_reaction("✅")
      else:
        await message.add_reaction("❌")
        await message.channel.send("You have to wait for someone else to message!")
      
      if len(userInput) > 2: 
        await message.channel.send("Only first word is taken: " + userInput[1])
      
      

    elif message.content.startswith('$end'):
      # await message.channel.send(text)
      await message.channel.send(arrayToString(text))
      text.clear()

    # else:
    #   await message.add_reaction("❌")

client.run(os.getenv('TOKEN'))