import discord
from discord.ext import commands
import subprocess
from colorama import Fore, Back, Style

class Reload(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot 

    @commands.command()
    async def reload(self, ctx, *, arg):
        try : 
            print(arg)
            self.bot.reload_extension("cogs."+arg)
        except commands.ExtensionError:
            print(Fore.RED + "[ERROR] : " + Fore.YELLOW + str(ctx.author) + Fore.RESET  + 
                " not found " + Fore.YELLOW + arg + Fore.RESET) 
            await ctx.send("error happend, extension not loaded")
        else : 
            await ctx.send("heyyy worked")


def setup(bot):
    bot.add_cog(Reload(bot))