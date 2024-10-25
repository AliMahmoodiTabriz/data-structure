class WaterContainer:
    def maxArea(self, hight: list[int]) -> int:
        max_area = 0
        l = 0
        r = len(hight) - 1
        while l < r:
            lenght = self.min(hight[l], hight[r])
            width = r - l
            area = width * lenght
            max_area = self.max(max_area, area)
            if hight[l] < hight[r]:
                l += 1
            else:
                r -= 1
        return max_area

    def min(self, left, right):
        if left < right:
            return left
        return right

    def max(self, left, right):
        if left > right:
            return left
        return right


my_container = WaterContainer()
print(my_container.maxArea([1, 8, 6, 2, 5, 7]))
