# restAPI

[![Python version](https://img.shields.io/badge/restAPI-0.29-pink?style=flat-square)](https://aayush.wtf) [![Python version](https://img.shields.io/badge/Python-3.7-green?style=flat-square)](https://aayush.wtf) [![Maintained](https://img.shields.io/badge/Maintained-yes-orange?style=flat-square)](https://aayush.wtf) [![OS](https://img.shields.io/badge/OS--red?style=flat-square)](https://apple.com)

## Device-info rest api, made using flask

> ### What does it do?
> Grabs various device **information** and "turns" it into an api, which can be accessed from anywhere.  

> ### What kind of information?
> Battery Info, Cpu Usage, Disk, Ram usage, User Info ...

> ### What can we do with the data?
> Make charts, log them, make an web/android/ios app for it.. the possibilities are endles.

> ### How can we access the data?
> The data is hosted on port 8080 *configurable* so by simply opening http://localhost:8080/api in a web-browser,
or typing 
`curl http://localhost:8080/api` in terminal.


### API output eg:
```json
  "battery_info": {
    "Charge": 100, 
    "Charging": "No", 
    "Connected": "Yes", 
    "data": {...}
  }, 
  "cpu": {
    "used": 82.4,
    "temp" : 42.2
  }, 
  "userInfo": {
    "uname": "Darwin", 
    "username": "aayushpokharel"
  }, 
  "vm_stat": {
    "\"Translation faults\"": "72532354", 
    "Anonymous pages": "902183", 
    "Compressions": "647382", 
    "Decompressions": "172141", 
    "File-backed pages": "487363", 
    "Pageins": "2446247", 
    "Pageouts": "11464", 
    "Pages active": "698073", 
    "Pages copy-on-write": "13049615", 
    "Pages free": "124517", 
    "Pages inactive": "667096", 
    "Pages occupied by compressor": "162257", 
    "Pages purgeable": "82111", 
    "Pages purged": "236144", 
    "Pages reactivated": "629222", 
    "Pages speculative": "29377", 
    "Pages stored in compressor": "351785", 
    "Pages throttled": "0", 
    "Pages wired down": "415305", 
    "Pages zero filled": "45670391"
  }
}
```
### How to Install?
```bash
git clone https://github.com/Aayush9029/restAPI.git

cd restApi

pip install -r requirements.txt -y

python3 main.py
```


---
### Web Request Example:
<img src="https://raw.githubusercontent.com/Aayush9029/restAPI/master/img/apiImage.png"/>

### Curl Example: 
<img src="https://raw.githubusercontent.com/Aayush9029/restAPI/master/img/curlImage.png"/>

---
*tested on macOS catalina*
