Author: Mon4rch

import re

has_www = "www"
has_http = "http"
has_https = "https"
hyphen = '-'
def domain_name(url):
"""
This function extracts domain names (excluding TLD)
"""
    print(url)
    if has_www in url:
        domain = re.findall(r"[.](\w+)[.]", url)
        return ''.join(domain)
    
    elif hyphen in url:
        domain = re.findall(r"(\w+[-]\w+)+[?<=.][^.]+", url)
        return ''.join(domain)  
    
    elif has_http in url:
        domain = re.findall(r"[^http|:](\w+)[?<=.].*[^.]+", url)
        return ''.join(domain)
    
    elif has_https in url:
        domain = re.findall(r"[^https|:|](\w+)[?<=.].*[^.]+", url)
        return ''.join(domain)      
    
    else:
        domain = re.findall(r"(\w+)[?<=.].*[^.]+",url)
        return ''.join(domain)
    
    
