import requests
import time
import re
import json
import os
import sys


# == SETTINGS ==

# The curl command copied from dev tools
CURL_COMMAND = os.environ['CURL_COMMAND']
GUILD_ID = os.environ['GUILD_ID']
if CURL_COMMAND is None:
    if GUILD_ID is None and len(sys.argv) > 1:
        GUILD_ID = sys.argv[1]
    if GUILD_ID is not None:
        CURL_COMMAND = "https://mee6.xyz/api/plugins/levels/leaderboard/" + GUILD_ID + "?page=0"

if CURL_COMMAND is None:
    exit(1)

# Max amount of pages to read. The program waits 1 second per page read to avoid being rate-limited
# by Mee6's servers.
MAX_PAGES = 100



# == SCRIPT START ==

headers = {}
url = ""

url = CURL_COMMAND.replace("curl '", "").split(" ")[0][:-1]
# print(url)

for part in CURL_COMMAND.split(" -H "):
    # print("> HEADER")
    if part.startswith("curl "):
        # print("nope")
        continue
    # print("part:", part)
    header_str = part[1:-1]
    # print("header_str:", header_str)
    header_parts = header_str.split(": ", 1)
    # print("header_parts", header_parts)
    headers[header_parts[0]] = header_parts[1]


data_file = open("data.txt", "w")
data_file.write("[")
first = True
for i in range(MAX_PAGES):
    print("Page:", i)
    resp = requests.get(re.sub("\\?page=[0-9]+", "?page=" + str(i), url), headers)
    json_resp = resp.json()
    json_players = json_resp["players"]
    json_players_len = len(json_players)
    print("LEN:", str(json_players_len))

    if json_players_len == 0:
        break

    if first:
        first = False
    else:
        data_file.write(",")
    # data_file.write(str(json_players).replace("'", '"'))
    data_file.write(json.dumps(json_players))

    time.sleep(1)

data_file.write("]")
data_file.close()
