####HUB###
from homeassistant.components.discovery import load_platform
from homeassistant.helpers import discovery
from homeassistant.helpers.entity import Entity
from homeassistant.const import CONF_NAME, CONF_USERNAME, CONF_PASSWORD, CONF_PORT
import logging
import pyharmony


DOMAIN = 'harmony'
REQUIREMENTS = ['pyharmony>=0.2.0']
_LOGGER = logging.getLogger(__name__)
CONF_IP = 'ip'


def setup(hass, config):
        # write file containing activities and commands
        #HARMONY_CONF_FILE = hass.config.path('harmonyConf-' + hub[CONF_NAME] + '.txt')
        #pyharmony.ha_get_config_file(hub[CONF_USERNAME], hub[CONF_PASSWORD], hub[CONF_IP], hub[CONF_PORT], HARMONY_CONF_FILE)
        
    # create current activity sensor for each Harmony device
    discovery.load_platform(hass, 'sensor', DOMAIN, {})
        # create switch for each activity
        #configData = hub
        #configData['activities'] = pyharmony.ha_get_activities(hub[CONF_USERNAME], hub[CONF_PASSWORD], hub[CONF_IP], hub[CONF_PORT])
        #load_platform(hass, 'switch', DOMAIN, configData)
    return True

class HarmonyDevice(Entity):
    """Representation of a base Harmony Device"""
    def __init__(self, name, username, password, ip, port):
        self._name = name
        self._email = username
        self._password = password
        self._ip = ip
        self._port = port

    @property
    def name(self):
        """Return the name of the Harmony device"""
        return self._name
            