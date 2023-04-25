from functools import reduce

nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
nums3 = [7, 8, 9]

sum_of_list_args = reduce(lambda x, y: x + y,
                          list(map(lambda x, y, z: x + y + z, nums1, nums2, nums3)))
