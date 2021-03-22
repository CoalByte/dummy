from discord.ext import commands
import update
from update import Loop
__version__ = 2

TOKEN = open("token.txt", "r").read()
link = "https://raw.githubusercontent.com/CoalByte/dummy/main/discord01.py"


def upd(arg):
    update.main(source=arg, filename="bot.py")
    
    
update_loop = Loop(seconds=10, func=upd, arguments=link)
bot = commands.Bot(command_prefix="!!")


print(f"New session started.... (v{__version__})")


@bot.command()
async def hello(ctx):
    await ctx.send("Hello, World! I updated this!")


update_loop.start()
bot.run(TOKEN)
