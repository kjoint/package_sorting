import data_structure
import csv
import package


class Truck:
    def __init__(self, package_list, start_time):
        self.package_list = package_list
        self.sorted_list = []
        self.mileage_list = []
        self.mileage = 0
        self.start_time = start_time

    def mileage_total(self):
        miles = 0
        for p in self.sorted_list:
            miles += package_info.search(p).mileage
        return miles

    def get_return_trip_miles(self):
        last = self.sorted_list[-1:]
        last_address = package_info.search(last[0]).address
        last_index = address_index.get(last_address)
        return_distance = dist_table[int(last_index)][0]
        return return_distance

# create a function that returns the number of packages left on a truck
# boolean is truck full
# O(N^2) time complexity


with open('Distance_file.csv') as distances:
    data = csv.reader(distances)
    dist_table = list(data)
    for x, row in enumerate(dist_table):
        for y, col in enumerate(row):
            dist_table[x][y] = float(dist_table[x][y])


# creating a dictionary of Address key/row index values
# O(N) time complexity
address_index = {}

with open('distance_name_key.csv') as keys:
    data = csv.reader(keys)
    address_index = {rows[0]: rows[1] for rows in data}


package_info = data_structure.HashTable()
package.load_package_data('Package_file.csv', package_info)



