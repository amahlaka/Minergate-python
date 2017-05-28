# Minergate-python
Python wrapper for minergate api
## Usage:
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

## NOTE:
Currently minergate api has some problems with ProfitRating and login
Instead of returning the login token as it should, it returns `{"code":"InternalError","message":"Cannot read property 'send' of undefined"}`This is a error on server side and we are waiting for a fix, meanwhile, you can acquire the login token using a browser

##TODO:
- Add manual token retrieval process
- ??
- Profit
