from colorama import Fore
import json

filename = "huawei.json"

filter_dict = dict()
filter_dict["power"] = Fore.RED
filter_dict["time"] = Fore.GREEN
filter_dict["clock"] = Fore.BLUE
filter_dict["huawei"] = Fore.WHITE
filter_dict["start"] = Fore.CYAN

json_string = json.dumps(filter_dict, indent = 4)
with open(filename, 'w') as json_file:
    json_file.write(json_string)