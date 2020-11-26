# HowToCogs

Okay, so welcome to this tutorial of cogs 

Cogs are a great way to have different scripts running the bot, they also allow you to have less lines in your main script .

So today im going to tell you how to do this!

So first you need your main script.
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

So thats your script.
Create a folder named "cogs", case sensitive.

Once you're done with that, now you can create an extension.
To create a cog, first you need to create your extension.

for this example im going to call it moderation.py.
You can call it whatever you want.

After you have created your file, you need to create the cog itself.
So this is what the extension (moderation.py) is going to look like inside

```py
import discord
from discord.ext import commands

class Moderation(commands.Cog):
    """optional description to show on the help command. Remove this line for no description."""
    def __init__(self, bot):
        self.bot = bot
```

After you have done that step you can start coding.
Unlike in the main script, all of your commands need to have an indent (tab/4 spaces).
Commands in cogs, unlike in your main script, use `@commands.command(...)` instead of `@bot.command(...)`.
They, like all other functions in a `class`, require `self` as the first argument (and `ctx` as the second argument).

So this is going to be my example command in the cog (moderation.py)

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

Once you have all of your desired commands in the cog, now you need to define your setup function.
So this is how you do that:

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

Make sure `def setup(bot):` is **not indented into your class**.

Now you can save and close the extension (or leave it open, just at least save it)

Now go to your main file and you are going to load an extension.
If you decide to load other extensions (Jishaku for example), as long as its all formated properly, your cogs should work.

So go to your main file (bot.py), and now my file will look like this

```py
import discord
import datetime
import traceback
from discord.ext import commands
bot = commands.Bot(command_prefix=commands.when_mentioned_or('b!'), case_insensitive=True)
TOKEN = "bottokenhere"

@bot.event  # The event for the bot
async def on_ready():  # Defines what to do when the event/command is used/called
    print(f"I am online! {bot.user.name}")  # Prints to the console that the bot is online

try:
    bot.load_extension("cogs.moderation")  # Instead of a file-like or path-like string, you put `directory.file`, without a file extension.
except:
    print("Failed to load moderation:")
    traceback.print_exc()

bot.run(TOKEN)  # Will run the token
```

If you have bot defined as client, then you just change the bot sections to client.
