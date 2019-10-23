class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        lens1 = len(nums1)
        lens2 = len(nums2)
        if lens1 < 1 and lens2 > 1:
            ids = lens2 // 2
            if lens2 % 2 == 0:
                return (nums2[ids] + nums2[ids - 1]) / 2
            else:
                return nums2[ids]
        if lens2 < 1 and lens1 > 1:
            ids = lens1 // 2
            if lens1 % 2 == 0:
                return (nums1[ids] + nums1[ids - 1]) / 2
            else:
                return nums1[ids]

        if (lens1 + lens2) % 2 == 0:
            target_0 = (lens1 + lens2) // 2 - 1
            target_1 = (lens1 + lens2) // 2
        else:
            target_0 = (lens1 + lens2) // 2
            target_1 = (lens1 + lens2) // 2

        l1 = 0
        l2 = 0
        count = -1
        value1 = 0
        value2 = 0
        while l1 < lens1 and l2 < lens2:
            if nums1[l1] < nums2[l2]:
                count += 1
                if count == target_0:
                    value1 = nums1[l1]
                if count == target_1:
                    value2 = nums1[l1]
                l1 += 1
            else:
                count += 1
                if count == target_0:
                    value1 = nums2[l2]
                if count == target_1:
                    value2 = nums2[l2]
                l2 += 1
        while count < target_1:
            if l2 < lens2:
                count += 1
                if count == target_0:
                    value1 = nums2[l2]
                if count == target_1:
                    value2 = nums2[l2]
                l2 += 1
            if l1 < lens1:
                count += 1
                if count == target_0:
                    value1 = nums1[l1]
                if count == target_1:
                    value2 = nums1[l1]
                l1 += 1
        return (value1 + value2) / 2
