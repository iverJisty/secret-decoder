#!/usr/bin/env python3
import base64
import sys
from io import StringIO

import yaml
import colorama
from colorama import Fore, Style

def decode_secret_and_output(secret):
    # Decode all base64-encoded strings in the 'data' section of the secret
    print("{")
    if 'data' in secret:
        num_items = len(secret['data'])
        for i, (key, value) in enumerate(secret['data'].items()):
            decoded_value = try_decode_base64(value)
            colored_key = f'{Fore.GREEN}{key}{Style.RESET_ALL}'
            colored_value = f'{Fore.YELLOW}{decoded_value}{Style.RESET_ALL}' 

            if i == num_items - 1:  # Last item
                print(f"\t\"{colored_key}\": \"{colored_value}\"")
            else:
                print(f"\t\"{colored_key}\": \"{colored_value}\",")

    print("}")


def try_decode_base64(encoded_string):
    try:
        decoded_bytes = base64.b64decode(encoded_string + '=' * (4 - len(encoded_string) % 4))
        return decoded_bytes.decode('utf-8')
    except UnicodeDecodeError:
        return '<binary>'


# Initialize colorama library for cross-platform coloring support on Windows and Unix systems.
colorama.init()
#just_fix_windows_console()

# Read input from stdin as YAML and parse it into a Python object
input_yaml = sys.stdin.read()
secrets_object = yaml.safe_load(input_yaml)

decode_secret_and_output(secrets_object)


colorama.deinit()
