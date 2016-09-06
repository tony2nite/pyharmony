#####SENSOR####
from homeassistant.helpers.entity import Entity
from homeassistant.const import CONF_NAME, CONF_USERNAME, CONF_PASSWORD, CONF_PORT
import pyharmony
import logging



DEPENDENCIES = []
_LOGGER = logging.getLogger(__name__)
CONF_IP = 'ip'


def setup_platform(hass, config, add_devices, discovery_info=None):
    """Setup the sensor platform."""
    for hub in discovery_info:
        add_devices([HarmonySensor(hub[CONF_NAME],
                     hub[CONF_USERNAME],
                     hub[CONF_PASSWORD],
                     hub[CONF_IP],
                     hub[CONF_PORT])])
    return True


class HarmonySensor(Entity):
    """Representation of a Sensor."""
    def __init__(self, name, username, password, ip, port):
        self._name = name
        self._email = username
        self._password = password
        self._ip = ip
        self._port = port

                
    def _get_status(self): 
        return pyharmony.show_current_activity(self._email, self._password, self._ip, self._port)

		
    @property
    def name(self):
        """Return the name of the sensor."""
        return self._name


    @property
    def state(self):
        """Return the state of the sensor."""
        return self._get_status()
    






