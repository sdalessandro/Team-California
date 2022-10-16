import re
from collections import defaultdict

friendDict= {}

with open("userFriends.txt", "r") as friendFile:
    lines = friendFile.read().splitlines()
    for line in lines:
        key, value = line.split(' ', 1)
        friendDict[key] = value

print(friendDict)