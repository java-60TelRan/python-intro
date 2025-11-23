import regular_expressions as regex
import sys
import re
text: str = "The internal network contains the following devices.\
    WEB server is running at 172.0.5.20. Database server is running at 10.0.5.20.\
        Backup is available through 172.0.5.40. Monitoring sends notifications from 85.12.30.7.\
            Whitelist for access from external network contains IP addresses from 200.13.4.1 to \
                200.13.4.100"
ip_regex= regex.ipV4AddressRe() 
ip_pattern = re.compile(ip_regex) 
mo = ip_pattern.search(text)
ip = mo.group()
print("ip address", ip)
print("first octet of ip address", re.search(r"\d{1,3}", ip).group())
print( "three first octets", re.findall(r"\d{1,3}", ip)[:-1])

