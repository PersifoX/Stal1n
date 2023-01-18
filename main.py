# main components | Этот код полное дерьмище, прошу меня простить

print("loading...")
print("-----------------------")

import disnake
import threading
import asyncio
import logging

import tools.read_command as read

from disnake.ext import commands
from colorama    import Fore, Style
from dotenv      import load_dotenv
from os          import getenv, listdir


load_dotenv()

print(Fore.GREEN + "libs imported")
print("-----------------------" + Fore.MAGENTA)

# main class

bot  = commands.Bot(command_prefix=commands.when_mentioned_or(getenv("PREFIX")), intents=disnake.Intents.all())
read = read.Readinput(bot=bot)

logging.basicConfig(level=logging.INFO, filename="statusx.log", filemode="w", format="%(asctime)s %(levelname)s %(message)s")

# funcs for cogs

def cogsLoad(self):
        curr, total = 0, len(listdir("./cogs")) - 1
        for filename in listdir("./cogs"):
            if filename.endswith(".py"):
                self.load_extension(f"cogs.{filename[:-3]}")
                curr += 1
                print(f"cog {filename} load, {curr}/{total}")

        print("-----------------------" + Style.RESET_ALL)

# load cogs

cogsLoad(bot)

# events

@bot.event
async def on_disconnect():
    print(Fore.RED +  "\n-----------------------\nbot disconnected or connection failed\n-----------------------" + Style.RESET_ALL)
    logging.warning("bot disconnected")

@bot.event
async def on_connect():
    print(Fore.GREEN +  "\n-----------------------\nbot connected\n-----------------------" + Style.RESET_ALL)
    logging.info("bot connected")

@bot.event
async def on_error(type, event):
    print(Fore.RED +  "\n-----------------------\n error event saved to statusx.log \n-----------------------" + Style.RESET_ALL)
    logging.error(f"{type}:\n{event}")

@bot.event
async def on_ready():

    print(Fore.CYAN + f"Starting as {bot.user} (ID: {bot.user.id})")
    print("-----------------------" + Style.RESET_ALL)
    print(Fore.GREEN + "Started!")
    print("-----------------------" + Style.RESET_ALL)

    await bot.change_presence(status=disnake.Status.idle, activity=disnake.Streaming(name="persifox.space", url="https://twitch.com/"))
    
    # async cmd input
    threading.Thread(target=forever, name="CMD").start()

    print(Fore.LIGHTCYAN_EX + "Waiting for input")
    print("-----------------------" + Style.RESET_ALL)
    
    logging.info("bot ready")


def forever():
    loop = asyncio.new_event_loop()
    loop.run_until_complete(read.readinput())
    loop.close()




bot.run(getenv("TOKEN"))