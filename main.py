import discord
import os
from replit import db
client = discord.Client()

# Variables
text = []
recentUser = 0
userInput = ""

#takes in array parameter and returns single string
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
  channels = ["one-word-story", "hangman"]
  
  if message.author == client.user:
    return
    
  # if bot recieves this type of message
  if message.content.startswith('$testing'):
    # bot replies
    await message.channel.send('testing')

  # One Word Story ------------------------------------

  if str(message.channel) in channels[0]:


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
  

  # Hangman ----------------------------------------
from random_word import randomWords


  if str(message.channel) in channels[1]:
    if message.content.startswith('$play'):
      



client.run(os.getenv('TOKEN'))