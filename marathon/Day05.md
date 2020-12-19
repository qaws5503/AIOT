# Day 5

## 作業1

問題：練習使用一個民生物聯網 API，例如空氣、地震等感測站所回傳的紀錄資料。[參考資料](https://ci.taiwan.gov.tw/dsp/environmental.aspx)

```python3
# python3

import requests
import pprint
# url for the API
url = 'https://sta.ci.taiwan.gov.tw/STA_AirQuality_v2/v1.0/Datastreams?$expand=Thing,Observations($orderby=phenomenonTime%20desc;$top=1)&$filter=name%20eq%20%27PM2.5%27%20and%20Thing/properties/authority%20eq%20%27%E8%A1%8C%E6%94%BF%E9%99%A2%E7%92%B0%E5%A2%83%E4%BF%9D%E8%AD%B7%E7%BD%B2%27%20and%20substringof(%27%E7%A9%BA%E6%B0%A3%E5%93%81%E8%B3%AA%E6%B8%AC%E7%AB%99%27,Thing/name)&$count=true'

response = requests.get(url)
result = response.json()
pprint.pprint(result)
```

## 作業2

問題：練習操作 OGC SensorThings API，將環保局測站位置的資料抓取下來，並且觀察下載資料的內容。[參考網址](https://sta.ci.taiwan.gov.tw/STA_AirQuality_EPAIoT/v1.0/Things)

```python3
# python3

import requests
import pprint
# url for the API
url = 'https://sta.ci.taiwan.gov.tw/STA_AirQuality_EPAIoT/v1.0/Things'

response = requests.get(url)
data = response.json()

value = data['value']


for i in range(len(value)):
    print("===data{}===".format(value[i]['@iot.id']))
    try:
        print("Locatiion:",value[i]['properties']['city']+',' + value[i]['properties']['township'])
    except:
        print("There is no Location data")
    # You can print any thing you want
```

## 作業3

問題：依據作業 2 所下載的各個環保局測站感測器的描述資料，進一步點選 Datastreams、Locations，以及 Datastreams 點選進入後，點選 Observations 的 URL，觀察所下載到的資料內容，其中 Observations 內部是否包含個別感測器紀錄的資料。

```python3
# python3

import requests
import pprint
# url for the APII
url = 'https://sta.ci.taiwan.gov.tw/STA_AirQuality_EPAIoT/v1.0/Things'

response = requests.get(url)
data = response.json()

value = data['value']

datastream_url_list=[]
for i in range(len(value)):
    datastream_url_list.append(value[i]['Datastreams@iot.navigationLink'])
datastream_url = datastream_url_list[0]
datastream_response = requests.get(datastream_url)
result = datastream_response.json()
pprint.pprint(result)
```

result is:

```js
{'@iot.count': 3,
 'value': [{'@iot.id': 2,
            '@iot.selfLink': 'https://sta.ci.taiwan.gov.tw/STA_AirQuality_EPAIoT/v1.0/Datastreams(2)',
            'Observations@iot.navigationLink': 'https://sta.ci.taiwan.gov.tw/STA_AirQuality_EPAIoT/v1.0/Datastreams(2)/Observations',
            'ObservedProperty@iot.navigationLink': 'https://sta.ci.taiwan.gov.tw/STA_AirQuality_EPAIoT/v1.0/Datastreams(2)/ObservedProperty',
            'Sensor@iot.navigationLink': 'https://sta.ci.taiwan.gov.tw/STA_AirQuality_EPAIoT/v1.0/Datastreams(2)/Sensor',
            'Thing@iot.navigationLink': 'https://sta.ci.taiwan.gov.tw/STA_AirQuality_EPAIoT/v1.0/Datastreams(2)/Thing',
            'description': '相對溼度',
            'name': 'Relative humidity',
            'observationType': 'http://www.opengis.net/def/observationType/OGC-OM/2.0/OM_Measurement',
            'observedArea': {'coordinates': [121.687045, 25.111078],
                             'type': 'Point'},
            'phenomenonTime': '2020-12-14T08:29:26.000Z/2020-12-14T10:03:26.000Z',
            'resultTime': None,
            'unitOfMeasurement': {'definition': 'https://en.wikipedia.org/wiki/Percentage',
                                  'name': 'percentage',
                                  'symbol': '%'}},
           {'@iot.id': 3,
            '@iot.selfLink': 'https://sta.ci.taiwan.gov.tw/STA_AirQuality_EPAIoT/v1.0/Datastreams(3)',
            'Observations@iot.navigationLink': 'https://sta.ci.taiwan.gov.tw/STA_AirQuality_EPAIoT/v1.0/Datastreams(3)/Observations',
            'ObservedProperty@iot.navigationLink': 'https://sta.ci.taiwan.gov.tw/STA_AirQuality_EPAIoT/v1.0/Datastreams(3)/ObservedProperty',
            'Sensor@iot.navigationLink': 'https://sta.ci.taiwan.gov.tw/STA_AirQuality_EPAIoT/v1.0/Datastreams(3)/Sensor',
            'Thing@iot.navigationLink': 'https://sta.ci.taiwan.gov.tw/STA_AirQuality_EPAIoT/v1.0/Datastreams(3)/Thing',
            'description': '溫度',
            'name': 'Temperature',
            'observationType': 'http://www.opengis.net/def/observationType/OGC-OM/2.0/OM_Measurement',
            'observedArea': {'coordinates': [121.687045, 25.111078],
                             'type': 'Point'},
            'phenomenonTime': '2020-12-14T08:30:26.000Z/2020-12-14T10:03:26.000Z',
            'resultTime': None,
            'unitOfMeasurement': {'definition': 'https://en.wikipedia.org/wiki/Celsius',
                                  'name': 'degree celsius',
                                  'symbol': '°C'}},
           {'@iot.id': 1,
            '@iot.selfLink': 'https://sta.ci.taiwan.gov.tw/STA_AirQuality_EPAIoT/v1.0/Datastreams(1)',
            'Observations@iot.navigationLink': 'https://sta.ci.taiwan.gov.tw/STA_AirQuality_EPAIoT/v1.0/Datastreams(1)/Observations',
            'ObservedProperty@iot.navigationLink': 'https://sta.ci.taiwan.gov.tw/STA_AirQuality_EPAIoT/v1.0/Datastreams(1)/ObservedProperty',
            'Sensor@iot.navigationLink': 'https://sta.ci.taiwan.gov.tw/STA_AirQuality_EPAIoT/v1.0/Datastreams(1)/Sensor',
            'Thing@iot.navigationLink': 'https://sta.ci.taiwan.gov.tw/STA_AirQuality_EPAIoT/v1.0/Datastreams(1)/Thing',
            'description': '細懸浮微粒 PM2.5',
            'name': 'PM2.5',
            'observationType': 'http://www.opengis.net/def/observationType/OGC-OM/2.0/OM_Measurement',
            'observedArea': {'coordinates': [121.687045, 25.111078],
                             'type': 'Point'},
            'phenomenonTime': '2020-12-14T08:28:26.000Z/2020-12-14T10:03:26.000Z',
            'resultTime': None,
            'unitOfMeasurement': {'definition': 'https://acronyms.thefreedictionary.com/ug%2Fm3',
                                  'name': 'microgram per cubic meter',
                                  'symbol': 'μg/m3'}}]}
```