from __future__ import print_function
from spyne.protocol.soap import Soap11
from spyne import Application, srpc, ServiceBase, Iterable, Unicode
from spyne.server.wsgi import WsgiApplication

#defining class attribute - sales agency 

class SalesAgencyService(ServiceBase):
    def find_sales_agency(self):
        sales_agency = None
        with Pyro4.locateNS() as ns:
            uri = ns.lookup("sales_agency")
            sales_agency = Pyro4.Proxy(uri)
        if not sales_agency:
            raise ValueError("no sales agency found!")
        return sales_agency
# remote call and defines type/order of soap parameters
    @srpc(_returns=Iterable(Unicode))
    def get_properties():
        sales_agency = self.find_sales_agency()
        return sales_agency.properties
#request protocol 
application  = Application([SalesAgencyService],
    tns='salesAgency.http',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11()
)
#wrap spyne app with Wsgi wrapper 
wsgi_application = WsgiApplication(application)
#register WSGI app as handler to server 
if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    server = make_server('127.0.0.1', 8000, wsgi_application)
    server.serve_forever()
