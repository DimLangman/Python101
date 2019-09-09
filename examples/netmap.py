# import nmap
# from nmap import PortScanner
# nm = nmap.PortScanner()
# hostlist = ' '.join(nm.all_hosts())
# nm.scan(hosts=hostlist, arguments='-n -sP -PE')

# for host in nm.all_hosts():
#    print(host)
#    print(nm[host].get('osclass', 'unknown'))
#!/usr/bin/env python


import nmap
# import nmap.py module

directory = dir(nmap)
print (directory)

nm = nmap.PortScanner()
# nm.scan('127.0.0.1', '22-443')
nm.scan('192.168.1.124', '22-100')
print (nm.csv())

nm.scan(hosts='192.168.1.0/24', arguments='-n -sP -PE -PA21,23,80,3389')
hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
for host, status in hosts_list:
    print('{0}:{1}'.format(host, status))
