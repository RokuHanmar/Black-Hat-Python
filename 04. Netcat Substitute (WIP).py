# Import libraries
import socket
import sys
import threading
import getopt
import subprocess

# Define global variables
listen = False
command = False
upload = False
execute = ""
target = ""
upload_destination = ""
port = 0

# Usage function explains how important commands are to be used, and is called if they fail to run
def usage():
    print("BHP Net Tool")
    
    print("Usage: bhpnet.py -t target_host -p port")
    print(" -l --listen    - listen on [host]:[port] for incoming connections")
    print(" -e --execute=file_to_run    - execute the given file upon receiving a connection")
    print(" -c --command    - initialise a command shell")
    print(" -u --upload=destination - upon receiving connection upload a file and write to [destination]")
    
    
    print("Examples: ")
    print("bhpnet.py -t 192.168.0.1 -p 5555 -l -c")
    print("bhpnet.py -t 192.168.0.1 -p 5555 -l -u=c:\\target.exe")
    print("bhpnet.py -t 192.168.0.1 -p 5555 -l -e=\"cat /etc.passwd\"")
    print("echo 'ABCDEFGHI' | ./bhpnet.py -t 192.168.11.12 -p 135")
    sys.exit(0)
    
def main():
    global listen
    global port
    global execute
    global command
    global upload_destination
    global target
    
    if not len(sys.argv[1:]):
        usage()
    
    # read commandline options
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hle:t:p:cu:",
        ["help", "listen", "execute", "target", "port", "command", "upload",])
    except getopt.GetoptError as err:
        print(str(err))
        usage()
