import discord
from discord.ext import commands
import subprocess
from colorama import Fore
import RPi.GPIO as GPIO 
from asyncio import sleep 


class Blink(commands.Cog):
    def __init__(self, bot):
        GPIO.setwarnings(False)
        self.bot = bot
        self.blinkMax = 75
        self.currentPWM = 0
        self.direction = True 
        self.stop = False
        GPIO.setmode(GPIO.BCM) 
        GPIO.setup(19, GPIO.OUT)
        GPIO.setup(26, GPIO.OUT)
        self.red = GPIO.PWM(19, 100)
        self.green = GPIO.PWM(26, 100)
        self.green.start(0)
        self.red.start(0)
        self.blinkSpeed = 1
    
    @commands.command()
    async def blink(self, ctx, *arg):

 
        if len(arg) !=0 and arg[0] == "stop".lower():
            self.stop = True
            await ctx.send("stopped")
            print(Fore.CYAN + "[BLINK] " + Fore.RESET + "stopped")
            self.green.stop()
            self.red.stop()


        else: 
            self.stop = False
            await ctx.send("Turning green leds on")
            print(Fore.CYAN + "[BLINK] " + Fore.RESET + "Turning leds on") 
            while self.stop == False :
                if self.direction == True :
                    self.currentPWM+=self.blinkSpeed
                else : 
                    self.currentPWM-=self.blinkSpeed
                if self.currentPWM == self.blinkMax:
                    self.direction = False
                elif self.currentPWM == 0:
                    self.direction = True 
                self.red.ChangeDutyCycle(self.currentPWM)
                self.green.ChangeDutyCycle(self.currentPWM)
                await sleep(0.05)                
 


def setup(bot):
    bot.add_cog(Blink(bot))
    
