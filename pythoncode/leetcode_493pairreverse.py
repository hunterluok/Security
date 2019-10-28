

class Solution:
    def reversePairs(self, nums) -> int:
        new = nums[:]
        ends = len(nums) - 1
        start = 0
        count = self.get_count(nums, new, start, ends)
        print("data is {}".format(nums))
        print("new is {}".format(new))
        return count

    def get_count(self, data, new, start, ends):
        if len(data) < 1:
            return 0

        if start == ends:
            new[start] = data[start]
            return 0

        length = (ends - start) // 2
        left = self.get_count(new, data, start, start+length)
        right = self.get_count(new, data, start+length+1, ends)

        count = 0

        right_start = start + length + 1

        left_index = start + length
        right_index = ends
        new_index = ends


        while left_index >= start and right_index >= right_start:
            # 注意 这里的区别
            if data[left_index] >= data[right_index]:
                new[new_index] = data[left_index]
                temp_index = right_index
                while temp_index >= right_start:
                    if data[left_index] > 2 * data[temp_index]:
                        count += 1
                        print("ANOTH {}--{}".format(data[left_index], data[temp_index]))
                    temp_index -= 1

                left_index -= 1
                new_index -= 1
            else:
                new[new_index] = data[right_index]
                new_index -= 1
                right_index -= 1

        while left_index >= start:
            new[new_index] = data[left_index]
            left_index -= 1
            new_index -= 1
        while right_index >= start + length + 1:
            new[new_index] = data[right_index]
            new_index -= 1
            right_index -= 1
        return left + right + count


if __name__ == "__main__":
    # data = [7, 5, 6, 4]
    #data = [1, 3,2,3,1]
    # data = [2, 4, 3, 5, 1]
    # data = [-5, -5]
    data = [5, 4, 3, 2, 1]
    my = Solution()
    print(my.reversePairs(data))
