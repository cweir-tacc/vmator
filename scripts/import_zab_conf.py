from pyzabbix import ZabbixAPI, ZabbixAPIException
import sys

# The hostname at which the Zabbix web interface is available
ZABBIX_SERVER = "https://zabbix.tacc.utexas.edu"

zapi = ZabbixAPI(ZABBIX_SERVER)

# Login to the Zabbix API
username = 'cgweir'
password = '' # ASK FOR PASSWORD

zapi.login(username, password)

host_name = ''

# Get the hosts with the name 'host_name'
host = zapi.host.get(filter={"host": host_name}, selectInterfaces=["interfaceid"])

# Get all the hosts
hosts = zapi.host.get()

for h in hosts:
    print("Found host id {0}".format(host_id))