import random
from time import sleep

from tb_device_mqtt import TBDeviceMqttClient, TBPublishInfo


telemetry = {"temperature": random.randrange(0,50) , "enabled": False, "currentFirmwareVersion": "v1.2.2"}
client = TBDeviceMqttClient("127.0.0.1", "device_token")
# Connect to ThingsBoard
while True:
    client.connect()
    # Sending telemetry without checking the delivery status
    telemetry["temperature"] = random.randrange(0,50)
    # client.send_telemetry(telemetry)
    # Sending telemetry and checking the delivery status (QoS = 1 by default)
    result = client.send_telemetry(telemetry)
    # get is a blocking call that awaits delivery status
    success = result.get() == TBPublishInfo.TB_ERR_SUCCESS
    # Disconnect from ThingsBoard
    client.disconnect()
    print("Data Transferred")
    print(telemetry)
    sleep(5)