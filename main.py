import discord
import os
client = discord.Client()


# Returns concatenated list of words in text into s
def concatenatedResult(s, text):
  for item in text:
    s += item
  return s;

# Check to see if wordbot is running at all
@client.event
async def on_ready():
  print('Logged in as {0.user}'.format(client))

# runs each time messages is receieved
@client.event
async def on_message(message):
  
  # gets server id so it knows where to go
  channels = ["one-word-story"]
  text = [ ]
  s = "add smth here "


  if message.author == client.user:
    return
    
  # if bot recieves this type of message
  if message.content.startswith('$testing'):
    # bot replies
    await message.channel.send('testing')

  if str(message.channel) in channels:

    #add a story
    if message.content.startswith('$add'):
      text = message.content.split(' ')
      text.remove('$add')

      # Concatenate all words to form a sentence.
      # for item in text:
      #   s += item
      
      await message.channel.send(text)
      return s


    if message.content.startswith('$end'):
      await message.channel.send(concatenatedResult(s, text))

      
      #Keeps waiting user(s) to add more words until they type $end?
      # sentence = message.content.split(" ");
      # sentence.shift();
      # sentence = sentence.join(" ");
      # message.channel.send(sentence);
      





  
     

    





client.run(os.getenv('TOKEN'))