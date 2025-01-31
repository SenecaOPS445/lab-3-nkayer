#!/usr/bin/env python3
'''Lab 3 - Free Disk Space Script'''


import subprocess

def free_space():
    """Returns the free disk space on the root directory."""
    try:
        
        result = subprocess.run(
            "df -h | grep '/$' | awk '{print $4}'",
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        free_space_output = result.stdout.strip()
        return free_space_output
    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    print(free_space())
