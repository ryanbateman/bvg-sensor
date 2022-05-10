# BVG (Berlin Public Transport)

[![GitHub Release][releases-shield]][releases]
[![License][license-shield]](LICENSE)

[![hacs][hacsbadge]][hacs]
[![Project Maintenance][maintenance-shield]][user_profile]
[![BuyMeCoffee][buymecoffeebadge]][buymecoffee]


## Overview

This is an integration for [Home Assistant](https://www.home-assistant.io/) (a tool for managing and viewing your 'smart' devices at home). This integration adds the ability to track the next departure times for bus and trains stops on Berlin Public Transport. It is an extension of work by [@tobias-richter](tobias-richter) and [@fluffykraken](https://github.com/fluffykraken). 

## Installation

1. Using the tool of choice open the directory (folder) for your HA configuration (where you find `configuration.yaml`).
2. If you do not have a `custom_components` directory (folder) there, you need to create it.
3. In the `custom_components` directory (folder) create a new folder called `bvg_hacs`.
4. Download _all_ the files from the `custom_components/bvg_hacs/` directory (folder) in this repository.
5. Place the files you downloaded in the new directory (folder) you created.
6. Restart Home Assistant
7. In the HA UI go to "Configuration" -> "Integrations" click "+" and search for "BVG (Berlin Public Transport)"

Using your HA configuration directory (folder) as a starting point you should now also have this:

```text
custom_components/bvg_hacs/translations/en.json
custom_components/bvg_hacs/translations/fr.json
custom_components/bvg_hacs/translations/nb.json
custom_components/bvg_hacs/translations/sensor.en.json
custom_components/bvg_hacs/translations/sensor.fr.json
custom_components/bvg_hacs/translations/sensor.nb.json
custom_components/bvg_hacs/translations/sensor.nb.json
custom_components/bvg_hacs/__init__.py
custom_components/bvg_hacs/api.py
custom_components/bvg_hacs/binary_sensor.py
custom_components/bvg_hacs/config_flow.py
custom_components/bvg_hacs/const.py
custom_components/bvg_hacs/manifest.json
custom_components/bvg_hacs/sensor.py
custom_components/bvg_hacs/switch.py
```

## Configuration is done in the UI

<!---->

## Contributions are welcome!

If you want to contribute to this please read the [Contribution guidelines](CONTRIBUTING.md)

## Credits

This project was generated from [@oncleben31](https://github.com/oncleben31)'s [Home Assistant Custom Component Cookiecutter](https://github.com/oncleben31/cookiecutter-homeassistant-custom-component) template.

Code template was mainly taken from [@Ludeeus](https://github.com/ludeeus)'s [integration_blueprint][integration_blueprint] template

---

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
