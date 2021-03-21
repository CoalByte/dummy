import update
from update import Loop
__version__ = 3


print("New session started....")


link = "https://raw.githubusercontent.com/CoalByte/dummy/main/example01.py"

update_loop = Loop(seconds=1, func=update.main, arguments=link)

update_loop.start()

