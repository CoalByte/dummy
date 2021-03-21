import platform

print(True if platform.platform().startswith("W") else False)
