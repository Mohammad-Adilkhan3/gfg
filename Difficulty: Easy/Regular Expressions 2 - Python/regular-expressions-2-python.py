def validate(str):
    pat= '^[a-z]+[!@#$%]+[0123456789]'
    match = re.search(pat, str)
    if(match):
        return True
    else:
        return False
