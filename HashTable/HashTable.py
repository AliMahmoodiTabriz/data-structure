class HashTable:
    def __init__(self, size=7):
        self.data_map = [None] * 7

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter)*23) % len(self.data_map)
        return my_hash

    def print(self):
        for i, val in enumerate(self.data_map):
            print(i, " : ", val)

    def set(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get(self, key):
        index = self.__hash(key)
        data = self.data_map[index]
        if data is not None:
            for item in enumerate(data):
                if item[1][0] == key:
                    return item[1][1]
        return None

    def keys(self):
        allkes = []
        for nodes in enumerate(self.data_map):
            if nodes[1] is not None:
                for node in enumerate(nodes[1]):
                    allkes.append(node[1][0])
        return allkes


def item_in_common1(list1, list2):
        table = HashTable()
        for item in list1:
            table.set(str(item), True)

        for item in list2:
            if table.get(str(item)) is True:
                return True
        return False


def item_in_common(list1, list2):
    my_dic = {}
    for i,item in list1:
        my_dic[i] = True
    for i in list2:
         if i in my_dic:
             return True
    return False
# my_table = HashTable()
# my_table.set("bolts", 1400)
# my_table.set("washres", 50)
# my_table.set("lumber", 70)
# # print(my_table.get("ali"))
# # print(my_table.get("alii"))
# # print(my_table.get("al2222i"))
# print(my_table.keys())

list1=[1,2,3]
list2=[4,5,6]
print(item_in_common(list1,list2))
