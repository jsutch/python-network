def printPcap(pcap):
    """
    dump source and destination ips
    """
    for (ts,buf) in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            # read the source IP in src
            src = socket.inet_ntoa(ip.src)
            # read the destination IP in dst
            dst = socket.inet_ntoa(ip.dst)

            # Print(the source and destination IP
            print('Source: ' +src+ ' Destination: '  +dst)

        except:
            pass

# pcap file must be opened as a bytes object
f = open ('mycap.pcap','rb')
pcap = dpkt.pcap.Reader(f)
printPcap(pcap)
