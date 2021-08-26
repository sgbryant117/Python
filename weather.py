

import requests


url = 'https://api.tomorrow.io/v4/timelines'

api_key = "cGLfpt3VG95Cwy3VkQ1brNLGFTDsGndg"

querystring = {
 "location" : "33.7,-116.7",
 "fields" : "temperature",
 "units" : "imperial",
 "timesteps" : "1d",
 "apikey" : api_key
}

api_response = requests.request("GET", url, params = querystring)
weather_data = api_response.text

print(weather_data['data']['timelines'][0]['intervals'][0]['values']['temperature'])
print(type(weather_data))

for k,v in weather_data.items():
    print("{} {}".format(k,v))


def main():

    print("weather")

main()
