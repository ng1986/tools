#!/usr/bin/python3

import sqlite3
import argparse

def show():
    con = sqlite3.connect('hardware.db')
    cur = con.cursor()
    for row in cur.execute('SELECT * FROM INTERFACES'):
        print(row)
    con.close()

def showmac(mac):
    con = sqlite3.connect('hardware.db')
    cur = con.cursor()
    for row in cur.execute("SELECT * FROM INTERFACES WHERE mac LIKE ?", (mac,)):
        print(row)
    con.close()

def insert(hostname, mac, ip):
    con = sqlite3.connect('hardware.db')
    con.execute("INSERT INTO INTERFACES (HOSTNAME, MAC, IP) VALUES (?,?,?)",(hostname,mac,ip))
    con.commit()
    con.close()

parser = argparse.ArgumentParser()
parser.add_argument('--show', action='store_true')
parser.add_argument('--add', action='store_true')
parser.add_argument('--dhcp', action='store_true')
parser.add_argument('--mac')
parser.add_argument('--ip')
parser.add_argument('--hostname')
args = parser.parse_args()

if(args.show):
    if(args.mac):
        showmac(args.mac)
    else:
        show()

if(args.add):
    print("Datensatz hinzufügen!")
    print("MAC Adresse:")
    print(args.mac)
    print("Hostname:")
    print(args.hostname)
    print("IP:")
    if(args.dhcp):
        print("0.0.0.0")
    else:
        print(args.ip)
    insert(args.hostname,args.mac,args.ip)
