import regular_expressions as regex
import sys
import re
text: str = "The internal network contains the following devices.\
    WEB server is running at 172.0.5.20. Database server is running at 10.0.5.20.\
        Backup is available through 172.0.5.40. Monitoring sends notifications from 85.12.30.7.\
            Whitelist for access from external network contains IP addresses from 200.13.4.1 to \
                200.13.4.100"
ip_regex= regex.ipV4AddressRe()  
devices = ["WEB Server","DB server", "Backup", "Monitoring", "Whitelist From", "Whitelist To"]
devAddresses = {devices[i]: mo.group() for i, mo in enumerate(re.finditer(ip_regex, text))}
print("all IP address of the known devices ", devAddresses)
print("IP address of WEB server is ", devAddresses["WEB Server"])