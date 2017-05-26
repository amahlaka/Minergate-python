# Minergate-python
Python wrapper for minergate api
Usage:
```
import mgPython
getTopHashrate() # Returns top 10 list of miners per currency
getLoginToken(username, password, 2fa code) # Returns login token NOTE: server problems have broken this for now
getMiningStats(token) # Returns mining stats
getWorkers(token) # returns Worker stats
```

All functions return response in json format, so you can do:
```
workers = getWorkers(token)
print(workers["btc"])
```
to get info about your Bitcoin miners
