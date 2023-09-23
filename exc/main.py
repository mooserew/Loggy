import pyfiglet
import sys

ascii_header = pyfiglet.figlet_format("Loggy")
print(ascii_header)
 
inp = input(str("Welcome to Loggy, to show a list of available commands type -help: "))

if inp == "-help":
    print("-portscan: look for open ports\n-wifiscan: scan every device connected to your network")
