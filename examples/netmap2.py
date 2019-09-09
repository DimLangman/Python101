import nmap

nm = nmap.PortScanner()

# Scan Linksys
nm.scan('192.168.1.4', '1-1024')
print (nm.csv())

# Scan LAN
nm.scan(hosts='192.168.1.0/24', arguments='-n -sP -PE -PA80,3389')
hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
for host, status in hosts_list:
    print('{0}:{1}'.format(host, status))


