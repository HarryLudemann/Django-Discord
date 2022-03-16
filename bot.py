import os # for loading cog files
import discord
from discord.ext import commands
# Custom Modules
import functions

#Gets prefix from db
def get_prefix(client, message):
  prefix = functions.GetConfigValue('identifier', str(message.guild.id))
  return prefix

client = commands.Bot(command_prefix= get_prefix, case_insensitive=True, description="Hazzahs Bot", help_command=None)
token = str(os.getenv("DiscordBotToken"))

for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    client.load_extension(f'cogs.{filename[:-3]}')

# @client.command()
# async def botsguilds(ctx): 
#   for guild in client.guilds:              
#     await ctx.send(guild.name)

def update_connected_bots(guild):
  """ Gets list of guilds connected to bot and updates to model """
  Guildlist = []
  for item in client.guilds:              
      Guildlist.append(item.id)
  functions.UpdateConnectedGuilds(Guildlist)

@client.event
async def on_guild_join(guild):
  update_connected_bots(guild)

@client.event
async def on_guild_remove(guild):
  update_connected_bots(guild)


# Run Bot
client.run(token)
