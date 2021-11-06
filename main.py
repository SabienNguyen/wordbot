import discord
import os
from replit import db
client = discord.Client()

# Variables
global text 
text = []

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
  global text
  
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
      userInput = message.content.split("$add ")
      text.append(userInput[1])
      text.append(" ")
      await message.add_reaction("✅")

    if message.content.startswith('$end'):
      # await message.channel.send(text)
      await message.channel.send(arrayToString(text))
      text.clear()

client.run(os.getenv('TOKEN'))