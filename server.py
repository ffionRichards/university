from __future__ import print_function
import Pyro4
import uuid

#Gives remote access to class
@Pyro4.expose
class SalesAgency(object):
    def __init__(self):
        self._properties = {}

    @property
    def properties(self):
        return self._properties


#Add a property
    def add(self, owner, number, postcode, price):
        prop = {
            "Owner": owner,
            "Number": number,
            "Postcode": postcode,
            "Price": price
        }
#Give unique ID number 
#ID is unique due to uuid       
        unique_id = uuid.uuid4()
        if unique_id not in self._properties:
            self._properties[unique_id] = prop
#Delete property 
    def delete(self, unique_id):
        del self._properties[unique_id]

# Pyro server for the warehouse
def main():
    sale_agency = SalesAgency()
    sale_agency.add("David Bean", 16, "CF24 4QD", 250000)
    print("Sales agency created.")

    with Pyro4.Daemon() as daemon:
        sale_agency_uri = daemon.register(sale_agency)
        print("Sales agency registered.")

        with Pyro4.locateNS() as ns:
            ns.register("sales_agency", sale_agency_uri)

        print("Properties available.")
        daemon.requestLoop()


if __name__ == "__main__":
    main()
