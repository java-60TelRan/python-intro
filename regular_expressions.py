def pythonicNameRe()->str:
    return r"[A-Za-z_]\w*"
def passwordRe():
    return r"(?=.*[A-Z])(?=.*[a-z])(?=.*[#$%])(?=.*[\d])[A-Za-z#$%\d_-]{8,}"
def ipV4AddressRe()->str:
    # TODO
    """returns regexp as match pattern of IPv4 address
       comprises of 4 octets separated by dot
       each octet contains 1-3 symbols from 0 to 255
    """    
def mobileIsraelNumberRe()->str:
    # TODO
    """returns regexp for mobile phone Israel number
       +972- - Israel preffix (not mandatary)
       Operator preffix 0 (only without +972-)
       50,51, 52, 53, 54, 55, 56, 57,58, 59
       optional dash
       7 digits as follows
       xxxxxxx
       xxx-xx-xx
       x-xx-xx-xx
    """    