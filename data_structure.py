"""Hash table class data structure to store package objects created in the package class. Chaining hash table has insert
search and remove methods. """


class HashTable:
    # Constructor
    # O(N) time complexity
    def __init__(self, length=10):
        self.table = []
        for i in range(length):
            self.table.append([])

    # Insert method
    # O(N) time complexity
    def insert(self, key, item):
        # determine which index to insert item in hash table
        hash_index = hash(key) % len(self.table)
        index_list = self.table[hash_index]

        # update if in the list
        for key_value in index_list:
            if key_value[0] == key:
                key_value[1] == item
                return True

        # append if not in the list
        new_key_item = [key, item]
        index_list.append(new_key_item)
        return True

    # Search for item in hash table
    # O(N) time complexity
    def search(self, key):
        hash_index = hash(key) % len(self.table)
        index_list = self.table[hash_index]

        for key_value in index_list:
            if key_value[0] == key:
                return key_value[1]
        return None

    # removes item from hash table.
    # O(N) time complexity
    def remove(self, key):
        hash_index = hash(key) % len(self.table)
        index_list = self.table[hash_index]

        for key_value in index_list:
            if key_value[0] == key:
                index_list.remove([key_value[0], key_value[1]])

