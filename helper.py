import json
import logging

# Loading json 

try:

    with open('firewallRules.json','r') as file:
        rules = json.load(file)

except FileNotFoundError as e:
    print("Getting Error: ",e)

except json.JSONDecodeError as e:
    print("Getting Error:",e) 

finally:
    file.close()


# {
#     "BannedIpAddress" : [],
#     "BannedPorts" : [],
#     "BannedSubnet" : [],
#     "Timethreshold" : 10
# }

# ins = isinstance(rules,dict)
# print(ins)

def get_BannedIpAddr():

    if "BannedIpAddress" in rules and isinstance(rules["BannedIpAddress"],list):
        BannedIpAddr = rules['BannedIpAddress']

    else:
        BannedIpAddr = []
    return BannedIpAddr
    
def get_BannedPort():
    
    if "BannedPorts" in rules and isinstance(rules['BannedPorts'],list):
        BannedPorts = rules['BannedPorts']
        
    else:
        BannedPorts = []
    return BannedPorts
    
def get_BannedPrefix():
    if "BannedSubnet" in rules and isinstance(rules['BannedSubnet'],list):
        Bannedprefix = rules['BannedSubnet']
    
    else:
        Bannedprefix = []
    return Bannedprefix

def get_timeThreshold():
    if 'TimeThreshold' in rules and isinstance(rules['TimeThreshold'],int):
        time = rules['TimeThreshold']
    else:
        time = 10
    return time

def get_pingAttack():
    if "BlockPingAttack" in rules and isinstance(rules["BlockPingAttack"],str):
        BlockPingAttack = rules["BlockPingAttack"]

    else:
        BlockPingAttack = True
    return eval(BlockPingAttack)


# Function for outgoing rules

try:

    with open('outgoingFirewallRules.json','r') as outfile:
        outrules = json.load(outfile)

except FileNotFoundError as e:
    print("Getting Error: ",e)

except json.JSONDecodeError as e:
    print("Getting Error:",e) 

finally:
    outfile.close()

# {
#     "BlockIpAddress" : [],
#     "BlockPorts" : []
# }

def get_outIpAddr():
    if "BlockIpAddress" in outrules and isinstance(outrules["BlockIpAddress"],list):
        BlockIpAddr = outrules["BlockIpAddress"]
    else:
        BlockIpAddr = []
    return BlockIpAddr

def get_outPort():
    if "BlockPorts" in outrules and isinstance(outrules["BlockPorts"],list):
        BlockPort = outrules["BlockPorts"]
    else:
        BlockPort = []
    return BlockPort

ip = get_BannedIpAddr()
port = get_BannedPort()
pr = get_BannedPrefix()
t = get_timeThreshold()

print(ip,port,pr,t)