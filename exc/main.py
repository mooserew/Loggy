import pyfiglet
import sys

ascii_header = pyfiglet.figlet_format("Loggy", font="slant")
print(ascii_header)
 
try:
    while True:
        inp = input("Welcome to Loggy, to show a list of available commands type -help: ")
        if inp == "-help":
            print("-portscan: look for open ports\n-wifiscan: scan every device connected to your network")
        elif inp == "-portscan":
            import portscanner  # You might want to handle this import better
        elif inp =="-wifiscan":
            import wifiscanner
        else:
            print("Invalid command. Type -help to see available commands.")
except KeyboardInterrupt:
    print("\nCancelled by user. Exiting...")

