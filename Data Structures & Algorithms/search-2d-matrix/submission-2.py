class Solution:
    def searchMatrix(self, mat: List[List[int]], tar: int) -> bool:
        arr = []
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                arr.append(mat[i][j])
        lo, hi = 0, len(arr)-1
        ans = -1
        while(lo<=hi):
            mid = (lo+hi)//2
            # print(lo, mid, hi, ans)
            if arr[mid]<=tar:
                ans = mid
                lo = mid+1
            else:
                hi = mid-1
        # print(lo, hi, ans)
        if (ans==-1) or (ans!=-1 and arr[ans]!=tar):
            return False
        return True