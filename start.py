import sys
import requests
import os
from dotenv import load_dotenv

load_dotenv()
day = int(sys.argv[1])
path = f"./{day}/{day}"

USER_AGENT = "https://github.com/adit-bala/AOC-2022 by @adit-bala on Github"
URL = f"https://adventofcode.com/2022/day/{day}/input"
cookie = os.getenv('COOKIE')

# create folder for day
if not os.path.exists(f"./{day}"):
    os.makedirs(f"./{day}")

# attempt to fetch inputs
if not os.path.exists(f"{path}.txt"):
    try:
        with requests.get(url=URL, cookies={"session": cookie}, headers={"User-Agent": USER_AGENT}) as response:
            if response.ok:
                if response.ok:
                    data = response.text
                    input = open(f"{path}.txt", "w+")
                    input.write(data.rstrip("\n"))
                    input.close()
                else:
                    print("Server response sus")
    except Exception as e:
        print("something went wrong lol")

# try to set up code
if not os.path.exists(f"{path}.py"):
    code = open(f"{path}.py", "w+")
    code.write(f"with open((__file__.rstrip(\"{day}.py\")+\"{day}test.txt\"), 'r') as input_file:\n input = input_file.read()\n\n\n\nprint(\"Part One : \"+ str(None))\n\n\n\nprint(\"Part Two : \"+ str(None))"
    ) 
    code.close()

# try to set up test
if not os.path.exists(f"{path}test.txt"):
    test = open(f"{path}test.txt", "w+")
    test.close()


