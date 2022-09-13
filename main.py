#---main components---

print("загрузка...")
print("-----------")

import disnake
from disnake.ext import commands, tasks
from asyncio import sleep
from colorama import Fore, Style
from dotenv import load_dotenv
from os import getenv, listdir
load_dotenv()

print(Fore.GREEN + "бумаги загружены")
print("-----------------------" + Fore.MAGENTA)

#---main class--------

bot = commands.Bot(command_prefix=commands.when_mentioned_or(getenv("PREFIX")), intents=disnake.Intents.all()) #slash command only OR when mentioned


def cogsLoad(self):
        curr, total = 0, len(listdir("./бумаги")) - 3
        for filename in listdir("./бумаги"):
            if filename.endswith(".py"):
                self.load_extension(f"бумаги.{filename[:-3]}")
                curr += 1
                print(f"бумага {filename} загружена, {curr}/{total}")

        print("-----------------------" + Style.RESET_ALL)

cogsLoad(bot)


@bot.event
async def on_ready():
    
    print(Fore.CYAN + f"Стал править СССР как {bot.user} (ID: {bot.user.id})")
    print("-----------------------" + Style.RESET_ALL)
    print(Fore.GREEN + "Сталин на посту!")
    print("-----------------------" + Style.RESET_ALL)

    while True:
        await bot.change_presence(status=disnake.Status.dnd, activity=disnake.Activity(type=disnake.ActivityType.listening, name=f"гимн СССР на {len(bot.guilds)} республиках")) #set activity to watching AlonClub
        await sleep(5)


bot.run(getenv("TOKEN"))