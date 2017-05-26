"""
Python Wrapper for minergate api.

Made by Arttu Mahlakaarto
Feel free to donate:
BTC: 1PhfraqhnPt9B91WE4Ve5FVkJrxEiyenu1
ETH: 0xa34ad58c8213c2e473f2faf0ea521c59e9400915
ZEC: t1PYTokShkUHCUv6oeqwwHizXbjj7UQnX5c
"""
import json
import requests
host = "https://api.minergate.com"


def getProfitRating():
    """Return the list of all currencies sorted by profitability."""
    url = host+"/1.0/pool/profit-rating"
    response = requests.get(url)
    output = response.json()
    return(output)


def getTopHashrate():
    """Return top 10 miners, based on hashrate."""
    url = host+"/1.0/pool/top/hashrate"
    response = requests.get(url)
    output = response.json()
    return(output)


def getBlockchainInfo(cc):
    """Return Blockchain info for cc."""
    url = host+"/1.0/"+cc+"/status"
    response = requests.get(url)
    output = response.json()
    return(output)


def getLoginToken(user, passw, otp):
    """Login (Not working, server side issues)."""
    print("NOTE: May not work")
    s = requests.Session()
    url = host+"/1.0/auth/login/"
    args = {"email": user,
            "password": passw,
            "totp": otp}
    head = "'Content-type': 'application/json'"
    response = s.post(url, headers={head},  data=json.dumps(args))
    output = response.json()
    print(s.cookies.get_dict())
    return(output)


def getBalance(token):
    """Get Balances."""
    s = requests.Session()
    url = host+"/1.0/balance"
    response = s.get(url, headers={'token': token})
    output = response.json()
    return(output)


def getWorkers(token):
    """Get Workers."""
    s = requests.Session()
    url = host+"/1.0/workers"
    response = s.get(url, headers={'token': token})
    output = response.json()
    return(output)


def getMiningStats(token):
    """Get Mining stats."""
    s = requests.Session()
    url = host+"/1.0/mining/stats"
    response = s.get(url, headers={'token': token})
    output = response.json()
    return(output)


def getNickname(token):
    """Get nickname."""
    s = requests.Session()
    url = host+"/1.0/profile/nickname"
    response = s.get(url, headers={'token': token})
    output = response.json()
    return(output)
