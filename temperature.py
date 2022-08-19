import logging
# Importing models and REST client class from Community Edition version
from tb_rest_client.rest_client_ce import *
# Importing the API exception
from tb_rest_client.rest import ApiException


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(module)s - %(lineno)d - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

# ThingsBoard REST API URL
url = "http://localhost:9090"
# Default Tenant Administrator credentials
username = "username"
password = "password"


# Creating the REST client object with context manager to get auto token refresh
with RestClientCE(base_url=url) as rest_client:
    try:
        # creating a Device
        device = Device(name="Thermometer 1", type="thermometer", device_profile_id="894fcc20-1edc-11ed-9523-2b90da0aac54")
        device = rest_client.save_device(device)

        logging.info(" Device was created:\n%r\n", device)

        # find device by device id
        found_device = rest_client.get_device_by_id(DeviceId('DEVICE', device.id))

        # save device shared attributes
        res = rest_client.save_device_attributes("{'targetTemperature': 22.4}", DeviceId('DEVICE', device.id),
                                                 'SERVER_SCOPE')

        logging.info("Save attributes result: \n%r", res)


        # Get device shared attributes
        res = rest_client.get_attributes_by_scope('DEVICE', DeviceId('DEVICE', device.id), 'SERVER_SCOPE')
        logging.info("Found device attributes: \n%r", res)
        # delete the device
        rest_client.delete_device(DeviceId('DEVICE', device.id))
    except ApiException as e:
        logging.exception(e)