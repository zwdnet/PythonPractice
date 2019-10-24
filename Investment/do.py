# coding:utf-8
# 量化交易框架:执行层


import requests
import json
import base64
import hmac
import hashlib
import datetime
import time


if __name__ == "__main__":
	base_url = "https://api.sandbox.gemini.com"
	endpoint = "/v1/order/new"
	url = base_url + endpoint
	
	gemini_api_key = "account-PsnWZPOnOf0FatEh3pWj"
	gemini_api_secret = "49wC5psfvDhMmtKaNzmmVg42yYYb"
	
	t = datetime.datetime.now()
	payload_nonce = str(int(time.mktime(t.timetuple()) * 1000))
	
	payload = {
		"request" : "/v1/order/new",
		"nonce" : payload_nonce,
		"symbol" : "btcusd",
		"amount" : "5",
		"price" : "7428.00",
		"side" : "buy",
		"type" : "exchange limit",
		"options" : ["maker-or-cancel"]
	}
	
	encoded_payload = json.dumps(payload).encode()
	b64 = base64.b64encode(encoded_payload)
	signature = hmac.new(bytes(gemini_api_secret, "latin-1"), b64, hashlib.sha384).hexdigest()
	print(signature)
	
	requests_header = {
		"Content-Type" : "text/plain",
		"Content-Length" : "0",
		"X-GEMINI-APIKEY" : gemini_api_key,
		"X-GEMINI-PAYLOAD" : b64, 
		"X-GEMINI-SIGNATURE" : signature,
		"Cache-Control" : "no-cache"
	}
	
	response = requests.post(url,
	                                               data = None,
	                                               headers = requests_header)
	new_order = response.json()
	print(new_order)
	