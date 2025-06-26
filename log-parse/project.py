import os
import sys
platform = sys.platform
#Get current working directory
os.chdir('../../../../../../var/log')
cwd = os.getcwd()
try:
    with open('system.log', 'r') as log_file:
        for line in log_file:
            print(line.strip())
            if 'dead_process'.upper() in line:
                print("Found 'dead_process' in log file.")
except FileNotFoundError:
    print("Error: 'application.log' not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
