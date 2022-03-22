import discord
import os
import random

#lets bot run offline from replit for an hour
from stay_alive import stay_alive # or whatever you named your file and function
stay_alive() # call the function

intents=intents=discord.Intents.all()
client = discord.Client(intents=intents)

#shows if bot is connected
@client.event
async def on_ready():
  print("Connected\n")
  print(client.user)

#generates greeting if new member joins server
@client.event
async def on_member_join(member):
  #yoosung dms welcome server message
  await member.create_dm()
  await member.dm_channel.send(
    f'Glad I can count on you to join me, {member.name}.')

#bot outputs random quote if user inputs assigned message
@client.event
async def on_message(message):
  if message.author == client.user:
    return

  albedo_quotes = [
    'If one day, I lose control... destroy Mondstadt... destroy everything...',
    'Can I rely on you to stop me?',
    'Have you ever considered that the world of Teyvat may have a natural hostility to outlanders?',
    'I am Albedo, Chief Alchemist of the Knights of Favonius.',
    'You carry the aura of the stars, interesting...',
    'I would like to study you, if you do not mind.',
    'I\'m certain we will have many opportunities to be alone in the future.',
    'One day, I will uncover its secrets, it\'s only a matter of time.',
    'Genius? ... A number of people call me that. But I don\'t think I\'m any "genius."',
    'The capacity of our brains is limited, so we are bound to forget things.',
    'Would you oblige me by serving as my assistant?',
    'After observing so many experiments, you surely know a good deal about alchemy by now.',
    'I have faith in my ability to instruct you, and even more faith in your exceptional talents.',
    'Your help inspired me to discover the means to make a flower bloom.',
    'Everything you do is an action I wish to observe.',
    'I mean that the time that I\'ve spent traveling with you in the mountains was a valuable journey for me.',
    'In the future... If the need arises... Can I solicit your help again?',
    'Those born of earth are bound by its imperfections, but those born of chalk are free of impurities... You and I are alike, both composed of a substance that has yet to be fully defined...',
    
  ]

  if message.content == 'albedo.' or message.content == 'Albedo.' or message.content == 'ALBEDO.':
    response = random.choice(albedo_quotes)
    await message.channel.send(response)

  albedo_replies = [
  'I can agree.',
  'The evidence doesn\'t support it.',
  'I am conflicted.',
  'I need to consult with Sucrose first.',
  'Further research is required.',
  'Oui.',
  'Non.',
  'The truth of this world... What could it be?',
  'I don\'t think you will have any problems.',
  'My calculations were off...',
  'Let\'s investigate this further.',
  'Relax, we will work together.',
  'I have faith in your ability to discern the truth.',
  'My experiments indicate a positive result.',
  'Such failure appeared...',
  'It should now be possible.',
  'To the best of my knowledge, I conclude it\'s false.',
  'There\'s still a lot to learn.',
  'I\'ll make time to go over it in greater detail after our research.',
  'I may just have a fleeting miracle for you to witness.',
  'I\'ve just about reached a conclusion.',
  'I got a myriad of data today, and it was very difficult sorting through, but I can perceive a likely outcome.',
  'By how it\'s going, I doubt it\'ll come into fruition.',
  'These calculations makes me wonder if we\'ll even see anything positive.',
  'But the integral preliminary conclusion that I can offer you is... Impossible.',
  'But the integral preliminary conclusion that I can offer you is... Unlikely.',
  'It\'s arguably a small miracle',
  'It would seem that that\'s as far as it go.',
  ]
    
  if 'albedo?' in message.content:
    replies = random.choice(albedo_replies)
    await message.channel.send(replies)

  if 'Albedo?' in message.content:
    replies = random.choice(albedo_replies)
    await message.channel.send(replies)

  if 'ALBEDO?' in message.content:
    replies = random.choice(albedo_replies)
    await message.channel.send(replies)
    
my_secret = os.environ['albedo_key']
client.run(my_secret)
