# Import Modules
import os # for loading cog files
import discord
from discord.ext import commands
from discord.utils import get
# Custom Modules
import functions

#Django Functions:
# def GetGuilds():
#   guilds = client.fetch_guilds(limit=150).flatten()
#   return guilds

# def GetGuildMembers(ID):
#   guild = client.get_guild(ID)
#   memberList = guild.members
#   for item in memberList:
#     print(item)


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
# Run Bot
client.run(token)