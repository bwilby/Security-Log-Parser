# Security-Log-Parser
This is a python script that parses SSH user authentication logs to detect failed login attempts and outputs the results to the screen.
Brute force SSH attacks are one of the most common attack vectors in real life environments. This script automates the detection process that some SOC Analysts do manually. 
## What it does
- Parses log files for failed SSH login attempts
- Groups failed attempts by their IP addresses
- Flags the IPs that have multiple attempts as brute force attempts
- Reports the total failed login attempts

## How it works
- Import auth.log file
```bash
python log_parser.py
```
## Sample Output
```=== Failed Login Report ===
IP: 192.168.1.100 | Attempts: 3 | Usernames tried: {'admin'}
IP: 192.168.1.105 | Attempts: 3 | Usernames tried: {'root'}
IP: 192.168.1.200 | Attempts: 1 | Usernames tried: {'admin'}

=== Brute Force Alerts ===
ALERT: Possible brute force from 192.168.1.100 - 3 attempts
ALERT: Possible brute force from 192.168.1.105 - 3 attempts
Total Failed login attempts: 7
```
