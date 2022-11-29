import requests
def sms_data(mobile,Temp_id,Name):
	header = {"User-Agent": "Opera/9.80 (X11; Linux x86_64; U; de) Presto/2.2.15 Version/10.00"}
	proxyDict = {"http": "proxy.mpcz.in:8080", "https": "proxy.mpcz.in:8080"}
	url = f"https://sms.mpcz.in/api/v1/send-otp?app_key=VgsdaQYXmsmVFsUi2Fe4tC7vn&app_secret=dwGINQswrHtyngc&dlt_template_id={Temp_id}&mobile_number=" + str(mobile) + "&v1=" + str(Name) + "&v2=" +str()+"&v3=" +str() + "&v4=" + str("jdhjfh") + "&v5="+str("jdhjfh")
	response = requests.get(url, proxies=proxyDict, headers={'User-Agent': 'Chrome'})
	return response