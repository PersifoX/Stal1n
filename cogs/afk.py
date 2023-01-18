import datetime
import disnake


from disnake.ext import commands
from disnake.ext.commands import Cog

class Власть(Cog):
    def __init__(self, bot: disnake):
        self.bot = bot

    @commands.command(name="afk")
    async def afk(self, ctx):

        name = str(ctx.author.name)
        nick = str(ctx.author.nick)

        if " [отошел]" in nick:
            return

        if nick != 'None':
            nick = nick + " [отошел]"

        else:
            nick = name + " [отошел]"

        
        await ctx.author.edit(nick = nick)

        await ctx.message.add_reaction(emoji="<a:loadwave:1065016541239844977>")


    
    @Cog.listener()
    async def on_message(self, message):
        
        if message.author != self.bot:

            if " [отошел]" in  str(message.author.nick):


                nick = message.author.nick.replace(" [отошел]", "")

                await message.author.edit(nick = nick)

                await message.add_reaction(emoji="<a:verify:1065016038170820608>")



    @afk.error
    async def afk_error(self, ctx, error):
        await ctx.send(embed=disnake.Embed(title="<a:loadwave:1065016541239844977>", description=f"||```{error}```||", colour=disnake.Colour.red(), timestamp=datetime.datetime.now()))



def setup(bot: commands.Bot):
    bot.add_cog(Власть(bot))