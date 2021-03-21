import os
import requests
import update
import sys

link = "https://raw.githubusercontent.com/CoalByte/dummy/main/example01.py"

if sys.argv:
    update.main(url=link)
elif sys.argv[0] == "upd-done":
    print("Skipping update (auto restart previously executed)")
