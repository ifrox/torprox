import requests
from TorCtl import TorCtl
import random
import mechanize





def request(url):

	proxies = {'http':'127.0.0.1:8118'}

	userAgents = ['Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
				'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36',
				'Mozilla/5.0 (X11; Linux i586; rv:31.0) Gecko/20100101 Firefox/31.0',
				'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0',
				'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27',
				'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/534.55.3 (KHTML, like Gecko) Version/5.1.3 Safari/534.53.10',
				'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
				'Mozilla/5.0 (compatible, MSIE 11, Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko',
				'Opera/12.80 (Windows NT 5.1; U; en) Presto/2.10.289 Version/12.02',
				'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14',
				'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.28) Gecko/20120410 Firefox/3.6.28 Lunascape/6.7.1.25446'
				
	
				]

	user_agent = userAgents[random.randint(0,10)]

	headers = {"User-agent":user_agent,
				'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
				'Accept-Encoding':'gzip, deflate, sdch',
				'Accept-Language': 'en-US,en;q=0.8',
				'Connection':'keep-alive'}
	r = requests.get(url,headers=headers,proxies=proxies)

	return r.text

def brequest(url):
    br = mechanize.Browser()
	
    br.set_handle_equiv(True)
    #br.set_handle_gzip(True)
    br.set_handle_redirect(True)
    br.set_handle_referer(True)
    br.set_handle_robots(False)
    br.set_proxies({'http':'127.0.0.1:8118'})
    br.addheaders=[('User-agent','Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14'),
    				('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'),
    				('Accept-Encoding','none'),
    				('Accept-Language', 'en-US,en;q=0.8'),
    				('Connection','keep-alive')]
    br.open(url)
    return br.response().read()


def renew_ip_address():
	conn = TorCtl.connect(controlAddr="127.0.0.1", controlPort=9051, passphrase="lol")
	conn.send_signal("NEWNYM")
	conn.close()

