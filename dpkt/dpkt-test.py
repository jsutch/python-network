import dpkt
import socket

def printPcap(pcap):
    for (ts,buf) in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            # read the source IP in src
            src = socket.inet_ntoa(ip.src)
            # read the destination IP in dst
            dst = socket.inet_ntoa(ip.dst)

            # Print the source and destination IP
            print('Source: ' +src+ ' Destination: '  +dst)

        except:
            pass

# Open pcap file for reading
# must add 'rb' - if the reader hits a utf-8 byte it will hork
f = open('mycap.pcap','rb')
#pass the file argument to the pcap.Reader function
pcap = dpkt.pcap.Reader(f)
printPcap(pcap)

