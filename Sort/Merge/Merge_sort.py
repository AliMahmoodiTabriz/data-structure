class MergeSort:
    def merge(self, first_list, last_list):
        combined = []
        i = 0
        j = 0

        while i < len(first_list) and j < len(last_list):
            if first_list[i] < last_list[j]:
                combined.append(first_list[i])
                i += 1
            else:
                combined.append(last_list[j])
                j += 1

        while i < len(first_list):
            combined.append(first_list[i])
            i += 1
        while j < len(last_list):
            combined.append(last_list[j])
            j += 1
        return combined

    def merge_sort(self, mylist):
        if len(mylist) == 1:
            return mylist
        min_index = int(len(mylist)/2)
        left = self.merge_sort(mylist[:min_index])
        right = self.merge_sort(mylist[min_index:])
        return self.merge(left, right)


my_merg_sort = MergeSort()
print(my_merg_sort.merge_sort([4, 3, 2, 1]))
