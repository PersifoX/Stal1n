# main components

print("loading...")
print("-----------")

import disnake
import datetime

from disnake.ext import commands
from colorama    import Fore, Style
from dotenv      import load_dotenv
from os          import getenv, listdir

load_dotenv()

print(Fore.GREEN + "libs imported")
print("-----------------------" + Fore.MAGENTA)

# main class

bot = commands.Bot(command_prefix=commands.when_mentioned_or(getenv("PREFIX")), intents=disnake.Intents.all())

# funcs for cogs

def cogsLoad(self):
        curr, total = 0, len(listdir("./cogs")) - 1
        for filename in listdir("./cogs"):
            if filename.endswith(".py"):
                self.load_extension(f"cogs.{filename[:-3]}")
                curr += 1
                print(f"cog {filename} load, {curr}/{total}")

        print("-----------------------" + Style.RESET_ALL)

def cogsReload(self):
        print(Fore.CYAN + "-----------------------")
        curr, total = 0, len(listdir("./cogs")) - 1
        for filename in listdir("./cogs"):
            if filename.endswith(".py"):
                self.reload_extension(f"cogs.{filename[:-3]}")
                curr += 1
                print(f"cog {filename} reload, {curr}/{total}")

        print("-----------------------" + Style.RESET_ALL)

# load cogs

cogsLoad(bot)

# events

@bot.event
async def on_disconnect():
    print(Fore.RED +  "-----------------------\nbot disconnected or connection failed\n-----------------------" + Style.RESET_ALL)


@bot.event
async def on_ready():
    
    print(Fore.CYAN + f"Starting as {bot.user} (ID: {bot.user.id})")
    print("-----------------------" + Style.RESET_ALL)
    print(Fore.GREEN + "Started!")
    print("-----------------------" + Style.RESET_ALL)


    await bot.change_presence(status=disnake.Status.idle, activity=disnake.Activity(type=disnake.ActivityType.streaming, name=f"persifox.space"))
    

    print(Fore.LIGHTCYAN_EX + "Waiting for input")
    print("-----------------------" + Style.RESET_ALL)

    # input

    while True:
        read = input(">")

        if read == "cogsreload":
            cogsReload(bot)

        elif read == "help":
            print(Fore.GREEN + "cogsreload - reload all cogs\nstop - disconnecting bot and close session\ninfo - get info from discord\nreload - reload connection\nswitch - switch token" + Style.RESET_ALL)

        elif read == "stop":
            print(Fore.YELLOW + "disconnecting..." + Style.RESET_ALL)
            await bot.close()
            break

        elif read == "reload":
            print(Fore.YELLOW + "reloading..." + Style.RESET_ALL)
            bot.clear()
            print(Fore.GREEN + "done" + Style.RESET_ALL)
            
        elif read == "switch":
            await bot.start(token=input(Fore.CYAN + "token\n" + Style.RESET_ALL + ">>>"))
            break

        elif read == "info":
            print(Fore.GREEN + f"""
            bot name: {bot.user}  | id: {bot.user.id}
            owner:    {bot.owner} | id: {bot.owner_id}
            status:   {bot.status}
            limit:    {bot.session_start_limit.reset_time}
            ============================================
            guilds:   {len(bot.guilds)}
            users:    {len(bot.users)}
            emojis:   {len(bot.emojis)}
            stickers: {len(bot.stickers)}
            ----------------
            {datetime.datetime.now().strftime("%d-%m-%Y %H:%M")}
            """ + Style.RESET_ALL)
        
        else:
            print(Fore.YELLOW + "unknow command. Type 'help' for get info about commands" + Style.RESET_ALL)



bot.run(getenv("TOKEN"))

