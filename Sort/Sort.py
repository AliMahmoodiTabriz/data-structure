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

    # def selection_sort(self):
    #     min_index = 0
    #     def _sort(min_index):
    #         for i in range(min_index, len(self.data)-1, 1):
    #             if self.data[i] < self.data[i+1]:
    #                 min_index = i
    #                 break
    #         self.data[0], self.data[min_index] = self.data[min_index], self.data[0]

my_list = [4, 2, 6, 5, 1, 3]
my_sort = Sort(my_list)
my_sort.r_bubble_sort()
print(my_sort.data)
