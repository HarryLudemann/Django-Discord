# Import Modules
import discord
from discord.ext import commands

class Error_Handler(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    # Events
    # Check For Error And Send Result
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please specify the amount of messages you want to clear. Usage: //clear <number>')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send('You do not have manage_messages permssion')
        if isinstance(error, commands.MissingAnyRole):
            await ctx.send('You do not have required role')

def setup(client):
    client.add_cog(Error_Handler(client))
