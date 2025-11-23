import regular_expressions as regex
import re
text: str = "The internal network contains the following devices.\
    WEB server is running at 172.0.5.20. Database server is running at 10.0.5.20.\
        Backup is available through 172.0.5.40. Monitoring sends notifications from 85.12.30.7.\
            Whitelist for access from external network contains IP addresses from 200.13.4.1 to \
                200.13.4.100"
ip_regex= regex.ipV4AddressRe()               
mo:re.Match = re.search(ip_regex, text)
print(f"IP address: {mo.group()}; start index: {mo.start()}; end index: {mo.end()}")                