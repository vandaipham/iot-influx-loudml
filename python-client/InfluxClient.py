from http import client
from influxdb_client import InfluxDBClient, Point
from influxdb_client .client.write_api import SYNCHRONOUS

# Connect to InfluxDB
URL = "http://yourIPaddress:8086"
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

myDict = {'temperature':0, 'humidity':0, 'sound_level':0, 'light_level':0, 'UV_Index':0,
            'presure':0, 'eco2':0, 'tvoc':0, 'magnetic':0, 'battery': 0}


myUpload = createDataUpload(node="123456", sensorData=myDict)
write_api.write(my_bucket, "-", myUpload)

client.close()