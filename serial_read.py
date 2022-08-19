import json

import serial
from time import sleep

from tb_device_mqtt import TBDeviceMqttClient, TBPublishInfo

device_token = "token"

client = TBDeviceMqttClient("127.0.0.1", device_token)

sr = serial.Serial('/dev/ttyACM0')
print('\nStatus -> ', sr)
while True:
    line = sr.readline()
    decoded = line.decode("utf-8")
    try:
        j = json.loads(decoded)
    except:
        continue

    client.connect()
    # Sending telemetry without checking the delivery status

    # client.send_telemetry(telemetry)
    # Sending telemetry and checking the delivery status (QoS = 1 by default)
    result = client.send_telemetry(j)
    # get is a blocking call that awaits delivery status
    success = result.get() == TBPublishInfo.TB_ERR_SUCCESS
    # Disconnect from ThingsBoard
    client.disconnect()
    print("Data Transferred")
    print(j)
    # j = json.loads(str(line))
    # print(j)
sr.close()