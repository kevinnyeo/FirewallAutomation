import requests
import csv
import subprocess

try:
    response = requests.get("https://feodotracker.abuse.ch/downloads/ipblocklist.csv").text
    response_lines = response.splitlines()
except requests.exceptions.RequestException as e:
    print("Error fetching IP blocklist:", e)
    exit(1)

rule_delete = 'netsh advfirewall firewall delete rule name=BadIP'
subprocess.run(['powershell', '-Command', rule_delete], shell=True)

mycsv = csv.reader(filter(lambda x: not x.startswith('#'), response_lines))
next(mycsv)  # Skip the header row

for row in mycsv:
    if len(row) >= 2:
        ip = row[1]
        if ip != 'dst_ip':
            print("Added rule to block:", ip)

            rule_out = f'netsh advfirewall firewall add rule name=BadIP Dir=Out Action=Block RemoteIP={ip}'
            subprocess.run(['powershell', '-Command', rule_out], shell=True)

            rule_in = f'netsh advfirewall firewall add rule name=BadIP Dir=In Action=Block RemoteIP={ip}'
            subprocess.run(['powershell', '-Command', rule_in], shell=True)
    else:
        print("Invalid row length:", row)