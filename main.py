from danfsvc import *
from dbsvc import *
from datetime import datetime

danfosToken = getDanfosToken()

allDevices = getAllyDevices(danfosToken)

allRadiatorsThermostat = filterAllyRadiatorThermostat(allDevices)

now = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

for t in allRadiatorsThermostat:
    name = getRadiatorThermostatName(t)
    currentTemperature = getRadiatorThermostatCurrentTemperature(t)
   # updateTime = getRadiatorThermostatUpdateTimeInSeconds(t) * 1000
    writeMeasure(now, "radiators", name+"_current_temperature", currentTemperature)

