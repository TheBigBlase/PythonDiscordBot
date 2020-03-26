import discord
from discord.ext import commands
import subprocess
from colorama import Fore, Back, Style

class Bash(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 

    @commands.command()
    async def bash(self, ctx, *args):
        """run a bash command"""
        if ctx.author == self.bot : return 
        tab = [] 
        message = " ".join(args)
        for string in args:
            tab.append(string)
        print("tab = ", [*tab])

        p = subprocess.Popen(message, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
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
            await ctx.send("```" + message + "```"+ "\nnoice")
            

def setup(bot):
    bot.add_cog(Bash(bot))