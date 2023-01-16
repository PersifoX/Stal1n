import datetime
import disnake


from disnake.ext import commands
from disnake.ext.commands import Cog

class Власть(Cog):
    def __init__(self, bot: disnake):
        self.bot = bot

    @commands.command(name="afk")
    async def afk(self, ctx):

        if " [отошел]" in ctx.author.nick:
            return

        if ctx.author.nick:
            nick = ctx.author.nick + " [отошел]"
        else:
            nick = ctx.author.name + " [отошел]"
        
        await ctx.author.edit(nick = nick)


    
    @Cog.listener()
    async def on_message(self, message):
        
        if message.author != self.bot:

            if " [отошел]" in  message.author.nick:

                nick = message.author.nick.replace(" [отошел]", "")

                await message.author.edit(nick = nick)

                await message.add_reaction(emoji="🟢")



    @afk.error
    async def timeout_error(self, ctx, error):
        await ctx.send(embed=disnake.Embed(title="⭕", description="```Бот не имеет разрешений для выполнения. Пересмотрите его права, или поставьте его роль выше вашей.```", colour=disnake.Colour.red(), timestamp=datetime.datetime.now()), delete_after=5)



def setup(bot: commands.Bot):
    bot.add_cog(Власть(bot))