<h1>⚙️ Microsoft Windows Firewall Automation Rules</h1>

<h2>Description:</h2>

- <b>Automate updating of Windows Firewall rules via Python</b> 
- <b>List of IP addresses will be obtained via a csv file</b>


<h2>Languages and Utilities Used:</h2>

- <b>Microsoft Windows Defender Firewall</b>
- <b>Python via Visual Code Studio</b>
- <b>Windows PowerShell


<h2>Environments Used: </h2>

- <b>Windows 11</b> (22H2)

<h2>Resources Used: </h2>
https://feodotracker.abuse.ch/



<h2>Program walk-through:</h2>

<p align="center">
 <b> Check out Part 1 Here: https://github.com/kevinnyeo/MicrosoftWindowsDefenderFirewall</b><br/>
<p align="center">
 <b>As seen in Part 1, Windows Defender Firewall rules requires you to paste in a list of IP addresses to block. This can be automated via running a Python script.</b>  <br/>
 <img src="https://i.imgur.com/bTv8qdA.png" height="80%" width="80%" />
<p align="center">
 We will be getting a list of malicious IP addresses from https://feodotracker.abuse.ch/blocklist/
 <img src="https://i.imgur.com/Ekozmys.png" height="80%" width="80%" />
 <img src="https://i.imgur.com/nhbC3lG.png" height="80%" width="80%" />
 <br />
<p align="center">
 Script used in Python via Visual Studio Code <br/>
 <img src="https://i.imgur.com/xamcUUd.png" height="80%" width="80%" />

<b> This script fetches an IP blocklist CSV from https://feodotracker.abuse.ch/blocklist, processes the CSV data to extract IP addresses, deletes an existing firewall rule named 'BadIP', and then 
 adds new firewall rules to block the extracted IP addresses both for outbound and inbound traffic. The script makes use of the requests, csv, and subprocess modules to achieve these tasks. </b><br/>
<p align="center">
 Importing Required Modules:<br/>
  
 import requests: This module allows the script to make HTTP requests to fetch data from a URL.<br/>
 import csv: This module provides functionality to read and write CSV (Comma-Separated Values) files.<br/>
 import subprocess: This module allows running shell commands from within the script.<br/>
 
<p align="center"> 
 Fetching IP Blocklist:<br/>
 
 The script attempts to fetch an IP blocklist from the specified URL: "https://feodotracker.abuse.ch/downloads/ipblocklist.csv".<br/>
 It uses the requests.get() function to retrieve the content of the URL as text.<br/>
 If the request is successful, the text content is split into individual lines using splitlines() and stored in the response_lines variable.<br/>
 If the request fails due to a network issue (requests.exceptions.RequestException), an error message is printed, and the script exits with status code 1.<br/>

<p align="center"> 
 Deleting Existing Firewall Rule:<br/>
  
 A PowerShell command netsh advfirewall firewall delete rule name='BadIP' is executed using subprocess.run() to delete an existing firewall rule named 'BadIP'.<br/>

<p align="center"> 
 Processing CSV Data and Adding Firewall Rules:<br/>
  
 The script iterates through each line of the response_lines list, which contains the content of the fetched CSV file.<br/>
 It uses a lambda function with the filter() function to exclude lines starting with # (comment lines) from being processed by the CSV reader.<br/>
 For each row (line) in the CSV data, it extracts the IP address from the second column (row[1]).<br/>
 If the IP address is not "dst_ip", it prints a message indicating that a rule is being added to block that IP.<br/>
 It constructs two PowerShell commands (rule_out and rule_in) to add outbound and inbound firewall rules to block the specified IP address using the netsh command.<br/>
 The subprocess.run() function is used to execute the PowerShell commands in the Windows Command Prompt, with the shell=True argument indicating that the command should be interpreted by the 
 shell.<br/>

<p align="center"> 
  Run Python Script via Command Prompt (Administrator) <br/>
  <img src="https://i.imgur.com/FusdCWA.png" height="80%" width="80%" />
  <img src="https://i.imgur.com/zVCJTyd.png" height="80%" width="80%" />

<p align="center"> 
  List of malicious IP addresses has been added to block list <br/>
  <img src="https://i.imgur.com/i5f2q0y.png" height="80%" width="80%" />



 
  








 





</p>

<!--
 ```diff
- text in red
+ text in green
! text in orange
# text in gray
@@ text in purple (and bold)@@
```
--!>
