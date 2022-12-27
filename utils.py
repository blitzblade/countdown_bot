import json
import sys
from logger_tool import Logger


def load_config(file="config.json"):
    return json.load(open(file))


def save_config(data: dict, file: str):
    with open(file, "w") as f:
        json.dump(data, f)


def print_err(err):
    output = str(err) + " on line " + str(sys.exc_info()[2].tb_lineno)
    Logger.fatal(output)
