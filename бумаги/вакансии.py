import datetime
import disnake
import pymongo

from disnake.ext import commands, tasks

class Вакансии(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot



def setup(bot: commands.Bot):
    bot.add_cog(Вакансии(bot))