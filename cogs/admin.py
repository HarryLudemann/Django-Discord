# Import Modules
import discord
from discord.ext import commands
# Custom Modules
import functions

class Basic(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Permission Checkers
    #q command permissions 
    def check_q_permission(ctx): #Shows Error / Dont Remove
        role = discord.utils.get(ctx.guild.roles, name=str(functions.GetConfigValue('admin-quit', str(ctx.guild.id))))
        if role in ctx.author.roles:
            return True


    #Commands
    # Stop Bot
    @commands.command(name='q', help='Stop Bot', pass_context = True)
    @commands.check(check_q_permission)
    async def q(self, ctx):
        await exit()

def setup(client):
    client.add_cog(Basic(client))
