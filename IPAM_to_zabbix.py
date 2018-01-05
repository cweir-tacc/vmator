import phpipam_scraper as ipam
from pyzabbix import ZabbixAPI, ZabbixAPIException
import sys

# The hostname at which the Zabbix web interface is available
ZABBIX_SERVER = "https://zabbix.tacc.utexas.edu"

zapi = ZabbixAPI(ZABBIX_SERVER)

# Login to the Zabbix API
username = 'cgweir'
password = ''

zapi.login(username, password)

host_name = ''

# Get the hosts with the name 'host_name'
hosts = zapi.host.get(filter={"host": host_name}, selectInterfaces=["interfaceid"])




# Remove this, Its was an example of creating a new zabbix item for a Host
# if hosts:
#     host_id = hosts[0]["hostid"]
#     print("Found host id {0}".format(host_id))
#
#     try:
#         item = zapi.item.create(
#             hostid=host_id,
#             name='Used disk space on $1 in %',
#             key_='vfs.fs.size[/,pused]',
#             type=0,
#             value_type=3,
#             interfaceid=hosts[0]["interfaces"][0]["interfaceid"],
#             delay=30
#         )
#     except ZabbixAPIException as e:
#         print(e)
#         sys.exit()
#     print("Added item with itemid {0} to host: {1}".format(item["itemids"][0], host_name))
# else:
#     print("No hosts found")