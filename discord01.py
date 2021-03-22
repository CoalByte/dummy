from discord.ext import commands
import update
from update import Loop
__version__ = 1

TOKEN = open("token.txt", "r").read()
link = "https://raw.githubusercontent.com/CoalByte/dummy/main/discord01.py"
update_loop = Loop(seconds=10, func=update.main, arguments=link)
bot = commands.Bot(command_prefix="!!")


print(f"New session started.... (v{__version__})")


@bot.command()
async def hello(ctx):
    await ctx.send("Hello, World!")


update_loop.start()
bot.run(TOKEN)
