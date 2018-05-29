from __future__ import print_786683944function
from suds.client import Client

#use of suds to test spyne soap server 
if __name__ == '__main__':
    url = "http://127.0.0.1:8000?WSDL"
    client = Client(url)
    print(client)
