# defines autodoor object




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
        pass
    