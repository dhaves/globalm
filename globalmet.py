'''import urllib, json
url = "http://api.plos.org/search?q=title:DNA"
response = urllib.urlopen(url)
data = json.loads(response.read().decode("utf-8"))
print (data['response']['numFound'])
'''

import urllib2, json,csv
from datetime import datetime
from os import path

def writeRowToFile(r):
	if(path.exists("log.csv")):
		with open("log.csv","a") as f:
			cr = csv.writer(f,delimiter=",",lineterminator="\n")
			cr.writerow(r)
            
	else:
		with open("log.csv","w") as f:
			cr = csv.writer(f,delimiter=",",lineterminator="\n")
			cr.writerow(["id_estacion","fecha_medicion", "temp_c", "temp_f","wind_kph","wind_mph","wind_dir","precip_today_metric","precip_today_imperial","relative_humidity","eto"])
			cr.writerow(r)

#  with open("log.csv","a") as f:
    #  cr = csv.writer(f,delimiter=",",lineterminator="\n")

    #  cr.writerow(r)


headers = { 'Authorization' : 'Token ea86a649b495c8cb159b32a89099359503f8ff28' }
req = urllib2.Request("http://globalmet.mx/estaciones/conditions/78/")
req.add_header('User-Agent' , 'PostmanRuntime/7.26.8')
req.add_header('Authorization' , 'Token ea86a649b495c8cb159b32a89099359503f8ff28')
response = urllib2.urlopen(req).read().decode("utf-8")
data = json.loads(response)
wind_kph=data['current_observation']['wind_kph']
wind_mph= 0.6214 * wind_kph
celsius=data['current_observation']['temp_c']
wind_dir=data['current_observation']['wind_dir']
precip_today_metric=data['current_observation']['precip_today_metric']
relative_humidity=data['current_observation']['relative_humidity']
fahrenheit = (celsius * 9/5) + 32 
eto=data['current_observation']['eto']
fecha_medicion=str(data['current_observation']['fecha_medicion']).replace(":","_")

precip_today_imperial=precip_today_metric*0.03937007874
print('La temeratura en C =  %0.2f '%(celsius))
print('La temperatura en F = %0.2f ' %(fahrenheit))
print('Velocidad del Viento en kph: %0.2f ' %(wind_kph))
print('Velocidad del Viento en mph: %0.2f ' %(wind_mph))
print('Con direccion: %s ' %(wind_dir))
print('Precipitacion hoy: %0.3f ' %(precip_today_metric))
print('Precipitacion hoy(Pulgadas): %0.3f ' %(precip_today_imperial))
print('Humedad relativa: %s ' %(relative_humidity))
print('Evapotranspiracion: %0.3f ' %(eto))
print('Fecha medicion: %s ' %(fecha_medicion))
row=["a","b","c","d"]
# cr.writerow(["id_estacion","fecha_medicion", "temp_c", "temp_f","wind_kph","wind_mph","wind_dir","precip_today_metric","precip_today_imperial","relative_humidity","eto"])

w=[78,fecha_medicion,celsius,fahrenheit,wind_kph,wind_mph,wind_dir,precip_today_metric,precip_today_imperial,relative_humidity,eto]
writeRowToFile(w)


# print (response)
exit(0)


















import urllib
import urllib2






url = 'http://globalmet.mx/estaciones/conditions/78/'

# headers = { 'as' : 'a'}
headers = { 'Authorization' : 'Token ea86a649b495c8cb159b32a89099359503f8ff28'}

req = urllib2.Request(url, None, headers)
response = urllib2.urlopen(req).read()
the_page = response.read()

print(the_page)
exit(0)




now = str(datetime.now()).replace(" ","_").replace(".","_").replace(":","-") # current date and time
print(now)


wind_kph=16.4
wind_mph= 0.6214 * wind_kph
celsius=45
wind_dir=270
precip_today_metric=25
relative_humidity="61%"
fahrenheit = (celsius * 9/5) + 32 
eto=16
precip_today_imperial=precip_today_metric*0.03937007874
print('La temeratura en C =  %0.2f '%(celsius))
print('La temperatura en Fis: %0.2f Fahrenheit' %(fahrenheit))
print('Velocidad del Viento en kph: %0.2f ' %(wind_kph))
print('Velocidad del Viento en mph: %0.2f ' %(wind_mph))
print('Con direccion: %0.1f ' %(wind_dir))
print('Precipitacion hoy: %0.3f ' %(precip_today_metric))
print('Precipitacion hoy(Pulgadas): %0.3f ' %(precip_today_imperial))
print('Humedad relativa: %s ' %(relative_humidity))
print('Evapotrasnpiracion: %0.3f ' %(eto))





exit(0)
print(response)

