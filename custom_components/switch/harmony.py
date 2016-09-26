#####SWITCH####
from homeassistant.components.switch import SwitchDevice
from homeassistant.const import CONF_NAME, CONF_USERNAME, CONF_PASSWORD, CONF_PORT
import pyharmony
import logging


DOMAIN = 'harmony'
REQUIREMENTS = ['pyharmony>=0.2.0']
_LOGGER = logging.getLogger(__name__)
CONF_IP = 'ip'


def setup_platform(hass, config, add_devices_callback, configData, discovery_info=None):
    for activity in configData['activities']:
        add_devices_callback([HarmonySwitch(activity,
                                        configData['name'],
                                        configData['username'],
                                        configData['password'],
                                        configData['ip'],
                                        configData['port'],
                                        False, 
                                        configData['activities'][activity])])

    return True


class HarmonySwitch(SwitchDevice):
    """Switch used to start a Harmony Hub activity"""
    def __init__(self, activityName, hubName, username, password, ip, port, state, activityID):
        self._name = hubName + '-' + activityName
        self._email = username
        self._password = password
        self._ip = ip
        self._port = port
        self._state = state
        self._activityID = activityID
        

    @property
    def name(self):
        """Return the name of the activity"""
        return self._name    
    @property
    def activityID(self):
        return self._activityID
    @property
    def is_on(self):
        return self._state
        
    def turn_on(self):
        pyharmony.ha_start_activity(self._email, self._password, self._ip, self._port, self._activityID)
        self._state = False