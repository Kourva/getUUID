#!/usr/bin/env python3


# Get both version1 or version4 UUID from https://www.uuidgenerator.net
# GitHub: https://github.com/kozyol/getUUID


# Imports
import requests, sys, bs4


# Gets version 1 UUID
def get_version1():
    response = requests.get("https://www.uuidgenerator.net/version1")
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    temp = soup.find(id="generated-uuid").text
    return temp


# Gets version 4 UUID
def get_version4():
    response = requests.get("https://www.uuidgenerator.net/version4")
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    temp = soup.find(id="generated-uuid").text
    return temp


# Takes arguments
arguments = sys.argv


# Help message
help_message = """
Help: python getUUID.py [[-h] [-v1] [-v4]]
    -h  : Show this message and exit.
    -v1 : get version 1 UUID
    -v4 : get version 4 UUID

* What is a Version 1 UUID?
    A Version 1 UUID is a universally unique identifier that 
    is generated using a timestamp and the MAC address of 
    the computer on which it was generated.

* What is a version 4 UUID?
    A Version 4 UUID is a universally unique identifier that 
    is generated using random numbers.using a secure random 
    number generator.
"""


# Run the program
if __name__ == "__main__":
    if "-h" in arguments:
        print(help_message)
        sys.exit()

    if "-v1" in arguments:
        print(f"Version1 UUID: \033[2;32m{get_version1()}\033[m")

    if "-v4" in arguments:
        print(f"Version4 UUID: \033[2;32m{get_version4()}\033[m")

    if len(sys.argv) == 1:
        print("\033[2;31mError: no argument found! Use -h\033[m")

# EOF
