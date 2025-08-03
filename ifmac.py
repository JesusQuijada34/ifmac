#!/usr/bin/python
#@mix $match
#!pod!#
# 2025-07-05  Jesus Quijada  <jesusquijada@jesusquijada-3000-N200>

import random
import subprocess
import os
import sys
# 🎨 Colores ANSI

VERDE = '\033[92m'
ROJO = '\033[91m'
AZUL = '\033[94m'
AMARILLO = '\033[93m'
MAGENTA = '\033[95m'
RESET = '\033[0m'

plataforma = sys.platform

ifmaclinux = f"""{VERDE}╔═=═ MAC ADDRESS CHANGER ═=════════════════════════=═ - + x ═=═
║ Contribuye al proyecto en {ROJO}GitHub:{AZUL}
║ https://github.com/jesusquijada34/imac/{VERDE}
╚══════════════════════════════════════════════════════════════"""
ifmacwin = f"""{ROJO}╔═=═ MAC ADDRESS CHANGER ═=════════════════════════=═ - + x ═=═
║ Ups!, tu Windows no es compatible con este paquete
║ Puedes usar TMAC.exe y personalizar tu MAC Address, gracias!.
╚══════════════════════════════════════════════════════════════"""
ifmacandroid = f"""{ROJO}╔═=═ MAC ADDRESS CHANGER ═=════════════════════════=═ - + x ═=═
║ Ups!, Android no es soportable con este paquete influent
║ Puedes usar programas de terceros para disfrazar tu MAC!.
╚══════════════════════════════════════════════════════════════"""
ifmacunknown = f"""{ROJO}╔═=═ MAC ADDRESS CHANGER ═=════════════════════════=═ - + x ═=═
║ Ups!, Jesus Quijada no hace paquetes para {plataforma}
║ Soporte y Mantenimiento al Telegram: t.me/@JesusQuijada34.
╚══════════════════════════════════════════════════════════════"""
def banner():
    if plataforma.startswith("win"):
        print(ifmacwin)
    elif plataforma.startswith("linux"):
        print(ifmaclinux)
        mostrar_interfaces()
        interfaz = input(f"{MAGENTA}[🔧] Ingresa la interfaz a modificar: {RESET}").strip()
        nueva_mac = generar_mac_con_02()
        print(f"{AZUL}[🎲] MAC aleatoria generada: {VERDE}{nueva_mac}{RESET}")
        cambiar_mac(interfaz, nueva_mac)
    elif plataforma.startswith("android"):
        print(ifmacandroid)
    else:
        print(ifmacunknown)

def generar_mac_con_02():
    # Siempre inicia con 02 para garantizar unicidad y validez
    mac = ['02']
    for _ in range(5):
        mac.append(format(random.randint(0x00, 0xFF), '02X'))
    return ':'.join(mac)

def mostrar_interfaces():
    print(f"""{AZUL}══════════════════════════════════════════════════════════════
 🌐 Interfaces de red disponibles:
Para saber cual es la interfaz de red activa que quieres
cambiarle la MAC, debes de asegurarte que tenga el prefijo de
<UP>. Las interfaces que tienen el prefijo de <DOWN>, no van a
hacer efecto en la interfaz encendida. Estoy ejecutando
    {ROJO}ip link...{AZUL} Coloca las credenciales indicadas!
══════════════════════════════════════════════════════════════""")
    subprocess.run(['sudo', 'ip', 'link'])
def cambiar_mac(interfaz, nueva_mac):
    print(f"{AMARILLO}[🔄] Cambiando la MAC de {interfaz} a {nueva_mac}...{RESET}")
    try:
        subprocess.run(['sudo', 'ip', 'link', 'set', interfaz, 'down'], check=True)
        subprocess.run(['sudo', 'ip', 'link', 'set', interfaz, 'address', nueva_mac], check=True)
        subprocess.run(['sudo', 'ip', 'link', 'set', interfaz, 'up'], check=True)
        print(f"{VERDE}[✅] Éxito: MAC cambiada a {nueva_mac} en {interfaz}{RESET}")
    except subprocess.CalledProcessError as e:
        print(f"{ROJO}[❌] Error al cambiar la MAC: {e}{RESET}")

if __name__ == "__main__":
    banner()
    
