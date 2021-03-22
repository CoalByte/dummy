from discord.ext import commands
import update
from update import Loop
import asyncio
__version__ = 4

TOKEN = open("token.txt", "r").read()
link = "https://raw.githubusercontent.com/CoalByte/dummy/main/discord01.py"


def shutdown():
    async def internal():
        await bot.logout()
    asyncio.run(internal())


def upd(arg):
    update.main(source=arg, filename="bot.py", pre_boot=shutdown)
    
    
update_loop = Loop(seconds=10, func=upd, arguments=link)
bot = commands.Bot(command_prefix="!!")


print(f"New session started.... (v{__version__})")


@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello, World! I updated this again! {str(__version__)}")


update_loop.start()
bot.run(TOKEN)
