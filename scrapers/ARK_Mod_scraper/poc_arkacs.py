import re
import time
from urllib.request import urlopen
from html import unescape

# Grab cheat commands from steam URL
#
#url = "https://steamcommunity.com/workshop/filedetails/discussion/1967741708/1744516107488290239/"
#url = "https://steamcommunity.com/workshop/filedetails/discussion/1295978823/1699416432427273146"

url = input ("Enter URL of page with spawn commands: ")
print ("URL Provided:", (url))
print ("Collecting commands")
time.sleep(5)

page = urlopen(url)
html = page.read().decode("UTF-8")

# Grab the title from the URL and parse for name.
#
pattern_title = ":\s.*\s:"
#pattern_title = "<title.*?>.*?</title.*?>"
#Sample Match: <title>Steam Community :: Lethals Reusables :: Discussions</title>
#
match_results = re.search(pattern_title, html, re.IGNORECASE)
title = match_results.group()
title = re.sub(r'^\s*(:\s*)?|(\s*:)?\s*$', '', title) # Remove begining and end charachters
title = unescape(title)
print ("Title:", (title))

# Parse the name from the command string.
#
pattern_name = "\s*blueprint\'.*?\/.*?\/.*?\/.*?\/.*?\'*\s\d\s\d\s\d"
# Sample Match: Blueprint'/Game/Mods/LethalReusable/BloodExtractor_LR.BloodExtractor_LR'" 1 0 0
#
match_results = re.search(pattern_name, html, re.IGNORECASE)
name = match_results.group()
name = unescape(name)
name = re.sub(r'^\S*(\.)|(\'\")?\s\d\s\d\s\d*$', '', name) # Remove begining and end charachters
print("Item Name:", (name))

# Parse the command sfrom the steam URL
pattern_command = "cheat\sgive.*?\s\d\s\d\s\d"
# Sample Match: <div class="bb_table_td">cheat giveitem "Blueprint'/Game/Mods/LethalReusable/BloodExtractor_LR.BloodExtractor_LR'" 1 0 0</div>
#
match_results = re.search(pattern_command, html, re.IGNORECASE)
command = match_results.group()
command = re.sub("<.*?>", "", command) # Remove HTML tags
command = unescape(command)
print("Item Spawn Command:", (command))

# Produce a working command line to add to the Ark CMDR custom commands csv list.
# Expected output (no spaces)
# Description, Group, Command, HotKey, HotKeyCode
#
HotKey = ""
HotKeyCode = ""
#
# Sample Syntax: LR Nightvision Goggles,LR Reusables,cheat giveitem "Blueprint'/Game/Mods/LethalReusable/NightVisionGoggles_LR.NightVisionGoggles_LR'" 1 65 0,,
# print ("LR Nightvision Goggles,LR Reusables,cheat giveitem \"Blueprint\'/Game/Mods/LethalReusable/NightVisionGoggles_LR.NightVisionGoggles_LR\'\" 1 65 0,,")
# print ("Description, Group, Command, HotKey, HotKeyCode")
print (name,title,command,HotKey,HotKeyCode,sep=",")
