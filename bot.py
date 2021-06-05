# Import Modules
import os # for loading cog files
import discord
from discord.ext import commands
# Custom Modules
import functions

#Gets prefix from db
def get_prefix(client, message):
  return functions.GetConfigValue('identifier', str(message.guild.id))

# Bots Description
description = "Hazzahs Bot"
# Initialize client
client = commands.Bot(command_prefix= get_prefix, case_insensitive=True, description=description, help_command=None)
# Get Discord Token From .env file
token = str(os.getenv("DiscordBotToken"))

# Load All Categorys in cogs folder
for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    client.load_extension(f'cogs.{filename[:-3]}')

@client.command()
async def botsguilds(ctx): 
  for guild in client.guilds:              
    await ctx.send(guild.name)

# Gets list of guilds connected to bot and updates to model
@client.event
async def on_guild_join(guild):
  Guildlist = []
  for item in client.guilds:              
      Guildlist.append(item.id)
      print(item.id)
  functions.UpdateConnectedGuilds(Guildlist)
  print('Added Guild ' + str(guild) + ' to Connected Guilds DB')

# Run Bot
client.run(token)