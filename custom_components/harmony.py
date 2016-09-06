####HUB###
from homeassistant.components.discovery import load_platform
import logging


DOMAIN = 'harmony'
DEPENDENCIES = []
_LOGGER = logging.getLogger(__name__)
_LOGGER.setLevel(logging.CRITICAL)



def setup(hass, config):
    load_platform(hass, 'sensor', DOMAIN, config[DOMAIN])
    return True
