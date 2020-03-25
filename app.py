import discord
from discord.ext import commands
import json 
import os
import subprocess
from colorama import Fore, Back, Style

bot = commands.Bot(command_prefix='!')

def init():
    with open("./settings.json", "r") as complex_data:
        data = complex_data.read()
        settings = json.loads(data)
    return settings 


settings = init()


@bot.event
async def on_ready():
    print(Fore.GREEN + 'Logged in as '+ Fore.RESET + bot.user.name)


@bot.command()
async def bash(ctx, *args):
    """run a bash command"""
    if ctx.author == bot : return 
    tab = [] 
    k = 0
    message = ""
    for string in args:
        tab.append(string)
        k = k+1
    

    p = subprocess.Popen([*tab], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    message, err = p.communicate()
    if p.returncode != 0: 
        err = str(err)
        err = err.replace(str("\\n"), "\n")
        err = err[2:len(err)-1]
        print(Fore.RED + "[ERROR] : " + Fore.YELLOW + str(ctx.author) + Fore.RESET  +
            " requested  " + Fore.YELLOW + str(" ".join(args))+ Fore.LIGHTRED_EX + " : error :" + Fore.RED + err + Fore.RESET) 
        await ctx.send("```" + err + "```")

    else :
        message = str(message)
        message = message.replace(str("\\n"), "\n")
        message = message[2:len(message)-1]
        print(Fore.LIGHTMAGENTA_EX + str(ctx.author) + Fore.RESET  + " requested " + Fore.BLUE + str(" ".join(args)) + Fore.RESET)
        await ctx.send("```" + message + "```")
    
bot.run(settings['token'])  