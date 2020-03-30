import discord
from discord.ext import commands
import json 
import subprocess
from colorama import Fore, Back, Style
#import RPi.GPIO as GPIO 

bot = commands.Bot(command_prefix='!')

def init():
    try : 
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(22, GPIO.OUT, initial=GPIO.HIGH)
        GPIO.setup(26, GPIO.OUT, initial=GPIO.HIGH)
        GPIO.setup(27, GPIO.OUT, initial=GPIO.HIGH)
        GPIO.setup(17, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setwarnings(False)
    except : print(Fore.RED + "error loading gpios " + Fore.RESET )

    with open("/home/pi/github/pythondiscordbot/settings.json", "r") as complex_data:
        data = complex_data.read()
        settings = json.loads(data)
    return settings 
        
extensions = ['cogs.bash', 
              'cogs.reload',
              'cogs.blink']


settings = init()

if __name__ == '__main__':
    for ext in extensions:
        print(ext)
        bot.load_extension(ext)
     
@bot.event
async def on_ready():
    print(Fore.GREEN + 'Logged in as '+ Fore.RESET + bot.user.name)


bot.run(settings['token'])  