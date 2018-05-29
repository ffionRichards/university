import sys
import Pyro4
import Pyro4.util
from employee import Employee

#remote exception
sys.excepthook = Pyro4.util.excepthook
#retriving proxy for name server from within the network 
#creates Proxy 
#connects to pyro object 
def find_sales_agency():
    sales_agency = None
    with Pyro4.locateNS() as ns:
        uri = ns.lookup("sales_agency")
        sales_agency = Pyro4.Proxy(uri)
    if not sales_agency:
        raise ValueError("no sales agency found!")
    return sales_agency


sales_agency = find_sales_agency()
#employee's actions 
mark = Employee("Mark")
mark.add(sales_agency)
mark.remove(sales_agency)

#Employee- search by price range example
results = mark.search_by_pric78668394e_range(1000, 251000)
for result in results:
    print(result.owner)
