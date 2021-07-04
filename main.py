import requests
import json
import secret

TOKEN = secret.TOKEN
CHAT_ID = secret.CHAT_ID



url = "https://cdt.hafas.de/bin/mgate.exe?rnd=1625242243755"


def sendMessage(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text="+ text
    requests.get(url)

sendMessage("JIMMY")

payload = json.dumps({
  "id": "686cvkkmgas69wck",
  "ver": "1.42",
  "lang": "deu",
  "auth": {
    "type": "AID",
    "aid": "SkC81GuwuzL4e0"
  },
  "client": {
    "id": "MMILUX",
    "type": "WEB",
    "name": "webapp",
    "l": "vs_webapp"
  },
  "formatted": False,
  "ext": "MMILUX.5",
  "svcReqL": [
    {
      "meth": "TripSearch",
      "req": {
        "jnyFltrL": [
          {
            "type": "GROUP",
            "mode": "INC",
            "value": "MYMIX_OEV"
          },
          {
            "type": "META",
            "mode": "INC",
            "meta": "notBarrierfree"
          },
          {
            "type": "PROD",
            "mode": "INC",
            "value": 295
          },
          {
            "type": "ATTRJ",
            "mode": "EXC",
            "value": "ad"
          }
        ],
        "getPolyline": True,
        "getPasslist": True,
        "gisFltrL": [
          {
            "type": "P",
            "mode": "FBT",
            "profile": {
              "type": "K",
              "checkInTime": "3"
            }
          },
          {
            "type": "P",
            "mode": "FBT",
            "profile": {
              "type": "P",
              "checkInTime": "3"
            }
          },
          {
            "type": "P",
            "mode": "FBT",
            "profile": {
              "type": "T",
              "checkInTime": "3"
            }
          },
          {
            "type": "P",
            "mode": "F",
            "profile": {
              "type": "F",
              "maxdist": "1500"
            }
          },
          {
            "type": "P",
            "mode": "B",
            "profile": {
              "type": "F",
              "maxdist": "1500"
            }
          },
          {
            "type": "M",
            "mode": "FBT",
            "meta": "foot_speed_normal"
          },
          {
            "type": "P",
            "mode": "FB",
            "profile": {
              "type": "B",
              "maxdist": "5000"
            }
          },
          {
            "type": "M",
            "mode": "FBT",
            "meta": "bike_speed_normal"
          }
        ],
        "depLocL": [
          {
            "lid": "A=1@O=Pfaffenthal-Kirchberg, Gare@X=6132917@Y=49618936@U=82@L=200417051@B=1@p=1619607441@",
            "name": "Pfaffenthal-Kirchberg, Gare"
          }
        ],
        "arrLocL": [
          {
            "lid": "A=1@O=Clervaux, Gare@X=6024624@Y=50061583@U=82@L=110101016@B=1@p=1619607441@",
            "name": "Clervaux, Gare"
          }
        ],
        "outFrwd": True,
        "liveSearch": False,
        "maxChg": "1000",
        "minChgTime": "-1",
        "getIV": True
      },
      "id": "1|5|"
    }
  ]
})
headers = {
  'Connection': 'keep-alive',
  'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
  'sec-ch-ua-mobile': '?0',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
  'Content-Type': 'application/json',
  'Accept': '*/*',
  'Origin': 'https://cdt.hafas.de',
  'Sec-Fetch-Site': 'same-origin',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Dest': 'empty',
  'Referer': 'https://cdt.hafas.de/?',
  'Accept-Language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7,la;q=0.6,fr;q=0.5'
}



response = requests.request("POST", url, headers=headers, data=payload).json()

dTimeS = int(response['svcResL'][0]['res']['outConL'][0]['dep']['dTimeS']) #time on plan
dTimeR = int(response['svcResL'][0]['res']['outConL'][0]['dep']['dTimeR'])#time with delay

aTimeS = int(response['svcResL'][0]['res']['outConL'][0]['arr']['aTimeS']) #time on plan
aTimeR = int(response['svcResL'][0]['res']['outConL'][0]['arr']['aTimeR']) #time with delay

direction = response['svcResL'][0]['res']['common']['dirL'][0]['txt']#time with delay

str_number = str(dTimeR)
time = ('{}:{}:{}'. format(str_number[:2], str_number[2:4], str_number[4:]))


if (dTimeR > 145500 and dTimeR < 151500) or (dTimeR > 122500 and dTimeR < 124500):
    sendMessage(f"RUN! Zuch fiirt um {time} richtung {direction}")
