# Import Modules
import discord
from discord.ext import commands
# Custom Modules
import functions

client = discord.Client

class Basic(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Permission Checkers
    # test command permissions 
    def check_test_permission(ctx): #Shows Error / Dont Remove
        role = discord.utils.get(ctx.guild.roles, name=str(functions.GetConfigValue('admin-test', str(ctx.guild.id))))
        if role in ctx.author.roles:
            return True


    #Commands
    # test command
    @commands.command(name='test', help='Stop Bot', pass_context = True)
    @commands.check(check_test_permission)
    async def test(self, ctx):
        activeservers = ctx.guilds
        for guild in activeservers:
            print(guild.name)
            print(guild.id)
        await ctx.send(str(len(activeservers)))

def setup(client):
    client.add_cog(Basic(client))
