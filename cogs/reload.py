import discord
from discord.ext import commands
import subprocess
from colorama import Fore, Back, Style
import RPi.GPIO as GPIO

class Reload(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot 

    @commands.command()
    async def reload(self, ctx, *, arg):
        try : 
            self.bot.reload_extension("cogs."+arg)
            GPIO.cleanup()
        except commands.ExtensionError:
            print(Fore.RED + "[ERROR] : " + Fore.YELLOW + str(ctx.author) + Fore.RESET  + 
                " not found " + Fore.YELLOW + arg + Fore.RESET) 
            await ctx.send("error happend, extension not loaded")
        except : 
            print(Fore.RED + "error cleaning gpios" + Fore.RESET )
        else : 
            await ctx.send("heyyy worked")
            print(Fore.GREEN + "[RELOAD] " + Fore.GREEN + arg + Fore.RESET + " Sucess, suckless") 


def setup(bot):
    bot.add_cog(Reload(bot))
