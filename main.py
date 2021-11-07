import discord
import os
import requests
from random import randint
# from replit import db
client = discord.Client()

#----------------One Word Story------------------
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
    
#-------------------------------------------------

#------------------Hangman---------------------------

def inWord(guess, randWord):
  for letter in randWord:
    if guess == letter:
      return True
      print("trint")
  return False


#-------------------------------------------------
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

  #Variables

  #Word List
  word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
  response = requests.get(word_site)
  randWordList = response.content.splitlines()

  if str(message.channel) in channels[1]:
    if message.content.startswith('$play'):
      global randWord, gameStatus, lives, win
      
      gameStatus = True
      randWord = ""
      lives = 6
      win = False
      difficultyInput = message.content.split(" ")

      #Choose random word 5 letters or less
      if (difficultyInput[1] == "easy"):
        randWord = randWordList[randint(0, 9999)]
        while len(randWord) > 5:
          randWord = randWordList[randint(0, 9999)]
        await message.channel.send("Easy: " + str(len(randWord)))
      #Choose random word 6-11 letters
      elif difficultyInput[1] == "medium":
        randWord = randWordList[randint(0, 9999)]
        while  6 > len(randWord) > 11:
         randWord = randWordList[randint(0, 9999)]
        await message.channel.send("Medium: " + str(len(randWord)))
      #Choose random word 12 letters or more
      elif difficultyInput[1] == "hard":
        randWord = randWordList[randint(0, 9999)]
        while len(randWord) < 12:
          randWord = randWordList[randint(0, 9999)]
        await message.channel.send("Hard: " + str(len(randWord)))
      #Prints error message if user doesn't type "easy","medium", or "hard"
      else:
        await message.channel.send("Invalid difficulty/Game is currently going on")

      s = ""
      for range in randWord:
        s+= "\_ "
      await message.channel.send(s)

      
      # await message.channel.send()
    if gameStatus == True:
      if message.content.startswith('$guess '):
        userInput = message.content.split(" ")
        guess = userInput[1]
        await message.channel.send("You just guessed..." + guess)
        await message.channel.send(randWord)
        if guess in randWord.decode("utf-8") :
          await message.channel.send("AY nice")
          await message.channel.send(s)
          win = True
        else:
          await message.channel.send("Nope, try again")
          lives -= 1
          await message.channel.send(lives) #DELETE OR CHANGE
      await message.channel.send(win)
    if lives <= 0:
      gameStatus = False
      await message.channel.send("Awww, maybe next time")
      await message.channel.send("type $play to play again")

      
      
      
      

        
    
    


 # await settings.message.add_reaction("🍎")
      # await settings.message.add_reaction("🍊")
      # awai csettings.messagemad_reaction("🍋")


client.run(os.getenv('TOKEN'))