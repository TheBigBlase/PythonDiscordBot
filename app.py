import discord
from discord.ext import commands
import json 
import subprocess
from colorama import Fore, Back, Style

bot = commands.Bot(command_prefix='!')

def init():
    with open("./settings.json", "r") as complex_data:
        data = complex_data.read()
        settings = json.loads(data)
    return settings 

extensions = ['cogs.bash', 
              'cogs.reload']


settings = init()

if __name__ == '__main__':
    for ext in extensions:
        print(ext)
        bot.load_extension(ext)
     
@bot.event
async def on_ready():
    print(Fore.GREEN + 'Logged in as '+ Fore.RESET + bot.user.name)


bot.run(settings['token'])  