#HowToCogs

#Okay, so welcome to this tutorial of cogs 

#Cogs is a great way so you can have different scripts running the bot, they also allow you to have less lines in your main script 

#So today im going to tell you how to do this!

#So first you need your main script
#Lets say this is your script so far

import discord
import datetime
from discord.ext import commands
bot = commands.Bot(command_prefix=commands.when_mentioned_or('b!'), case_insensitive=True)
TOKEN = "bottokenhere"


@bot.event
async def on_ready():
    print(f"I am online!  {bot.user.name}")

bot.run(TOKEN)


#So thats your script
#Create a folder named "cogs", and it will be caps sensitive

#Once your done with that, now you can create a cog
#To create a cog, first you need to create your file

#for this example im going to call it moderation.py
#You can call it whatever you want, but it does need to have the .py extension at the end

#After you have created your file, you need to create the class portion of the cog
#So this is what the cog file (moderation.py) is going to look like

import discord
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

#After you have done that step you can start coding
#Unlike in the main script, all of your commands need to have an indent (tab), and then they need to have @commands.command
#and they need (self)

#So this is going to be my example command in the cog (moderation.py)

import discord
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def foo(self, ctx):
        await ctx.send("Foo!")

#Once you have all of your desired commands in the cog, now you need to define your setup function
#So this is how you do that

import discord
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def foo(self, ctx):
        await ctx.send("Foo!")
        
def setup(bot):
    bot.add_cog(Moderation(bot))

#Now you can save and close the cog file (or leave it open, just at least save it)

#Now go to your main file and you are going to load an extension
#The extension is going to be how the cog works with the bot
#If you decide to load other extensions (Jishaku for example), as long as its all formated properly, your cogs should work

#So go to your main file (bot.py)
#and now my file will look like this

import discord
import datetime
from discord.ext import commands
bot = commands.Bot(command_prefix=commands.when_mentioned_or('b!'), case_insensitive=True)
TOKEN = "bottokenhere"

@bot.event#The event for the bot
async def on_ready():#Defines what to do when the event/command is used/called
    print(f"I am online!  {bot.user.name}")#Prints to the console that the bot is online

bot.load_extension("cogs.moderation")#Will load the cog, if your cog has script errors, the bot most likley will not run
bot.run(TOKEN)#Will run the token

#If you have bot defined as client, then you just change the bot sections to client

#Please do not try to host this script or anything, I am not responsible for servers/computers being wrecked becasue
#This script will not be able to do that.