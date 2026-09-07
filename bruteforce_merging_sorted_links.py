from unittest import TestCase


class Test(TestCase):
    def test_merge(self, nums1, m: int, nums2, n: int):
        nums1[m:] = nums2
        for j in range(m + n - 1):
            for i in range(m + n - 1):
                if nums1[i] > nums1[i + 1]:
                    temp = nums1[i]
                    nums1[i] = nums1[i + 1]
                    nums1[i + 1] = temp
                    return nums1
        self.fail()

    print(test_merge())
