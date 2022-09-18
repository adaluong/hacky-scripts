#!/usr/bin/python3

import zipfile

def bruteforce(passwords, zipfile):
    """ Bruteforce the password for a zipfile given a list
    
    Args:
        passwords (str): name of text file containing a list of potential passwords
        zipfile (obj): zipfile to be cracked
        
    Returns:
        str or None: the successful password, or None
    
    """
    with open(passwords, "rb") as f:
        for line in f:
            line = line.strip()
            try:
                zipfile.extractall(pwd = line)
                return line.decode()
            except:
                continue
        return None


passwords = "password_list.txt"
zipname = "SECRET.ZIP"

zipfile = zipfile.ZipFile(zipname)
found_password = bruteforce(passwords, zipfile)

if found_password != None:
    print(f"the password for {zipname} is: {found_password}")
else:
    print(f"no password found for {zipname} in {passwords}")
