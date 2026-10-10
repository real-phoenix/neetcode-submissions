class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = []
        idx1, idx2 = 0, 0
        while(idx1<len(nums1) and idx2<len(nums2)):
            if nums1[idx1]<nums2[idx2]:
                nums.append(nums1[idx1])
                idx1+=1
            else:
                nums.append(nums2[idx2])
                idx2+=1

        while(idx1<len(nums1)):
            nums.append(nums1[idx1])
            idx1+=1

        while(idx2<len(nums2)):
            nums.append(nums2[idx2])
            idx2+=1

        n = len(nums)
        if n%2==0:
            return ((nums[(n//2)-1] + nums[n//2]))/2
        else:
            return nums[n//2]
