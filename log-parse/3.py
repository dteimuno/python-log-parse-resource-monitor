import os
from pathlib import Path

file_path = Path('/var/log/system.log')
lines = open(file_path, 'r').readlines()
dead_count = 0
#print first 10 lines
for line in lines[:10]:
    print(line.strip())
for line in lines:
    if 'dead_process'.upper() in line.upper():
        dead_count += 1
        print("Dead count:", dead_count)
    else:
        print("No dead process found in this line.")