# home-automation-thermostat

## Built with
* Python 3.5

## Description


## Hardware

- [Raspberry Pi 3 Model B +](https://www.raspberrypi.org/documentation/usage/gpio/)
- [DS18B20 temperature sensor](https://cleste.ro/modul-senzor-de-temperatura-ds18b20.html)
- [5V Relay](https://cleste.ro/modul-releu-1-canal-5v.html)

### Hardware Picture
1. **Inoklima Thermostat on the TOP**

2. **Prototype Thermostat on the BOTTOM**

![Prototype](images/hardware.JPEG)

## Usage

```code
supervisord
uwsgi --http-socket :5000 --plugin python3 --wsgi-file wsgi.py
```
