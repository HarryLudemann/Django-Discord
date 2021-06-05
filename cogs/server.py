# Import Modules
import discord
from discord.ext import commands
# Custom Modules
import functions

client = discord.Client

class Basic(commands.Cog):

    def __init__(self, client):
        self.client = client
  
    @commands.Cog.listener()
    async def on_ready(self):
        print('Server Commands Ready')

    #Events
    # On Bot Successfully Connected
    @commands.Cog.listener()
    async def on_ready(self):
        print('We have logged in as {0.user}'.format(self.client))

    # On Member Join
    @commands.Cog.listener()
    async def on_member_join(self, member):
        await member.create_dm()
        await member.dm_channel.send( f'Hi {member.name}, welcome to my Discord server!' )

    # On Server Join
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        try:
            functions.CreateConfigFile(str(guild.id))
            print(f'Created .ini Infomation For {guild.name}')
        except:
            print(f'{guild.name} Rejoined')

    # Permission Checks
    # chat command
    def check_ping_permission(ctx): #Shows Error / Dont Remove
        role = discord.utils.get(ctx.guild.roles, name=str(functions.GetConfigValue('basic-ping', str(ctx.guild.id))))
        if role in ctx.author.roles:
            return True
    # chat command
    def check_changeprefix_permission(ctx): #Shows Error / Dont Remove
        role = discord.utils.get(ctx.guild.roles, name=str(functions.GetConfigValue('admin-changeprefix', str(ctx.guild.id))))
        if role in ctx.author.roles:
            return True

    #Commands
    # Help Command
    @commands.command()
    async def help(self, ctx):
        await ctx.send(''' ```
Hazzahs Discord Bot

Basic:
  help                Shows this message
  ping                Ping Bot

Fun:
  cat                 Returns Random Cat
  dog                 Returns Random Dog
  comeback {Target}   Returns Random Comeback
  inspire             Returns Inspirational Quote
       ``` ''')

    # Ping Command
    @commands.command(name='ping', help='Test Bot Is Active')
    @commands.check(check_ping_permission)
    async def ping(self, ctx):
        await ctx.send('Pong')

    # Change Prefix Command
    @commands.command(name='changeprefix', help='Change Prefix')
    @commands.check(check_changeprefix_permission)
    async def changeprefix(self, ctx, message):
        try:
            functions.SetConfigValue('identifier', message, str(ctx.guild.id))
            await ctx.send(f'Changed Prefix to {message}')
        except:
            print('Failed')

    # Get Current Server Info
    @commands.command(name='info', help='Server Info', pass_context = True)
    async def info(self, gui):
      await ctx.send(f'{ctx.author.name}, you are currently in {ctx.guild.name} ({ctx.guild.id}).')


def setup(client):
    client.add_cog(Basic(client))
