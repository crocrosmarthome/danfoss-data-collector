import base64, requests, json

import os

_client_id = os.environ['DANFOSS_CLIENT_ID']
_client_secret = os.environ['DANFOSS_CLIENT_SECRET']

def getDanfosToken():

    # Encode the client ID and client secret
    authorization = base64.b64encode(bytes(_client_id + ":" + _client_secret, "ISO-8859-1")).decode("ascii")
    headers = {
        "Authorization": f"Basic {authorization}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    body = {
        "grant_type": "client_credentials"
    }
    response = requests.post("https://api.danfoss.com/oauth2/token", data=body, headers=headers)
    bearer = json.loads(response.text)
    return bearer['access_token']


def getAllyDevices(token: str):
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json"
    }
    response = requests.get("https://api.danfoss.com/ally/devices", headers=headers)
    return json.loads(response.text)['result']


def filterAllyRadiatorThermostat(allDevices: list):
    return list(filter(lambda device: (device['device_type'] == 'Danfoss Ally™ Radiator Thermostat'), allDevices))

def getRadiatorThermostatName(radiatorThermostat):
    return radiatorThermostat['name']

def getRadiatorThermostatCurrentTemperature(radiatorThermostat):
    return next(filter(lambda stat: (stat['code'] == 'temp_current'), radiatorThermostat['status']), None)['value'] / 10

def getRadiatorThermostatUpdateTimeInSeconds(radiatorThermostat):
    return radiatorThermostat['update_time']



