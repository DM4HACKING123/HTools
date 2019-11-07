import scapy.all as scapy
def arping(ip):
  scapy.ARP(pdst=ip)
