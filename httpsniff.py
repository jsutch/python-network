#!/usr/bin/python

import socket
import struct
import binascii

def mac_print(mac):
 mac_ad = "%.2x:%.2x:%.2x:%.2x:%.2x:%.2x" % (ord(mac[0]), ord(mac[1]), ord(mac[2]), ord(mac[3]), ord(mac[4]), ord(mac[5]))
 return mac_ad

RawSocket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))

while True:
 packet = RawSocket.recvfrom(65565)
 
 # Check for the TCP packets
 IpHeader = packet[0][14:34]
 TcpHeader = packet[0][34:54]
 ip_hdr = struct.unpack("!B8s1s2s4s4s", IpHeader)
 tcp_hdr = struct.unpack("!HHLLB7s", TcpHeader)
 if binascii.hexlify(ip_hdr[2]) == "06" and (tcp_hdr[0] == 80 or tcp_hdr[1] == 80):
  # Check for the TCP protocol and port 80 [HTTP]
  
  # Extracting the Mac Address from EtherNet Header
  dst_mac = mac_print(packet[0][0:6])
  src_mac = mac_print(packet[0][6:12])

  # Extracting the IP address from IP header
  src_ip = socket.inet_ntoa(ip_hdr[4])
  dst_ip = socket.inet_ntoa(ip_hdr[5])

  # Extracting Source and Destination Port
  src_port = tcp_hdr[0]
  dst_port = tcp_hdr[1]

  # Calculating the length of data
  eth_length = 14
  iph_length = ip_hdr[0]
  iph_length = (iph_length & 0xF) * 4
  tcph_length = tcp_hdr[4]
  tcph_length = (tcph_length >> 4) * 4
  hdr_length = eth_length + iph_length + tcph_length
  data_length = len(packet[0]) - hdr_length
  Data = packet[0][hdr_length:]
  if Data == None:
   continue
  else:
   # print all The Data
   print("Source { IP : " + str(src_ip) + " | Mac : " + src_mac + " | Port : " + str(src_port) + " }")
   print("Dest.  { IP : " + str(dst_ip) + " | Mac : " + dst_mac + " | Port : " + str(dst_port) + " }")
   print("Data : " + Data)
   print("---------------------------------------")
