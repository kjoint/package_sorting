# Keith M. Joint, Student ID: 001138774
# Nearest neighbor algorithm implemented in main.py using the functions truck_sort() and nearest()


import del_truck
import datetime
import time
from datetime import timedelta

# Manually loading trucks with list of unsorted packages

truck_1 = [1, 4, 6, 13, 14, 15, 16, 19, 20, 21, 25, 26,30, 34, 39, 40]
truck_2 = [2, 3, 5, 7, 10, 11, 12, 17, 18, 29, 31, 32, 33, 36, 37, 38]
truck_3 = [8, 9, 22, 23, 24, 27, 28, 35]
all_packages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
                29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]
# creating the start date times for each truck

truck_1_start = datetime.datetime(2021, 9, 22, 8, 0, 0)
truck_2_start = datetime.datetime(2021, 9, 22, 9, 10, 0)
truck_3_start = datetime.datetime(2021, 9, 22, 10, 30, 0)

# Creating truck objects

first_truck = del_truck.Truck(truck_1, truck_1_start)
second_truck = del_truck.Truck(truck_2, truck_2_start)
third_truck = del_truck.Truck(truck_3, truck_3_start)

# Updating the wrong address for package no. 9 received at 10:20 AM

del_truck.package_info.search(9).address = '410 S State St'
del_truck.package_info.search(9).city = 'Salt Lake City'
del_truck.package_info.search(9).state = 'UT'
del_truck.package_info.search(9).zip = '84111'


# Algorithm that takes a package ID and an unsorted list. Finds the next nearest package to the package passed in the
# signature of the function. Called by the truck sort function.
# O(n) time complexity


def nearest(t, location):
    if location == 0:
        start_index = 0
    else:
        start = del_truck.package_info.search(location).address
        start_index = int(del_truck.address_index.get(start))
    shortest_distance = 50
    shortest_location = 0

    for p in t.package_list:
        dest = del_truck.package_info.search(p).address
        dest_index = int(del_truck.address_index.get(dest))
        current_distance = del_truck.dist_table[dest_index][start_index]
        if current_distance < shortest_distance:
            shortest_distance = current_distance
            shortest_location = p

    t.mileage_list.append(shortest_distance)
    del_truck.package_info.search(shortest_location).mileage = shortest_distance
    del_truck.package_info.search(shortest_location).delivery_status = True
    if len(t.sorted_list) == 0:
        first_time = (shortest_distance / 18) * 60
        time = t.start_time + timedelta(minutes=first_time)
        del_truck.package_info.search(shortest_location).delivery_time = time
    else:
        time_min = (shortest_distance / 18) * 60
        # time delta the package that was passed in
        start_time = del_truck.package_info.search(location).delivery_time
        time = start_time + timedelta(minutes=time_min)
        del_truck.package_info.search(shortest_location).delivery_time = time

    return shortest_location

# Main sorting function. takes a truck object and a starting location and returns a list of packages
# sorted by next nearest location.
# O(n) time complexity
# truck_sort function together with nearest function has a time complexity of O(n^2)


def truck_sort(truck_index, origin):
    # truck.sorted_list.append(origin)
    # truck.package_list.remove(origin)
    next_dest = origin
    t = truck_list[truck_index]
    while len(t.package_list) > 0:
        next_dest = nearest(t, next_dest)  # Nearest is O(N)
        t.sorted_list.append(next_dest)
        t.package_list.remove(next_dest)
    # print(t.sorted_list)
    return t.sorted_list

# Creating a list of truck objects.
# O(n) time complexity


truck_list = [first_truck, second_truck, third_truck]
truck_sort(0, 0)
truck_sort(1, 0)
truck_sort(2, 0)


# Creating user interface allowing user to retrieve delivery information for a single package, all packages and the
# total miles traveled by all three trucks.


print('Welcome to the WGU package tracking system.')

total_miles = 0

# sum the total mileage of each truck
# O(N) time complexity

for truck in truck_list:
    total_miles += truck.mileage_total() + truck.get_return_trip_miles()
print('Total miles traveled is: ', round(total_miles, 2), 'miles')

user_input = -1
while user_input != '0':
    user_input = input('Main Menu: \n'
                       'To look up delivery information for a specific package please enter "1"\n'
                       'To look up information about all packages to be delivered enter "2"\n'
                       'To exit program at any time enter "0"\n')
    if user_input == '1':
        package_input = input('please enter a package ID\n')
        hour_string = input('Please enter the hour\n')
        minute_string = input('Please enter the minutes\n')
        package_datetime = del_truck.package_info.search(int(package_input)).delivery_time
        package_time = package_datetime.time()
        request_time = datetime.time(hour=int(hour_string), minute=int(minute_string))
        if request_time < package_time:
            print('package is en route, approximate delivery time is: ',
                  del_truck.package_info.search(package_input).time)
        if request_time >= package_time:
            print('Package delivered at ', package_time)
    if user_input == '2':
        hour_string = input('please enter the hour')
        minute_string = input('Please enter the minute')
        request_time = datetime.time(hour=int(hour_string), minute=int(minute_string))
        for p in all_packages:
            package_datetime = del_truck.package_info.search(p).delivery_time
            package_time = package_datetime.time()
            if request_time < package_time:
                print('Package ID: ', p, 'Package is en route. Approximate delivery time is ', package_time)
            else:
                print('Package ID: ', p, 'Package delivered at ', package_time)
    if user_input == '0':
        SystemExit


