# BVG (Berlin Public Transport)

[![GitHub Release][releases-shield]][releases]
[![License][license-shield]](LICENSE)

[![hacs][hacsbadge]][hacs]
[![Project Maintenance][maintenance-shield]][user_profile]
[![BuyMeCoffee][buymecoffeebadge]][buymecoffee]


## Overview

This is an integration for [Home Assistant](https://www.home-assistant.io/) (a tool for managing and viewing your 'smart' devices at home). This integration adds the ability to track the next departure times for bus and trains stops on Berlin Public Transport.  

It is an extension of work by [@tobias-richter](https://github.com/tobias-richter) and [@fluffykraken](https://github.com/fluffykraken), forked to be made HACS ready and to pick up (seemingly) abandoned code.  

## HACS Installation

1. Open HACS and select `Integrations`
2. Click `Explore and Download Repositories`
3. Type 'bvg' into the search
4. Click 'Download this repo with HACS'
5. Restart Home Assistant

## Manual Installation

1. Using the tool of choice open the directory (folder) for your HA configuration (where you find `configuration.yaml`).
2. If you do not have a `custom_components` directory (folder) there, you need to create it.
3. In the `custom_components` directory (folder) create a new folder called `bvg_hacs`.
4. Download _all_ the files from the `custom_components/bvg_hacs/` directory (folder) in this repository.
5. Place the files you downloaded in the new directory (folder) you created.
6. Restart Home Assistant

# Prequisites

You will need to specify at least a ``stop_id`` and a ``direction`` for the connection you would like to display.

To find your ``stop_id`` use the following link: https://1.bvg.transport.rest/stations/nearby?latitude=52.52725&longitude=13.4123 and replace the values for ```latitude=``` and ```longitude=``` with your coordinates. You can get those e.g. from Google Maps.
Find your `stop_id` within the json repsonse in your browser. 

### Example:
You want to display the departure times from "U Rosa-Luxemburg-Platz" in direction to "Pankow"

#### get the stop_id:

Link: https://1.bvg.transport.rest/stations/nearby?latitude=52.52725&longitude=13.4123

``

{"type":"stop","id":"900000100016","name":"U Rosa-Luxemburg-Platz","location":{"type":"location","latitude":52.528187,"longitude":13.410405},"products":{"suburban":false,"subway":true,"tram":true,"bus":true,"ferry":false,"express":false,"regional":false},"distance":165}

``

Your ``stop_id`` for ``"U Rosa-Luxemburg-Platz"`` would be ``"900000100016"``

#### get the direction:

Specify the final destination (must be a valid station name) for the connection you want to display. In this example this would be ``Pankow``. If your route is beeing served by multiple lines with different directions, you can define multiple destinations in your config.

```yaml
# Example configuration.yaml entry
- platform: bvgsensor
    stop_id: your stop id
    direction: 
      - "destionation 1"
      - "destination 2"
````

# Configuration

To add the BVG Sensor Component to Home Assistant, add the following to your `configuration.yaml` file:

```yaml
# Example configuration.yaml entry
- platform: bvgsensor
    stop_id: your stop id
    direction: the final destination for your connection
````

- **stop_id** *(Required)*: The stop_id for your station.
- **direction** *(Required)*: One or more destinations for your route.
- **name** *(optional)*: Name your sensor, especially if you create multiple instance of the sensor give them different names. * (Default=BVG)*
- **walking_distance** *(optional)*: specify the walking distance in minutes from your home/location to the station. Only connections that are reachable in a timley manner will be shown. Set it to ``0`` if you want to disable this feature. *(Default=10)*
- **file_path** *(optional)*: path where you want your station specific data to be saved. *(Default= your home assistant config directory e.g. "conf/" )*

### Example Configuration:
```yaml
sensor:
  - platform: bvgsensor
    name: U2 Rosa-Luxemburg-Platz
    stop_id: "900000100016"
    direction: "Pankow"
    walking_distance: 5
    file_path: "/tmp/"
```

<!---->

## Credits

Core sensor code was written by It is an extension of work by [@fluffykraken](https://github.com/fluffykraken) and updated by [@tobias-richter](tobias-richter). 

This project was generated from [@oncleben31](https://github.com/oncleben31)'s [Home Assistant Custom Component Cookiecutter](https://github.com/oncleben31/cookiecutter-homeassistant-custom-component) template.

[buymecoffee]: https://www.buymeacoffee.com/secretdarkR
[buymecoffeebadge]: https://img.shields.io/badge/buy%20me%20a%20coffee-donate-yellow.svg?style=for-the-badge
[hacs]: https://hacs.xyz
[hacsbadge]: https://img.shields.io/badge/HACS-Custom-orange.svg?style=for-the-badge
[exampleimg]: example.png
[license-shield]: https://img.shields.io/github/license/ryanbateman/bvg_hacs.svg?style=for-the-badge
[maintenance-shield]: https://img.shields.io/badge/maintainer-%40ryanbateman-blue.svg?style=for-the-badge
[releases-shield]: https://img.shields.io/github/release/ryanbateman/bvg_hacs.svg?style=for-the-badge
[releases]: https://github.com/ryanbateman/bvg_hacs/releases
[user_profile]: https://github.com/ryanbateman
