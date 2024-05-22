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

