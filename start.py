import sys
import requests
import os
from dotenv import load_dotenv

load_dotenv()
day = int(sys.argv[1])

USER_AGENT = "adventofcode_working_directories_creator"
URL = f"https://adventofcode.com/2022/day/{day}/input"
cookie = os.getenv('COOKIE')

# create folder for day
if not os.path.exists(f"./{day}"):
    os.makedirs(f"./{day}")

# attempt to fetch inputs
if not os.path.exists(f"./{day}/{day}.txt"):
    try:
        with requests.get(url=URL, cookies={"session": cookie}, headers={"User-Agent": USER_AGENT}) as response:
            if response.ok:
                if response.ok:
                    data = response.text
                    input = open(f"./{day}/{day}.txt", "w+")
                    input.write(data.rstrip("\n"))
                    input.close()
                else:
                    print("Server response sus")
    except Exception as e:
        print("something went wrong lol")

# try to set up code
if not os.path.exists(f"./{day}/{day}.py"):
    code = open(f"./{day}/{day}.py", "w+")
    code.write(f"\n\nwith open((__file__.rstrip(\"{day}.py\")+\"{day}.txt\"), 'r') as input_file:\n input = input_file.read()\n\n\n\nprint(\"Part One : \"+ str(None))\n\n\n\nprint(\"Part Two : \"+ str(None))"
    ) 
    code.close()

