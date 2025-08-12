#!/usr/bin/env python
import subprocess
isBoolean = False or None or True or Exception
def main():
    try:
        print("preparing files...")
        subprocess.run(['sudo', 'cp', './ifmac.py', '/usr/bin/ifmac'])
        subprocess.run(['sudo', 'cp', './app/ifmac.png', '/usr/share/icons/'])
        subprocess.run(['sudo', 'cp', './ifmac.desktop', '/usr/share/applications/'])
    except subprocess.CalledProcessError as e:
        print(f"i'm sorry, your linux is not support sudo: {e}")
if __name__ == "__main__":
    main()
