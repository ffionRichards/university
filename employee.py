from __future__ import print_function
import sys
import Pyro4

#runs in different versions of python 
if sys.version_info < (3, 0):
    input = raw_input


# Employee's details
class Employee(object):
    def __init__(self, name):
        self.name = name

# Search by Price Range 
    def search_by_price_range(self, sales_agency, minimum, maximum):
        results = set()
        for prop in sales_agency.properties:
            if prop["Price"] > minimum and prop["Price"] < maximum:
                results.add(prop)
        return results
#Search by postcode
    def search_by_postcode(self, sales_agency, postcode):
        results = set()
        for prop in sales_agency.properties:
            if prop["postcode"] == postcode:
                results.add(prop)
        return results
 #add a property - require details on owner, number, postcode, price 
 #If all details have been entered then property can be added       
    def add(self, sales_agency):
        print("Properties: ", sales_agency.properties)
        print("Please give me details of a property to add.")
        owner = input("Who is the property owner:").strip()
        number = input("What is the property number:").strip()
        postcode = input("What is the property postcode:").strip()
        price = input("What is the property price:").strip()
        if owner and number and postcode and price:
            sales_agency.add(owner, number, postcode, price)
        print("Properties: ", sales_agency.properties)
#delete a property from the system given its unique ID 
    def delete(self, sales_agency):
        print("Properties: ", sales_agency.properties)
        unique_id = input("Delete Property: '").strip()
        if unique_id:
            sales_agency.delete(unique_id)
        print("Properties: ", sales_agency.properties)
