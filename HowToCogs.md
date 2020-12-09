# HowToCogs

Okay, so welcome to this tutorial explaining how to use cogs.

Cogs are a great way to have different scripts for different command categories on the bot. They allow you to have less lines in your main script.

So today, I'm going to explain how to do this!

So first, you need to look at your main script.
Lets say this is your script so far:

```py
import discord
import datetime
from discord.ext import commands
bot = commands.Bot(command_prefix=commands.when_mentioned_or('b!'), case_insensitive=True)
TOKEN = "bottokenhere"


@bot.event
async def on_ready():
    print(f"I am online!  {bot.user.name}")

bot.run(TOKEN)
```

So that's your script.
Now, create a folder named "cogs" (all lowercase, it is case-sensitive).

Once you're done with that, it's time to create your first cog!
To create a cog, first you need to create your file.

For this example, I'm going to use ```moderation.py```
You can call it whatever you want, but it does need to have the ```.py``` extension at the end to work properly.

After you have created your file, you need to create the ```class``` portion of the cog.
So now the cog file (```moderation.py``` in this case) should look something like this:

```py
import discord
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
```

After you have done that step, you can start coding!
Unlike in the main script, all of your commands need to be indented (tab), and then they need to have ```@commands.command()```
You also need to use ```self.bot``` instead of just ```bot``` for functions.

So this is going to be my example command in the cog (moderation.py):

```py
import discord
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def foo(self, ctx):
        await ctx.send("Foo!")
```

Once you have all of your desired commands in the cog, now you need to define your setup function that will allow it to run.
Your file should now look something like this:

```py
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
```

Your cog is now ready to be loaded!

Now you need to go back to your main file, and you are going to load an extension.
The extension is going to be how the cog works with the bot.
If you decide to load other extensions (Jishaku for example), as long as its all formatted properly, your cogs should work

So go to your main file (bot.py)
and now my file will look like this

```py
import discord
import datetime
from discord.ext import commands
bot = commands.Bot(command_prefix=commands.when_mentioned_or('b!'), case_insensitive=True)
TOKEN = "bottokenhere"

@bot.event # The event for the bot
async def on_ready(): # Defines what to do when the bot is ready
    print(f"I am online!  {bot.user.name}") # Prints to the console that the bot is online

bot.load_extension("cogs.moderation") # Tries to load the cog, if your cog has syntax errors, the bot will most likely crash.
bot.run(TOKEN) # Runs the bot with the token.
```

If you have bot defined as client, then you just change the bot sections to client.
