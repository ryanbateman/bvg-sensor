"""Adds config flow for BVG (Berlin Public Transport)."""
from homeassistant import config_entries

from .const import DOMAIN, PLATFORMS


class BvgBerlinPublicTransportFlowHandler(config_entries.ConfigFlow, domain=DOMAIN):
    """Config flow for bvg_berlin_public_transport."""

    VERSION = 1
    CONNECTION_CLASS = config_entries.CONN_CLASS_CLOUD_POLL

    def __init__(self):
        """Initialize."""
        self._errors = {}
