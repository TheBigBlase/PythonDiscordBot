import discord
from discord.ext import commands
import subprocess
from colorama import Fore, Back, Style
#import RPi.GPIO as GPIO 

class Blink(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.blinkMax = 50
        self.currentPWM = 0
        self.direction = True 
        self.stop = False 
        self.pwmGreen = []
        self.pwmRed = []

    @commands.command()
    async def blink(self, ctx, *arg):
        if len(arg) !=1:
            return await ctx.send("wrong number of arguments bro")
        elif arg[0] == "green".lower() : 
            await ctx.send("Turning green leds on")

            while self.stop == False :
                if self.direction == True :
                    self.currentPWM=+1
                else : 
                    self.currentPWM=-1
                if self.direction == 50:
                    self.direction = False
                elif self.direction == 0:
                    self.direction = True 
                for k in range (0, len(self.pwmGreen)):
                    GPIO.PWM(self.pwmGreen[k],self.currentPWM)

    async def stopBlinking(self, ctx, *arg):
        if len(arg) !=1:
            return await ctx.send("wrong number of arguments bro")
        elif arg[0] == "stop".lower():
            self.stop == True
            await ctx.send("Should be stopped")


def setup(bot):
    bot.add_cog(Blink(bot))
    