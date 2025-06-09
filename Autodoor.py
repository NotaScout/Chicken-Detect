# defines autodoor object
# generic # includes
import os

# Omlet SDK
from dotenv import load_dotenv
from smartcoop.client import SmartCoopClient 
from smartcoop.api.omlet import Omlet 

# device objects
from Autodoor import Autodoor


#  Load the .env file FIRST
load_dotenv("ENVIRON.env")

#  Then read from it
api_key_d1 = os.getenv("DOOR_1_API_KEY")
db_name_d1 = os.getenv("DB_NAME")
debug_mode = os.getenv("DEBUG")

#  Then use it
client = SmartCoopClient(client_secret=api_key_d1)
omlet = Omlet(client)
deviceInfo = omlet.get_devices()
dev0 = deviceInfo[0]
# Print values


# make in future grab specific named door
def fetchDoor():
    
    return dev0


class OMLET_API():
    def __init__(self):
        self.APIKEY = api_key_d1
        self.DBINFO = db_name_d1
        self.DBMODE = debug_mode

class Autodoor():
    def __init__(self, doorInfo):
        self.deviceInfo = doorInfo
        self.deviceId = doorInfo.deviceId
        self.name = doorInfo.name
        self.deviceType = doorInfo.deviceType
        self.state = doorInfo.state
        self.configuration = doorInfo.configuration
        self.actions = doorInfo.actions
    '''
    6/8/25

    opens autodoor
    '''
    async def open_door():
        omlet
    


'''
print(f"API Key: {api_key_d1}")
print(f"Database: {db_name_d1}")
print(f"Debug mode: {debug_mode}")
print(f"Devices={dev0}")
'''