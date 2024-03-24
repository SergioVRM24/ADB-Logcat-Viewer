import subprocess
from colorama import init, Fore, Style
import json

init()

with open('huawei.json') as json_file:
    filters_dict = json.load(json_file)

command = ["adb", "logcat"]
process = subprocess.Popen(command, stdout = subprocess.PIPE, stderr = subprocess.STDOUT, text = True, bufsize = 1)
for line in process.stdout:
    for payload in filters_dict:
        if line.lower().count(payload) > 0:
            print(filters_dict[payload] + line.strip())

print(Style.RESET_ALL)