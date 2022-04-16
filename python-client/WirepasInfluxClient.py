from http import client
from influxdb_client import InfluxDBClient, Point
from influxdb_client .client.write_api import SYNCHRONOUS
import struct
import paho.mqtt.client as mqtt
import wirepas_mesh_messaging as wmm


# Connect to MQTT broker.
host = '192.168.1.8'
port = 1883
username = 'mqttmasteruser'
password = '3mERrV0z7rzUqWVgWIlSsQxjl'

# Connect to InfluxDB
URL = "http://192.168.1.120:8888"
username = ''
password = ''

database = 'IoTDB'
retention_policy = 'autogen'
my_bucket = f'{database}/{retention_policy}'

InfluxClient = InfluxDBClient(url=URL, token=f'{username}:{password}', org='-')
write_api = InfluxClient.write_api(write_options=SYNCHRONOUS)

def createDataUpload(node, sensorData):
    """
    :param 
        node: the device Address or ID
        sensorData: the sensor data is in dictionary type, for example: {"temperature": 30.5, "humidity": 20.0}
    :return: a list to write into InfluxDB
    """

    myDict = {"measurement": "Multisensor", "tags": {"Node": node}, "fields": sensorData}
    return [myDict]


def parseMsg(a):
    myData = {'temperature':0, 'humidity':0, 'sound level':0, 'lightLevel':0, 'UV Index':0,
            'presure':0, 'eco2':0, 'tvoc':0, 'magnetic':0, 'battery': 0}
    rht = int.from_bytes([a[0], a[1], a[2], a[3]], byteorder = "little", signed = False) / 1000
    temperature = int.from_bytes([a[4], a[5], a[6], a[7]], byteorder = "little", signed = True) / 1000
    sndlvl = struct.unpack('<f', bytearray([a[8], a[9], a[10], a[11]]))
    lightLevel = struct.unpack('<f', bytearray([a[12], a[13], a[14], a[15]]))
    UVIndex = struct.unpack('<f', bytearray([a[16], a[17], a[18], a[19]]))
    presure = struct.unpack('<f', bytearray([a[20], a[21], a[22], a[23]]))
    eco2 = int.from_bytes([a[24], a[25]], byteorder='little', signed=False)
    tvoc = int.from_bytes([a[26], a[27]], byteorder='little', signed=False)
    magneticField = int.from_bytes([a[28], a[29], a[30], a[31]], byteorder = "little", signed = False) / 1000
    battery = int.from_bytes([a[44]], byteorder='little', signed=False)
    myData['temperature'] = temperature
    myData['humidity'] = rht
    myData['sound level'] = sndlvl[0]
    myData['lightLevel'] = lightLevel[0]
    myData['UV Index'] = UVIndex[0]
    myData['presure'] = presure[0]
    myData['eco2'] = eco2
    myData['tvoc'] = tvoc
    myData['magnetic'] = magneticField
    myData['battery'] = battery
    return myData

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("gw-event/received_data/raspi_iotlab/sink1/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    #print(msg.topic+" "+str(msg.payload))
    message = wmm.ReceivedDataEvent.from_payload(msg.payload)
    if (message.source_endpoint == 1 and message.destination_endpoint ==1):
        myUpload = createDataUpload(node=message.source_address, sensorData=parseMsg(message.data_payload))
        write_api.write(my_bucket, "-", myUpload)


# Wirepas Client
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set(username, password)
client.connect(host, port, 20)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()