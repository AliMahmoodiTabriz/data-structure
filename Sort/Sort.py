class Sort:
    def __init__(self, values):
        self.data = values

    def r_bubble_sort(self):
        def _sort(count):
            for i in range(count):
                if count > i+1:
                    if self.data[i] > self.data[i+1]:
                        self.data[i], self.data[i +
                                                1] = self.data[i+1], self.data[i]
            if count >= 1:
                count = count-1
                _sort(count)
        _sort(len(self.data))

    def bubble_sort(self):
        for i in range(len(self.data)-1, 0, -1):
            for j in range(i):
                if self.data[j] > self.data[j+1]:
                    self.data[j], self.data[j +
                                            1] = self.data[j+1], self.data[j]

    def r_selection_sort(self):
        def _sort(old_index):
            min_index = old_index
            if old_index == len(self.data):
                return
            for i in range(old_index, len(self.data), 1):
                if self.data[min_index] > self.data[i]:
                    min_index = i
            self.data[old_index], self.data[min_index] = self.data[min_index], self.data[old_index]
            old_index += 1
            _sort(old_index)
        _sort(0)

    def selection_sort(self):
        for i in range(len(self.data)-1):
            min_index = i
            for j in range(i+1, len(self.data)):
                if self.data[min_index] > self.data[j]:
                    min_index = j
            if i != min_index:
                self.data[i], self.data[min_index] = self.data[min_index], self.data[i]

    def insertion_sort(self):
        for i in range(1, len(self.data)):
            temp = self.data[i]
            j = i-1
            while temp < self.data[j] and j > -1:
                self.data[j+1], self.data[j] = self.data[j], self.data[j+1]
                j -= 1


my_list = [4, 2, 6, 5, 1, 3]
my_sort = Sort(my_list)
my_sort.insertion_sort()
print(my_sort.data)
