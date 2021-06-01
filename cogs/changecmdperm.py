# Import Modules
import discord
from discord.ext import commands
# Custom Modules
import functions

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
        await ctx.send(f"y or n")
        msg = await self.client.wait_for("message", timeout=60, check=lambda message: message.author == ctx.author and message.channel == ctx.channel)
        if (msg.text == "y"):
            await ctx.send("y pressed")
        elif (msg.text == "n"):
            await ctx.send("n pressed")
        else:
            await ctx.send('Only n or y')


def setup(client):
    client.add_cog(Basic(client))
