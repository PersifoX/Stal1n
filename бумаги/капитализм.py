import datetime
import disnake
import pymongo

from бумаги.Завод.документ import Документ
from disnake.ext import commands, tasks

class Капитализм(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot



def setup(bot: commands.Bot):
    bot.add_cog(Капитализм(bot))