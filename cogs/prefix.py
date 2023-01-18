import datetime
import disnake


from disnake.ext import commands
from disnake.ext.commands import Cog

class Prefix(Cog):
    def __init__(self, bot: disnake):
        self.bot = bot


    @commands.command(name="prefix")
    async def prefix(self, ctx, prefix: str):

        name = str(ctx.author.name)
        nick = str(ctx.author.nick)


        if nick != 'None':
            nick = prefix + " " + nick

        else:
            nick = prefix + " " + name

        
        await ctx.author.edit(nick = nick)

        await ctx.message.add_reaction(emoji="<a:loadwave:1065016541239844977>")


    @commands.slash_command(name="prefix", description="сменить префикс (необязательно только себе)", )
    async def slash_prefix(ctx, prefix: str, user: disnake.Member = None, everyone: bool = False, remove: bool = False):

        await ctx.send("<a:loadwave:1065016541239844977>")

        if not user:
            name = str(ctx.author.name)
            nick = str(ctx.author.nick)
                             
        else:
            name = str(user.name)
            nick = str(user.nick)

        if not remove:
            if nick != 'None':
                nick = prefix + " " + nick

            else:
                nick = prefix + " " + name
        
        else:
            nick = nick.replace(prefix + " ", "")

        if everyone:
            for member in ctx.guild.members:
                try:
                    if member.nick:
                        nick = member.nick
                    else:
                        nick = member.name
                    if remove:
                        await member.edit(nick=nick.replace(prefix + " ", ""))
                    else:
                        await member.edit(nick=prefix + " " + nick)
                except:
                    pass


        else:
            nick = nick.replace(prefix + " ", "")
            await user.edit(nick = nick)


        await ctx.send(embed=disnake.Embed(title="<a:loadwave:1065016541239844977>", description=f"||Сменен префикс {user.mention} на '{prefix}'||", colour=disnake.Colour.green(), timestamp=datetime.datetime.now()), ephemeral=True)



    @prefix.error
    async def prefix_error(self, ctx, error):
        await ctx.send(embed=disnake.Embed(title="<a:loadwave:1065016541239844977>", description=f"||```{error}```||", colour=disnake.Colour.red(), timestamp=datetime.datetime.now()), delete_after=10)

    @slash_prefix.error
    async def prefix_error(self, ctx, error):
        await ctx.send(embed=disnake.Embed(title="<a:loadwave:1065016541239844977>", description=f"||```{error}```||", colour=disnake.Colour.red(), timestamp=datetime.datetime.now()), ephemeral=True)


def setup(bot: commands.Bot):
    bot.add_cog(Prefix(bot))