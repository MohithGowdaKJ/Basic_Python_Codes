def swapCase(s):
    sample = ''
    for i in s:
        if i.islower():
            sample = sample + i.upper()
        else:
            sample = sample + i.lower()
    print(sample)

swapCase('MoHitH')