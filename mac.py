import sys,requests,re

def checkMAC(mac):
    octets = ''
    if len(mac) == 17:
        octets = re.split('[\:\-\;]', mac)
    elif len(mac) == 12:
        n = 2
        octets = [mac[i:i+n] for i in range(0, len(mac), n)]
    elif len(mac) < 12:
        print("MAC address to short")
        quit()
    elif len(mac) > 17:
        print("MAC address to long")
        quit()
    if len(octets) != 6:
        print("MAC address incorrect")
        quit()
    for i in octets:
        try:
            int(i, 16) > 255
        except:
            print("MAC address not hexadecimal")
            quit()
    return ":".join(octets)

def MACvendor(mac):
    try:
        resp = requests.get("https://api.macvendors.com/"+mac)
    except:
        print("Website unreachable: https://api.macvendors.com/"+mac)
        exit()
    if resp.status_code == 200:
        print(resp.text)
    else:
        print("Vendor not found")

def MAC(mac):
    mac = checkMAC(mac)
    print(mac.upper())
    MACvendor(mac)


if len(sys.argv) == 1:
    print('Missing MAC')
    quit()
else:
    MAC(sys.argv[1])
