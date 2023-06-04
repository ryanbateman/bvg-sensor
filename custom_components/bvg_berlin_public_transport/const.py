"""Constants for BVG (Berlin Public Transport)."""
# Base component constants
NAME = "BVG (Berlin Public Transport)"
DOMAIN = "bvg_berlin_public_transport"
DOMAIN_DATA = f"{DOMAIN}_data"
VERSION = "0.3.1"

ATTRIBUTION = "Data provided by the v6 BVG http://transport.rest API"
ISSUE_URL = "https://github.com/ryanbateman/bvg-sensor/issues"

# Icons
ICON = "mdi:format-quote-close"

# Device classes
BINARY_SENSOR_DEVICE_CLASS = "connectivity"

# Platforms
BINARY_SENSOR = "binary_sensor"
SENSOR = "sensor"
SWITCH = "switch"
PLATFORMS = [BINARY_SENSOR, SENSOR, SWITCH]

# Defaults
DEFAULT_NAME = DOMAIN

STARTUP_MESSAGE = f"""
-------------------------------------------------------------------
{NAME}
Version: {VERSION}
This is a custom integration!
If you have any issues with this you need to open an issue here:
{ISSUE_URL}
-------------------------------------------------------------------
"""
