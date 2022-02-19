"""Package class containing all package info"""
import csv

import data_structure
from data_structure import HashTable


class Package:
    def __init__(self, p_id, p_address, p_city, p_state, p_zip, p_delivery, p_mass, p_notes):
        self.id = p_id
        self.address = p_address
        self.city = p_city
        self.state = p_state
        self.zip = p_zip
        self.delivery = p_delivery
        self.mass = p_mass
        self.notes = p_notes
        self.truck = 0
        self.delivery_status = False
        self.delivery_time = None
        self.mileage = 0

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.id, self.address, self.city, self.state, self.zip,
                                                               self.delivery, self.mass, self.notes, self.truck,
                                                               self.delivery_status, self.delivery_time)

    def __repr__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.id, self.address, self.city, self.state, self.zip,
                                                               self.delivery, self.mass, self.notes, self.truck,
                                                               self.delivery_status, self.delivery_time)


# loading package data from Package_file.csv. Uses one parameter called file_name
# O(N) time complexity


def load_package_data(file_name, package_hash):
    with open(file_name) as package_info:
        data = csv.reader(package_info)
        for package in data:
            id = int(package[0])
            address = package[1]
            city = package[2]
            state = package[3]
            zip = package[4]
            delivery = package[5]
            mass = package[6]
            notes = package[7]

            package = Package(id, address, city, state, zip, delivery, mass, notes)
            package_hash.insert(id, package)


