import logging
import time
import threading
import os
from colorama import Fore,Style
from netfilterqueue import NetfilterQueue
from scapy.all import IP, TCP, UDP, ICMP

from helper import *    #importing functions of helper

# Logging configurations
logging.basicConfig(
    filename='logs/firewall.log',  # Log file where the messages will be written
    level=logging.INFO,  # Set the logging level (could be DEBUG for more detail)
    format='%(asctime)s - %(levelname)s - %(message)s',  # Format of the log messages
)
# Create a logger object
logger = logging.getLogger('FirewallLogger')



BannedIpAddr = get_BannedIpAddr()
BannedPorts = get_BannedPort()
BannedPrefix = get_BannedPrefix()
TimeThreshold = get_timeThreshold()
BlockPingAttack = get_pingAttack()
OutBannedIp = get_outIpAddr()
OutBannedPorts = get_outPort()

def firewall(packet):
    pkt = IP(packet.get_payload())

# Checking that source ip of packet is in block ip's or not

    if pkt.src in BannedIpAddr:
        msg = f'Incoming : {pkt.src} is banned. {pkt.src} is trying to make connection'
        logger.info(msg)
        packet.drop
        return
    
# Checking Packet dest port is in tcp block port

    if pkt.haslayer(TCP):
        tcp = pkt.getlayer(TCP)
        if tcp.dport in BannedPorts:
            msg=f'Incoming : {tcp.dport} is banned, {pkt.src} is trying to connect on {tcp.dport}'
            logger.info(msg)
            packet.drop()
            return
    
# Checking Packet dest port is in udp block port

    if pkt.haslayer(UDP):
        udp = pkt.getlayer(UDP)
        if udp.dport in BannedPorts:
            msg=f'Incoming : {udp.dport} is banned, {pkt.src} is trying to connect on {udp.dport}'
            logger.info(msg)
            packet.drop()
            return
    
# Checking that Ip is from block subnet

    for p in BannedPrefix:
        if pkt.src.startswith(p):
            msg = f"Incoming : {pkt.src} is from Block Prefixes. {pkt.src} is trying to connect"
            logger.info(msg)
            packet.drop
            return
    
# Blocking Ping attack if true in rule
    DictOFPackets = {}
    PacketCountinSpecificTime = 100
    if BlockPingAttack and pkt.haslayer(ICMP):
        icmp = pkt.getlayer(ICMP)
        if icmp.code == 0 or True:
            if pkt.src in DictOFPackets:
                timestamp = list(DictOFPackets[pkt.src])
                if len(timestamp) >= PacketCountinSpecificTime:
                    if time.time() - timestamp[0] <= TimeThreshold:
                            msg = f"Incoming : Blocking Ping attack from {pkt.src}"
                            logger.warning(msg)
                            pkt.drop()

                    else:
                        DictOFPackets[pkt.src].pop(0)
                        DictOFPackets[pkt.src].append(time.time())

                else:
                    DictOFPackets[pkt.src].append(time.time())

            else:
                DictOFPackets[pkt.src] = [time.time()]
    
    packet.accept()
    return

def outFirewall(packet):
    pkt = IP(packet.get_payload())

    if pkt.dst in OutBannedIp:
        msg = f"Outgoing : Device is not allowed to connect to {pkt.dst}"        
        logger.info(msg)
        packet.drop()
        return

    if pkt.haslayer(TCP):
        tcp = pkt.getlayer(TCP)
        if tcp.sport in OutBannedPorts:
            msg = f"Outgoing : Device is not allowed to connect to port {tcp.sport}"
            logger.info(msg)
            packet.drop()
            return
    
    if pkt.haslayer(UDP):
        udp = pkt.getlayer(UDP)
        if udp.sport in OutBannedPorts:
            msg = f"Outgoing : Device is not allowed to connect to port {udp.sport}"
            logger.info(msg)
            packet.drop()
            return
    
    packet.accept()
    return

if __name__ == '__main__':

    os.system('clear')
    os.system('iptables --flush')
    os.system('iptables -I INPUT -d 192.168.37.0/24 -j NFQUEUE --queue-num 1')
    os.system("iptables -I OUTPUT -d 192.168.37.0/24 -j NFQUEUE --queue-num 2")

    print(f"{Style.BRIGHT} {Fore.GREEN} Firewall Started You can see Log in 'logs/' directory ")


#A NetfilterQueue object represents a single queue. Configure your queue with a call to bind, then start receiving packets with a call to run. NetfilterQueue.bind(queue_num, callback, max_len=1024, mode=COPY_PACKET, range=65535, sock_len=...)
    banner = '''🅿🅴🅽🆃🅴🆂🆃🅴🆁🅺🅰🆁🅰🅽'''
    print(f"{Fore.RED}                     creator :  {banner}{Style.RESET_ALL}")
    nfq = NetfilterQueue()
    nfq.bind(1,firewall)
    outnfq = NetfilterQueue()
    outnfq.bind(2,outFirewall)

    def incoming():
        nfq.run()
    def outgoing():
        outnfq.run()
    
    try:
        t1=threading.Thread(target=outgoing, daemon=True)
        t1.start()
        nfq.run()
    except KeyboardInterrupt as e:
        print("\nFirewall Closed: ",e)

    nfq.unbind()
    outnfq.unbind()

    os.system('iptables --flush')


