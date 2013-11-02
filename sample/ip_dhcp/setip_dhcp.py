#!/usr/bin/env python

import wmi

def set_ip_mask_gateway(ip,mask,gateway):
	try:

		nic_configs = wmi.WMI().win32_NetworkAdapterConfiguration(IPEnabled=True)
		print nic_configs
		nic = nic_configs[0]
		ip = u'192.168.0.11'
		netmask = u'255.255.0.0'
		gateway = u'192.168.0.1'

		nic.EnableStatic(IPAddress=[ip],SubnetMask=[netmask])
		nic.SetGateways(DefaultIPGateway=[gateway])
	except Exception,detail:
		print str(detail)


def set_dhcp():
	try:
		nic_configs = wmi.WMI().win32_NetworkAdapterConfiguration(IPEnabled=True)
		print nic_configs
		nic = nic_configs[0]
		nic.EnableDHCP()
	except Exception,detail:
		print str(detail)



if __name__ == '__main__':
	set_dhcp()
