#!/bin/python3
#@mix $match
#!pod!#
# 2025-07-05  Jesus Quijada  <jesusquijada@jesusquijada-3000-N200>

import random
import subprocess
import os
import sys
# 🎨 ANSI Krayola

g = '\033[92m'
r = '\033[91m'
b = '\033[94m'
y = '\033[93m'
m = '\033[95m'
re = '\033[0m'
banu = f"{r}[ ifMacAddressChanger ]{b} ! "

platform = sys.platform
osname = os.name

linux = f"{banu}{r}starring in a {platform}/{osname} env..."
win = f"{banu}{r}win/{osname} detected, in other case launch 'tmac'"
android = f"{banu}{r}jelly/{osname} detected, use a third-party apks's"
unknown = f"{banu}{r}{platform}/{osname} no improved, please send a trouble to t.me/JesusQuijada34"
def main():
    if platform.startswith("win"):
        print(win)
    elif platform.startswith("linux"):
        print(linux)
        show_profiles()
        profile = input(f"{b}============================================================\n{banu}{m}profile name to mask/unmask mac? : {re}").strip()
        newmac = hexmac()
        print(f"{banu}{g}generated : {newmac}")
        changemac(profile, newmac)
    elif platform.startswith("android"):
        print(android)
    else:
        print(unknown)
def hexmac():
    # allows starring with a hexa.02 for warranty simplify and speed-up powers
    mac = ['02']
    for _ in range(5):
        mac.append(format(random.randint(0x00, 0xFF), '02X'))
    return ':'.join(mac)
def show_profiles():
    print(f"{banu}{g}profile available for mask/unmask:\n{b}============================================================{re}")
    subprocess.run(['sudo', 'ip', 'link'])
def changemac(profile, newmac):
    print(f"{banu}{y}changing mac on '{profile}' profile with a mask '{newmac}'...")
    try:
        print(f"{b}============================================================\n{banu}{r}power off profile '{profile}'...")
        subprocess.run(['sudo', 'ip', 'link', 'set', profile, 'down'], check=True)
        print(f"{banu}{r}face mask is already running...")
        subprocess.run(['sudo', 'ip', 'link', 'set', profile, 'address', newmac], check=True)
        print(f"{banu}{r}power on profile '{profile}'...\n{b}============================================================")
        subprocess.run(['sudo', 'ip', 'link', 'set', profile, 'up'], check=True)
        print(f"{banu}{g}success: mac changed with a mask of '{newmac}' above '{profile}' profile{re}")
    except subprocess.CalledProcessError as e:
        print(f"{banu}{r}a error unexpected in facemask plug: {e}{re}")

if __name__ == "__main__":
    main()

