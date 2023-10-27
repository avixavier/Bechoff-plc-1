# import pycomm3
#
#
# from pycomm3 import LogixDriver
# plc_ip = "192.168.2.195"
# username = 'Administrator'
# password = '1'
# customport= 851
#
#
import  pymodbus 

from pymodbus.client.sync import ModbusTcpClient
from pymodbus.exceptions import ConnectionException

PLC_IP_ADDRESS = '192.168.2.195'
PLC_PORT = 502

client = ModbusTcpClient(PLC_IP_ADDRESS, port=PLC_PORT)

try:
    client.connect()
except ConnectionException as e:
    print(f"Connection to the PLC failed: {e}")
    exit(1)
client.close()
