import discord
import os
from replit import db
client = discord.Client()

global text 
text = []

# Returns concatenated list of words in text into s
def concatenatedResult(s, text):
  for item in text:
    s += item
  return s;

def appendConcatenatedResults(word):
  if "text" in db.keys():
    text = db["text"]
    text.append(word)
    db["text"] = text
  else:
    db["text"] = [word]





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
  s = "... "
  
  


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
      # elif message.content.startswith('$end'):
      #     plsWork = True
      await message.channel.send(text)

    

          
          
    # return text


    # if message.content.startswith('$end'):
    #   await message.channel.send(concatenatedResult(s, text)

      
      #Keeps waiting user(s) to add more words until they type $end?
      





  
     

    





client.run(os.getenv('TOKEN'))