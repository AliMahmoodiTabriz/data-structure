class QuickSort:
    def swap(self, my_list, index1, index2):
        my_list[index1], my_list[index2] = my_list[index2], my_list[index1]

    def pivot(self, my_list, pivot_index, end_index):
        swap_index = pivot_index
        for i in range(pivot_index+1, end_index + 1):
            if my_list[i] < my_list[pivot_index]:
                swap_index += 1
                self.swap(my_list, swap_index, i)
        self.swap(my_list, pivot_index, swap_index)
        return swap_index

    def _quick_sort(self, my_list, left, right):
        if right < left:
            return
        pivot_index = self.pivot(my_list, left, right)
        self._quick_sort(my_list, left, pivot_index-1)
        self._quick_sort(my_list, pivot_index+1, right)
        return my_list

    def quick_sort(self, my_list):
        return self._quick_sort(my_list, 0, len(my_list)-1)


my_sort = QuickSort()
my_list = [4, 6, 1, 7, 3, 2, 5]
print(my_sort.quick_sort(my_list))
