#!usr/bin/env python
# coding:utf-8

# There are two sorted arrays nums1 and nums2 of size m and n respectively.
#
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
#
# Example 1:
# nums1 = [1, 3]
# nums2 = [2]
#
# The median is 2.0
# Example 2:
# nums1 = [1, 2]
# nums2 = [3, 4]
#
# The median is (2 + 3)/2 = 2.5


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1 = len(nums1)
        len2 = len(nums2)
        if (len1 + len2) % 2:
            flag = False
        else:
            flag = True

        count = 0
        i = 0; start_i = 0; end_i = len1
        j = 0; start_j = 0; end_j = len2
        while True:
            if nums1[i] <= nums2[j]:
                mid_i = (start_i + end_i) / 2
            else:
                mid_j = (start_j + end_j) / 2

            pass
        return 0


def str2int(num):
    return int(num.strip())


if __name__ == '__main__':
    st = Solution()
    num1 = map(str2int, raw_input().strip().split(','))
    num2 = map(str2int, raw_input().strip().split(','))
    print st.findMedianSortedArrays(num1, num2)